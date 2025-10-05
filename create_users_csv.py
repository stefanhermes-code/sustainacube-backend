"""
Create users.csv with proper password hashes for the API
"""

from passlib.hash import bcrypt
import csv

def create_users_csv():
    """Create users.csv with hashed passwords"""
    
    # Read users from Corporate Users.csv
    users = []
    try:
        with open("Corporate Users.csv", 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get('Email', '').strip():
                    users.append({
                        'email': row['Email'].strip(),
                        'password': row['Password'].strip()
                    })
    except FileNotFoundError:
        print("Corporate Users.csv not found. Using sample data.")
        users = [
            {'email': 'stefan.hermes@htcglobal.asia', 'password': 'Windmill2025'},
            {'email': 'b.tenbrink@fdf-management.com', 'password': 'Jona2025'}
        ]
    
    # Create users.csv with hashed passwords
    with open("users.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['email', 'password_hash'])
        
        for user in users:
            hashed_password = bcrypt.hash(user['password'])
            writer.writerow([user['email'], hashed_password])
            print(f"Created hash for {user['email']}")
    
    print(f"\nCreated users.csv with {len(users)} users")
    print("Upload this file to your GitHub repository for the API to use.")

if __name__ == "__main__":
    create_users_csv()
