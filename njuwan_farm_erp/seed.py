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

        # 1. Your Specific Milking Herd
        milking_cows = [
            {'name': 'June', 'breed': 'Holstein', 'status': 'Lactating'},
            {'name': 'Njata', 'breed': 'Jersey', 'status': 'Lactating'},
            {'name': 'Mariru', 'breed': 'Ayrshire', 'status': 'Lactating'},
            {'name': 'Mahua', 'breed': 'Friesian', 'status': 'Lactating'},
            {'name': 'Turi', 'breed': 'Sahiwal', 'status': 'Lactating'},
            {'name': 'Madam', 'breed': 'Holstein', 'status': 'Lactating'}
        ]

        # 2. Add Milking Cows with specific production data
        for i, data in enumerate(milking_cows):
            tag = f"M{i+1:02d}"
            cow = Cow(tag_number=tag, name=data['name'], breed=data['breed'], status=data['status'])
            db.session.add(cow)
            db.session.flush()

            # Add 7 days of milk records (higher yields for milking cows)
            for d in range(7):
                db.session.add(MilkProduction(
                    cow_id=cow.id, 
                    litres=round(random.uniform(20.0, 35.0), 2), 
                    date=datetime.now() - timedelta(days=d)
                ))

        # 3. Add 4 Almost Calving Heifers (High Valuation)
        for i in range(1, 5):
            cow = Cow(tag_number=f"H{i:02d}", name=f"Heifer_{i}", breed='Friesian', status='Pregnant')
            db.session.add(cow)
            db.session.flush()
            # Add breeding record to show "Almost Calving"
            db.session.add(Breeding(
                cow_id=cow.id,
                insemination_date=datetime.now() - timedelta(days=250), # 9 months ago
                bull="Elite_Bull_X",
                expected_calving=datetime.now() + timedelta(days=random.randint(10, 30))
            ))

        # 4. Add 6 Young Calves
        for i in range(1, 7):
            db.session.add(Cow(tag_number=f"C{i:02d}", name=f"Calf_{i}", breed='Jersey', status='Young'))

        db.session.commit()
        print(f"Success! Seeded 16 animals: {len(milking_cows)} milking, 4 heifers, 6 calves.")
        
if __name__ == "__main__":
    seed_database()