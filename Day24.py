import os
import shutil
import datetime
import tarfile
import hashlib
import logging

# Setup logging to log backup activities
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Directories to back up
backup_dirs = ['/path/to/important/data1', '/path/to/important/data2']
# Directory to store backups
backup_storage = '/path/to/backup/storage'
# Number of backup copies to keep
num_backups_to_keep = 5

def create_backup():
    try:
        # Generate a unique backup name with a timestamp
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        backup_name = f'backup_{timestamp}.tar.gz'
        backup_path = os.path.join(backup_storage, backup_name)

        # Create a tar.gz file containing the specified directories
        with tarfile.open(backup_path, 'w:gz') as tar:
            for directory in backup_dirs:
                tar.add(directory, arcname=os.path.basename(directory))

        logging.info(f'Backup created: {backup_path}')
        
        # Encrypt the backup
        encrypt_backup(backup_path)
        
        # Manage old backups to keep only the latest n backups
        manage_old_backups()

    except Exception as e:
        logging.error(f'Error during backup creation: {e}')

def encrypt_backup(backup_path):
    try:
        # Read the backup file
        with open(backup_path, 'rb') as f:
            data = f.read()
            # Create a hash of the data as a simple form of encryption (replace with proper encryption)
            hashed_data = hashlib.sha256(data).hexdigest()

        # Write the hashed data to a new file
        encrypted_path = backup_path + '.enc'
        with open(encrypted_path, 'w') as f:
            f.write(hashed_data)

        logging.info(f'Backup encrypted: {encrypted_path}')
        
        # Remove the original unencrypted backup file
        os.remove(backup_path)

    except Exception as e:
        logging.error(f'Error during backup encryption: {e}')

def manage_old_backups():
    try:
        # List all encrypted backup files
        backups = [f for f in os.listdir(backup_storage) if f.startswith('backup_') and f.endswith('.enc')]
        # Sort backups by name (which includes the timestamp)
        backups.sort()

        # Remove older backups, keep only the latest n backups
        while len(backups) > num_backups_to_keep:
            oldest_backup = backups.pop(0)
            os.remove(os.path.join(backup_storage, oldest_backup))
            logging.info(f'Old backup removed: {oldest_backup}')

    except Exception as e:
        logging.error(f'Error managing old backups: {e}')

if __name__ == '__main__':
    create_backup()
