# python seed.py
# flask --app app run --debug

import random
from datetime import datetime, timedelta
from app import app, db
from models import MilkProduction, Transaction, Cow, Vaccination, Breeding, Crop, Feed, HealthRecord

def seed_database():
    with app.app_context():
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()

        breeds = ['Holstein', 'Jersey', 'Guernsey', 'Ayrshire', 'Sahiwal']
        statuses = ['Lactating', 'Dry', 'Quarantined', 'Sick']
        diseases = ['Mastitis', 'Foot Rot', 'Milk Fever', 'Bloat']
        feed_types = ['Silage', 'Dairy Meal', 'Napier Grass', 'Hay']

        print("Adding 30 cows and records...")
        
        for i in range(1, 31):
            # 1. Create Cow
            tag = f"{i:03d}"
            cow = Cow(
                tag_number=tag,
                name=f"Cow_{tag}",
                breed=random.choice(breeds),
                status=random.choice(statuses)
            )
            db.session.add(cow)
            db.session.flush() # Get cow.id for relationships

            # 2. Add Milk Records (Last 7 days)
            for d in range(7):
                date_point = datetime.now() - timedelta(days=d)
                # Randomize production between 15L and 35L
                milk = MilkProduction(
                    cow_id=cow.id,
                    litres=round(random.uniform(15.0, 35.0), 2),
                    date=date_point
                )
                db.session.add(milk)

            # 3. Add Feed Records (Last 7 days)
            for d in range(7):
                date_point = datetime.now() - timedelta(days=d)
                feed = Feed(
                    cow_id=cow.id,
                    f_type=random.choice(feed_types),
                    qty=round(random.uniform(5.0, 15.0), 1),
                    date=date_point
                )
                db.session.add(feed)

            # 4. Randomly add Health/Breeding records to trigger "Wellness Overview"
            if i % 5 == 0:
                health = HealthRecord(
                    cow_id=cow.id,
                    disease=random.choice(diseases),
                    treatment="Antibiotics and rest",
                    vet_name="Dr. Kariuki",
                    date=datetime.now() - timedelta(days=random.randint(1, 10))
                )
                db.session.add(health)

            if i % 7 == 0:
                breeding = Breeding(
                    cow_id=cow.id,
                    insemination_date=datetime.now() - timedelta(days=random.randint(30, 100)),
                    bull="Elite_Bull_X",
                    expected_calving=datetime.now() + timedelta(days=random.randint(100, 250))
                )
                db.session.add(breeding)

            if i % 10 == 0:
                vac = Vaccination(
                    cow_id=cow.id,
                    vaccine="Foot and Mouth",
                    due_date=datetime.now() + timedelta(days=random.randint(5, 20)),
                    status="Pending"
                )
                db.session.add(vac)

        db.session.commit()
        print("Success! 30 cows with milk, feed, and health records added.")

if __name__ == "__main__":
    seed_database()