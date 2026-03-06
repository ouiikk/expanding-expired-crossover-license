import os
import plistlib
import subprocess
from datetime import datetime, timezone

plist_path = os.path.expanduser('~/Library/Preferences/com.codeweavers.CrossOver.plist')

def reset_crossover_date():
    try:
        if os.path.exists(plist_path):
            with open(plist_path, 'rb') as f:
                data = plistlib.load(f)
        else:
            print(f"File not found: {plist_path}")
            return

        data['FirstRunDate'] = datetime.now(timezone.utc)

        with open(plist_path, 'wb') as f:
            plistlib.dump(data, f)

        subprocess.run(['killall', 'cfprefsd'], check=False)
        
        print("Successfully updated CrossOver.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    reset_crossover_date()
