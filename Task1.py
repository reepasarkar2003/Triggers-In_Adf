

# Task 1: Fetching and Processing Files


import os
import pandas as pd
import re
from datetime import datetime

# Create directories if they do not exist
os.makedirs('processed/CUST_MSTR', exist_ok=True)
os.makedirs('processed/master_child_export', exist_ok=True)
os.makedirs('processed/H_ECOM_ORDER', exist_ok=True)

# Function to extract date from filename
def extract_date_from_filename(filename, date_format='%Y%m%d'):
    date_match = re.search(r'(\d{8})', filename)
    if date_match:
        return datetime.strptime(date_match.group(1), date_format).strftime('%Y-%m-%d'), date_match.group(1)
    return None, None

# Process CUST_MSTR files
def process_cust_mstr(file_paths):
    for path in file_paths:
        df = pd.read_csv(path)
        date, _ = extract_date_from_filename(path)
        df['date'] = date
        output_path = f'processed/CUST_MSTR/{os.path.basename(path)}'
        df.to_csv(output_path, index=False)
        print(f'Processed and saved: {output_path}')

# Process master_child_export files
def process_master_child_export(file_paths):
    for path in file_paths:
        df = pd.read_csv(path)
        date, date_key = extract_date_from_filename(path)
        df['date'] = date
        df['date_key'] = date_key
        output_path = f'processed/master_child_export/{os.path.basename(path)}'
        df.to_csv(output_path, index=False)
        print(f'Processed and saved: {output_path}')

# Process H_ECOM_ORDER files
def process_h_ecom_order(file_paths):
    for path in file_paths:
        df = pd.read_csv(path)
        output_path = f'processed/H_ECOM_ORDER/{os.path.basename(path)}'
        df.to_csv(output_path, index=False)
        print(f'Processed and saved: {output_path}')

# Example file paths (these would be paths in your data lake in a real scenario)
cust_mstr_files = ['CUST_MSTR_20191112.csv', 'CUST_MSTR_20191113.csv']
master_child_files = ['master_child_export-20191112.csv', 'master_child_export-20191113.csv']
h_ecom_order_files = ['H_ECOM_ORDER.csv']

# Process all files
process_cust_mstr(cust_mstr_files)
process_master_child_export(master_child_files)
process_h_ecom_order(h_ecom_order_files)

