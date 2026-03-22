import random
from datetime import datetime, date, timedelta
from app import app, db
from models import MilkProduction, Cow, Breeding

def seed_database():
    with app.app_context():
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()

        # 1. Detailed Herd Configuration
        # Production is tuple: (Morning, Lunch, Evening)
        herd_data = [
            {'name': 'Njata', 'status': 'Lactating', 'prod': (6, 4, 2), 'breed': 'Jersey'},
            {'name': 'June', 'status': 'Pregnant', 'prod': (5, 0, 6), 'insem': date(2025, 8, 17)},
            {'name': 'Mariru', 'status': 'Pregnant', 'prod': (5, 3, 2), 'insem': date(2026, 3, 5)},
            {'name': 'Madam', 'status': 'Pregnant', 'prod': (8, 6, 3), 'insem': date(2025, 12, 31)},
            {'name': 'Jupiter', 'status': 'Lactating', 'prod': (7, 5, 3), 'breed': 'Holstein'},
            {'name': 'Mahua', 'status': 'Pregnant', 'prod': (0, 0, 0), 'insem': date(2025, 6, 26)}
        ]

        # 2. Add the Main Herd & Milk Sessions
        for data in herd_data:
            cow = Cow(
                tag_number=f"M-{data['name'][:3].upper()}", 
                name=data['name'], 
                status=data['status'],
                breed=data.get('breed', 'Friesian')
            )
            db.session.add(cow)
            db.session.flush()

            # Add Breeding record if insemination date exists
            if 'insem' in data:
                db.session.add(Breeding(
                    cow_id=cow.id,
                    insemination_date=data['insem'],
                    bull="Elite_Semen_001",
                    # Gestation is roughly 283 days
                    expected_calving=data['insem'] + timedelta(days=283)
                ))

            # Add specific Milk Production Sessions
            sessions = ['Morning', 'Lunch', 'Evening']
            for i, litres in enumerate(data['prod']):
                if litres > 0:
                    db.session.add(MilkProduction(
                        cow_id=cow.id,
                        litres=litres,
                        session=sessions[i],
                        date=datetime.now()
                    ))

        # 3. Add Young Stock (Heifers and Calves)
        # 4 Young Heifers
        for i in range(1, 5):
            db.session.add(Cow(tag_number=f"H0{i}", name=f"Heifer_{i}", status="Young", breed="Friesian"))

        # 2 Young Female Calves & 2 Young Male Calves
        for i in range(1, 3):
            db.session.add(Cow(tag_number=f"CF0{i}", name=f"F_Calf_{i}", status="Young", breed="Jersey"))
            db.session.add(Cow(tag_number=f"CM0{i}", name=f"M_Calf_{i}", status="Young", breed="Ayrshire"))

        # 2 Lactating Calves (Young animals currently being weaned/monitored)
        for i in range(1, 3):
            db.session.add(Cow(tag_number=f"LC0{i}", name=f"L_Calf_{i}", status="Lactating", breed="Holstein"))

        db.session.commit()
        print("Success! Njuwan Farm ERP seeded with specific production and breeding data.")

if __name__ == "__main__":
    seed_database()