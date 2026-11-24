import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DASHBOARD_DIR = os.path.join(BASE_DIR, 'dashboard')
output_path = os.path.join(DASHBOARD_DIR, 'index.html')

print("Starting generation of zero-emoji clean dashboard UI...")
