ASCII_ART = """

 ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗     ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗
██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗    ██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝
██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝    ███████╗██║     ██████╔╝██║██████╔╝   ██║   
██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗    ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   
╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║    ███████║╚██████╗██║  ██║██║██║        ██║   
 ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   
                                                                                                           
 """

MOTD = "Cleaner Script by Najoe\nBuild Version: 2.1.0"

import os
import re
import requests
import logging
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Configure logging
logging.basicConfig(filename=os.path.expanduser('~/wordpress_malware_scan.log'), level=logging.INFO)
logging.info(ASCII_ART)
logging.info(MOTD)

# PDF Report Setup
pdf_path = os.path.expanduser('~/Quarantine_Report.pdf')
pdf = SimpleDocTemplate(pdf_path, pagesize=letter)
quarantine_report_data = [["File Name", "Location", "Symptom", "Timestamp"]]

# Quarantine Folder
quarantine_folder = os.path.expanduser('~/QuarantineFiles')

if not os.path.exists(quarantine_folder):
    os.makedirs(quarantine_folder)

# Extensive Malware Patterns
patterns = [ ... ]  # Keep the previous patterns here

compiled_patterns = [re.compile(pattern) for pattern in patterns]

def quarantine_file(filepath):
    # Move the file to the quarantine folder
    file_name = os.path.basename(filepath)
    shutil.move(filepath, os.path.join(quarantine_folder, file_name))

def scan_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            data = f.read()
            for pattern in compiled_patterns:
                for match in pattern.findall(data):
                    logging.warning(f"Found suspicious pattern '{match}' in file {filepath}")
                    quarantine_report_data.append([os.path.basename(filepath), filepath, match, str(os.path.getctime(filepath))])
                    quarantine_file(filepath)
    except Exception as e:
        logging.error(f"Error scanning file {filepath}: {e}")

# Scan Function eloped
# Malware Patterns to look for (Add more weird patterns, unusual enumerators, etc.)
patterns = [
    r'base64_decode\(',
    r'eval\(',
    r'gzinflate\(',
    r'preg_replace\(.+\/e',
]

compiled_patterns = [re.compile(pattern) for pattern in patterns]

def scan_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()
        for pattern in compiled_patterns:
            for match in pattern.findall(data):
                logging.warning(f"Found suspicious pattern '{match}' in file {filepath}")

def scan_url(url):
    try:
        response = requests.get(url)
        for pattern in compiled_patterns:
            for match in pattern.findall(response.text):
                logging.warning(f"Found suspicious pattern '{match}' in URL {url}")
    except Exception as e:
        logging.error(f"Error scanning URL {url}: {e}")

# Scanning Files
# Replace '/path/to/wordpress' with the actual path to the WordPress installation
for root, dirs, files in os.walk('/path/to/wordpress'): 
    for file in files:
        if file.endswith('.php') or file.endswith('.js'):
            scan_file(os.path.join(root, file))

# Scanning URLs
# Replace 'list_of_urls' with the actual list of URLs you want to scan
list_of_urls = ['http://example.com', 'http://example.com/page']
for url in list_of_urls:
    scan_url(url)

logging.info("Scan completed.")


# Generate PDF Report for Quarantined Files
if len(quarantine_report_data) > 1:  # Check if there are quarantined files
    table = Table(quarantine_report_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    pdf.build([table])
