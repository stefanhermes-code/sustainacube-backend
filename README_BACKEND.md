# 🌱 SustainaCube Backend API

FastAPI backend for SustainaCube applications providing user authentication and usage tracking.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements_backend.txt
```

### 2. Run Locally
```bash
python main.py
```

### 3. API Documentation
- **Swagger UI**: http://localhost:10000/docs
- **ReDoc**: http://localhost:10000/redoc

## 📊 API Endpoints

### Authentication
- `POST /auth` - Authenticate user with email/password
- `GET /users` - Get all users (admin)

### Usage Tracking
- `POST /log_usage` - Log user activity and costs
- `GET /usage_stats` - Get usage statistics

### Health & Status
- `GET /` - API information
- `GET /health` - Health check
- `GET /ping` - Simple ping test

## 🔧 Configuration

### Environment Variables
- `PORT` - Server port (default: 10000)

### Data Files
- `users.csv` - User authentication data
- `usage_log.csv` - Usage tracking logs

## 🚀 Deployment

### Render.com
1. Connect GitHub repository
2. Set build command: `pip install -r requirements_backend.txt`
3. Set start command: `python main.py`
4. Set port: `10000`

### Docker
```bash
docker build -t sustainacube-backend .
docker run -p 10000:10000 sustainacube-backend
```

## 📝 Data Format

### Users CSV
```csv
email,password_hash
user@example.com,$2b$12$...
```

### Usage Log CSV
```csv
timestamp,email,question_count,cost_estimate
2025-01-01T12:00:00,user@example.com,1,0.05
```
