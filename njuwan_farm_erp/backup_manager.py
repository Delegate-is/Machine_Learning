import shutil
import os
from datetime import datetime

# Configuration
BASE_DIR = '/home/Juma/njuwan_farm_erp'
SOURCE_DB = os.path.join(BASE_DIR, 'farm.db')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')

def run_backup():
    # Create backup folder if it doesn't exist
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    
    # Generate filename with date (e.g., farm_backup_2026-03-09.db)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M')
    destination = os.path.join(BACKUP_DIR, f'farm_backup_{timestamp}.db')
    
    try:
        shutil.copy2(SOURCE_DB, destination)
        print(f"Backup successful: {destination}")
        
        # Keep only the last 7 backups to save space
        all_backups = sorted([os.path.join(BACKUP_DIR, f) for f in os.listdir(BACKUP_DIR)])
        while len(all_backups) > 7:
            os.remove(all_backups.pop(0))
            
    except Exception as e:
        print(f"Backup failed: {str(e)}")

if __name__ == "__main__":
    run_backup()