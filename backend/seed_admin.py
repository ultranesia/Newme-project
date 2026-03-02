"""Seed admin user untuk NEWME CLASS"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def seed_admin():
    # Connect to MongoDB
    mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
    db_name = os.environ.get('DB_NAME', 'newme_database')
    
    client = AsyncIOMotorClient(mongo_url)
    db = client[db_name]
    
    # Check if admin already exists
    existing_admin = await db.admin_users.find_one({"email": "admin@newme.com"})
    
    if existing_admin:
        print("✅ Admin sudah ada di database")
        return
    
    # Create admin user
    hashed_password = pwd_context.hash("admin123")
    
    admin_data = {
        "username": "admin",
        "email": "admin@newme.com",
        "password": hashed_password,
        "role": "super_admin",
        "createdAt": datetime.utcnow(),
        "lastLogin": None
    }
    
    result = await db.admin_users.insert_one(admin_data)
    print(f"✅ Admin berhasil dibuat dengan ID: {result.inserted_id}")
    print(f"   Email: admin@newme.com")
    print(f"   Password: admin123")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(seed_admin())
