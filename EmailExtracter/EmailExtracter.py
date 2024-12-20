import os
import csv
import re

def extract_unique_emails(folder_path, output_file):
    unique_emails = set()  # Set to store unique email IDs

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):  # Check if the file is a CSV file
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', newline='') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    email = row.get('Email ID')
                    if email:
                        unique_emails.add(email.strip())

    # Write unique emails to a new CSV file
    with open(output_file, 'w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(['email_id'])
        for email in unique_emails:
            csv_writer.writerow([email])

    print(f"Unique email IDs extracted and saved to {output_file}")

# Example usage:
folder_path = 'C:\\Users\\LENOVO\\Downloads\\PSF_Mumbai'
output_file = 'unique_emails.csv'
extract_unique_emails(folder_path, output_file)


def validate_email(email):
    # Regular expression pattern for basic email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def clean_emails(input_file, output_file):
    cleaned_emails = set()
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            email = row[0]
            if validate_email(email):
                cleaned_emails.add(email)
            else:
                print(f"Invalid email found: {email}")

    # Write cleaned emails to a new CSV file
    with open(output_file, 'w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(['email_id'])
        for email in cleaned_emails:
            csv_writer.writerow([email])

    print(f"Data cleaning completed. Cleaned emails saved to {output_file}")

# Example usage:
input_file = 'unique_emails.csv'
output_file = 'cleaned_emails.csv'
clean_emails(input_file, output_file)

def create_email_chunks(input_file, output_folder, chunk_size=300):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        chunk_number = 1
        chunk_emails = []

        for row in csv_reader:
            email = row[0].strip()  # Trim spaces from email address
            chunk_emails.append(email)

            if len(chunk_emails) == chunk_size:
                write_chunk_to_file(chunk_emails, output_folder, chunk_number)
                chunk_number += 1
                chunk_emails = []

        # Write the last chunk if it's not a full chunk
        if chunk_emails:
            write_chunk_to_file(chunk_emails, output_folder, chunk_number)

    print(f"Email chunks created and saved to {output_folder}")

def write_chunk_to_file(chunk_emails, output_folder, chunk_number):
    output_file = os.path.join(output_folder, f"email_chunk_{chunk_number}.csv")
    with open(output_file, 'w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(['email_id'])
        for email in chunk_emails:
            csv_writer.writerow([email])

# Example usage:
input_file = 'cleaned_emails.csv'
output_folder = 'email_chunks'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
create_email_chunks(input_file, output_folder)