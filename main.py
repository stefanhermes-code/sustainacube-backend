from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from passlib.hash import bcrypt
import csv
import os
from datetime import datetime
from typing import List, Dict, Any

app = FastAPI(title="SustainaCube Backend API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File paths
USERS_CSV = "users.csv"
USAGE_CSV = "usage_log.csv"

# Pydantic models
class User(BaseModel):
    email: str
    password: str

class UsageLog(BaseModel):
    email: str
    question_count: int
    cost_estimate: float

class UserResponse(BaseModel):
    email: str
    status: str
    message: str

# Utility functions
def read_users() -> List[Dict[str, str]]:
    """Read users from CSV file"""
    if not os.path.exists(USERS_CSV):
        return []
    with open(USERS_CSV, 'r', newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def append_usage(email: str, questions: int, cost: float):
    """Append usage log to CSV file"""
    file_exists = os.path.exists(USAGE_CSV)
    with open(USAGE_CSV, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "email", "question_count", "cost_estimate"])
        writer.writerow([datetime.utcnow().isoformat(), email, questions, cost])

def verify_password(password: str, hashed: str) -> bool:
    """Verify password against hash"""
    return bcrypt.verify(password, hashed)

# API Endpoints
@app.get("/")
async def root():
    return {
        "message": "SustainaCube Backend API",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "auth": "/auth",
            "log_usage": "/log_usage",
            "usage_stats": "/usage_stats",
            "health": "/health"
        }
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "users_file_exists": os.path.exists(USERS_CSV),
        "usage_file_exists": os.path.exists(USAGE_CSV)
    }

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.post("/auth", response_model=UserResponse)
async def authenticate_user(user: User):
    """Authenticate user with email and password"""
    users = read_users()
    
    for u in users:
        if u["email"] == user.email:
            # Check if password is hashed or plain text
            stored_password = u.get("password_hash") or u.get("password", "")
            
            # If it's a hash, verify it; if it's plain text, compare directly
            if stored_password.startswith("$2b$"):  # bcrypt hash starts with $2b$
                password_valid = verify_password(user.password, stored_password)
            else:
                password_valid = (user.password == stored_password)
            
            if password_valid:
                return UserResponse(
                    email=user.email,
                    status="authenticated",
                    message="Login successful"
                )
    
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/log_usage")
async def log_usage(entry: UsageLog):
    """Log user usage statistics"""
    try:
        append_usage(entry.email, entry.question_count, entry.cost_estimate)
        return {"status": "logged", "message": "Usage logged successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to log usage: {str(e)}")

@app.get("/usage_stats")
async def get_usage_stats():
    """Get usage statistics for all users"""
    if not os.path.exists(USAGE_CSV):
        return []
    
    stats = {}
    with open(USAGE_CSV, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row["email"]
            questions = int(row["question_count"])
            cost = float(row["cost_estimate"])
            timestamp = row["timestamp"]
            
            if email not in stats:
                stats[email] = {
                    "email": email,
                    "total_questions": 0,
                    "total_cost": 0.0,
                    "sessions": 0,
                    "last_activity": timestamp
                }
            
            stats[email]["total_questions"] += questions
            stats[email]["total_cost"] += cost
            stats[email]["sessions"] += 1
            
            # Keep track of most recent activity
            if timestamp > stats[email]["last_activity"]:
                stats[email]["last_activity"] = timestamp
    
    return list(stats.values())

@app.get("/users")
async def get_users():
    """Get all users (for admin purposes)"""
    users = read_users()
    # Don't return password hashes for security
    safe_users = []
    for user in users:
        safe_user = {k: v for k, v in user.items() if k not in ["password", "password_hash"]}
        safe_users.append(safe_user)
    return safe_users

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)