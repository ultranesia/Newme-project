"""
Seed 5 additional PAID questions for deeper personality analysis
Total will be: 5 FREE + 25 PAID = 30 questions
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime

async def seed_additional_questions():
    mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
    db_name = os.environ.get('DB_NAME', 'newme_database')
    
    client = AsyncIOMotorClient(mongo_url)
    db = client[db_name]
    
    # Count existing questions
    existing_free = await db.questions.count_documents({"isFree": True})
    existing_paid = await db.questions.count_documents({"isFree": False})
    
    print(f"📊 Current questions: {existing_free} FREE + {existing_paid} PAID = {existing_free + existing_paid} total")
    
    # 5 additional PAID questions for deeper analysis
    additional_questions = [
        {
            "category": "conflict_resolution",
            "text": "Ketika menghadapi konflik dengan rekan kerja, saya cenderung:",
            "isFree": False,
            "order": 21,
            "options": [
                {
                    "text": "Langsung menghadapi dan menyelesaikan masalah secara terbuka",
                    "scores": {
                        "extrovert": 3,
                        "api": 2,
                        "logam": 1,
                        "komunikasi": 3,
                        "assertif": 3
                    }
                },
                {
                    "text": "Mencari mediator atau pihak ketiga untuk membantu",
                    "scores": {
                        "introvert": 2,
                        "tanah": 2,
                        "empati": 2,
                        "diplomatis": 3
                    }
                },
                {
                    "text": "Memberikan waktu untuk menenangkan diri sebelum membahas",
                    "scores": {
                        "introvert": 3,
                        "air": 2,
                        "logika": 2,
                        "reflektif": 3
                    }
                },
                {
                    "text": "Mencari kompromi yang menguntungkan kedua belah pihak",
                    "scores": {
                        "ambivert": 2,
                        "kayu": 2,
                        "empati": 3,
                        "kolaboratif": 3
                    }
                }
            ],
            "createdAt": datetime.utcnow()
        },
        {
            "category": "stress_management",
            "text": "Saat menghadapi deadline yang ketat, cara saya mengelola stres adalah:",
            "isFree": False,
            "order": 22,
            "options": [
                {
                    "text": "Membuat to-do list detail dan menyelesaikannya satu per satu",
                    "scores": {
                        "introvert": 2,
                        "logam": 3,
                        "logika": 3,
                        "terorganisir": 3
                    }
                },
                {
                    "text": "Bekerja cepat dengan energi tinggi sampai selesai",
                    "scores": {
                        "extrovert": 3,
                        "api": 3,
                        "kinestetik": 2,
                        "energetik": 3
                    }
                },
                {
                    "text": "Mencari bantuan tim dan mendelegasikan tugas",
                    "scores": {
                        "extrovert": 2,
                        "kayu": 2,
                        "komunikasi": 3,
                        "kolaboratif": 3
                    }
                },
                {
                    "text": "Tetap tenang dan fokus pada prioritas utama",
                    "scores": {
                        "introvert": 3,
                        "air": 3,
                        "logika": 2,
                        "resilient": 3
                    }
                }
            ],
            "createdAt": datetime.utcnow()
        },
        {
            "category": "learning_style",
            "text": "Cara saya paling efektif mempelajari hal baru adalah:",
            "isFree": False,
            "order": 23,
            "options": [
                {
                    "text": "Membaca buku, artikel, atau dokumentasi secara mendalam",
                    "scores": {
                        "introvert": 3,
                        "logam": 2,
                        "logika": 3,
                        "analitik": 3
                    }
                },
                {
                    "text": "Diskusi dan brainstorming dengan orang lain",
                    "scores": {
                        "extrovert": 3,
                        "api": 2,
                        "komunikasi": 3,
                        "sosial": 3
                    }
                },
                {
                    "text": "Praktik langsung dan trial-error",
                    "scores": {
                        "extrovert": 2,
                        "kayu": 3,
                        "kinestetik": 3,
                        "praktis": 3
                    }
                },
                {
                    "text": "Menonton video tutorial atau demonstrasi visual",
                    "scores": {
                        "introvert": 2,
                        "air": 2,
                        "visual": 3,
                        "observer": 2
                    }
                }
            ],
            "createdAt": datetime.utcnow()
        },
        {
            "category": "work_environment",
            "text": "Lingkungan kerja yang membuat saya paling produktif adalah:",
            "isFree": False,
            "order": 24,
            "options": [
                {
                    "text": "Ruang kerja pribadi yang tenang dan terorganisir",
                    "scores": {
                        "introvert": 3,
                        "logam": 3,
                        "individual": 3,
                        "fokus": 3
                    }
                },
                {
                    "text": "Ruang terbuka dengan interaksi tim yang dinamis",
                    "scores": {
                        "extrovert": 3,
                        "api": 3,
                        "komunikasi": 3,
                        "kolaboratif": 3
                    }
                },
                {
                    "text": "Campuran antara ruang kolaborasi dan area fokus pribadi",
                    "scores": {
                        "ambivert": 3,
                        "kayu": 2,
                        "adaptif": 3,
                        "fleksibel": 2
                    }
                },
                {
                    "text": "Fleksibel - bisa di kantor, cafe, atau remote",
                    "scores": {
                        "ambivert": 2,
                        "air": 3,
                        "adaptif": 3,
                        "mandiri": 2
                    }
                }
            ],
            "createdAt": datetime.utcnow()
        },
        {
            "category": "innovation",
            "text": "Ketika diminta menghasilkan ide kreatif, pendekatan saya adalah:",
            "isFree": False,
            "order": 25,
            "options": [
                {
                    "text": "Riset mendalam terlebih dahulu, lalu buat konsep terstruktur",
                    "scores": {
                        "introvert": 3,
                        "logam": 3,
                        "logika": 3,
                        "analitik": 3,
                        "metodis": 3
                    }
                },
                {
                    "text": "Brainstorming spontan dengan tim untuk mengumpulkan berbagai perspektif",
                    "scores": {
                        "extrovert": 3,
                        "api": 3,
                        "komunikasi": 3,
                        "sosial": 3,
                        "kolaboratif": 3
                    }
                },
                {
                    "text": "Membuat prototype cepat dan test secara langsung",
                    "scores": {
                        "extrovert": 2,
                        "kayu": 3,
                        "kinestetik": 3,
                        "praktis": 3,
                        "eksperimental": 3
                    }
                },
                {
                    "text": "Refleksi mendalam dan eksplorasi berbagai kemungkinan secara internal",
                    "scores": {
                        "introvert": 3,
                        "air": 3,
                        "visual": 2,
                        "investigatif": 3,
                        "reflektif": 3
                    }
                }
            ],
            "createdAt": datetime.utcnow()
        }
    ]
    
    # Insert additional questions
    if additional_questions:
        result = await db.questions.insert_many(additional_questions)
        print(f"✅ Added {len(result.inserted_ids)} new PAID questions")
    
    # Count final
    final_free = await db.questions.count_documents({"isFree": True})
    final_paid = await db.questions.count_documents({"isFree": False})
    total = final_free + final_paid
    
    print(f"\n✨ Final question count:")
    print(f"   - FREE questions: {final_free}")
    print(f"   - PAID questions: {final_paid}")
    print(f"   - TOTAL questions: {total}")
    
    print(f"\n📊 Question breakdown by category:")
    categories = await db.questions.distinct("category")
    for cat in categories:
        count = await db.questions.count_documents({"category": cat})
        free_count = await db.questions.count_documents({"category": cat, "isFree": True})
        paid_count = await db.questions.count_documents({"category": cat, "isFree": False})
        print(f"   - {cat}: {count} total ({free_count} free, {paid_count} paid)")
    
    client.close()
    print("\n🎉 Additional questions seeded successfully!")

if __name__ == "__main__":
    asyncio.run(seed_additional_questions())
