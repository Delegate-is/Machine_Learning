from app import app, db, Cow, Feed, HealthRecord, Vaccination, Breeding
from datetime import datetime, timedelta

def seed_data():
    with app.app_context():
        # Optional: Clear data to start fresh and avoid "Unique Constraint" errors on Tag Numbers
        db.drop_all() 
        db.create_all()

        print("Seeding cows...")
        cow1 = Cow(tag_number="001", name="Mariru", status="Lactating", breed="Holstein", weight_kg=550.0)
        cow2 = Cow(tag_number="002", name="Doe", status="Dry", breed="Jersey", weight_kg=450.0)
        cow3 = Cow(tag_number="003", name="Bossy", status="Quarantined", breed="Guernsey", weight_kg=500.0)
        
        db.session.add_all([cow1, cow2, cow3])
        db.session.flush() # Flush to get IDs for the linked records

        print("Seeding Health & Medical records...")
        h1 = HealthRecord(cow_id=cow1.id, disease="Mastitis", treatment="Antibiotics", vet_name="Dr. Kamau", date=datetime.utcnow().date())
        h2 = HealthRecord(cow_id=cow3.id, disease="Foot Rot", treatment="Cleaning & Zinc", vet_name="Dr. Njoroge", date=datetime.utcnow().date())

        print("Seeding Vaccination schedule...")
        v1 = Vaccination(cow_id=cow1.id, vaccine="FMD", due_date=datetime.utcnow().date(), status="Completed")
        v2 = Vaccination(cow_id=cow2.id, vaccine="Anthrax", due_date=(datetime.utcnow() + timedelta(days=30)).date(), status="Pending")

        print("Seeding Breeding & Calving data...")
        # Testing the 283-day calculation logic
        ins_date = datetime.utcnow().date() - timedelta(days=60)
        exp_date = ins_date + timedelta(days=283)
        
        b1 = Breeding(
            cow_id=cow1.id, 
            insemination_date=ins_date, 
            bull="Top-Sire-01", 
            pregnancy_status="Confirmed", 
            expected_calving=exp_date
        )

        print("Seeding feed records...")
        f1 = Feed(cow_id=cow1.id, f_type="Dairy Meal", qty=10.0, cost=500, date=datetime.utcnow())
        f2 = Feed(cow_id=cow2.id, f_type="Silage", qty=15.0, cost=300, date=datetime.utcnow())
        
        db.session.add_all([h1, h2, v1, v2, b1, f1, f2])
        db.session.commit()
        
        print("Database seeded successfully with all relationships!")

if __name__ == "__main__":
    seed_data()