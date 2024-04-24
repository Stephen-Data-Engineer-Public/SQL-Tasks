import sqlite3
from faker import Faker

def create_fake_data():
    # Initialize Faker
    fake = Faker()

    # Connect to SQLite3 database
    conn = sqlite3.connect('fake_data.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS names (
                        id INTEGER PRIMARY KEY,
                        full_name TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        prefix TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS addresses (
                        id INTEGER PRIMARY KEY,
                        address TEXT,
                        city TEXT,
                        state TEXT,
                        country TEXT,
                        postcode TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS texts (
                        id INTEGER PRIMARY KEY,
                        random_text TEXT,
                        random_sentence TEXT,
                        random_paragraph TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS dates_and_times (
                        id INTEGER PRIMARY KEY,
                        random_date TEXT,
                        random_time TEXT,
                        random_date_time TEXT,
                        random_unix_time TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS internet_data (
                        id INTEGER PRIMARY KEY,
                        random_email TEXT,
                        random_domain_name TEXT,
                        random_url TEXT,
                        random_ipv4 TEXT
                    )''')

    # Insert fake data into tables
    for _ in range(10):  # Insert 10 fake records into each table
        # Names
        full_name = fake.name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        prefix = fake.prefix()

        cursor.execute("INSERT INTO names (full_name, first_name, last_name, prefix) VALUES (?, ?, ?, ?)",
                    (full_name, first_name, last_name, prefix))

        # Addresses
        address = fake.address()
        city = fake.city()
        state = fake.state()
        country = fake.country()
        postcode = fake.postcode()

        cursor.execute("INSERT INTO addresses (address, city, state, country, postcode) VALUES (?, ?, ?, ?, ?)",
                    (address, city, state, country, postcode))

        # Texts
        random_text = fake.text()
        random_sentence = fake.sentence()
        random_paragraph = fake.paragraph()

        cursor.execute("INSERT INTO texts (random_text, random_sentence, random_paragraph) VALUES (?, ?, ?)",
                    (random_text, random_sentence, random_paragraph))

        # Dates and Times
        random_date = fake.date()
        random_time = fake.time()
        random_date_time = fake.date_time()
        random_unix_time = fake.unix_time()

        cursor.execute("INSERT INTO dates_and_times (random_date, random_time, random_date_time, random_unix_time) VALUES (?, ?, ?, ?)",
                    (random_date, random_time, random_date_time, random_unix_time))

        # Internet Data
        random_email = fake.email()
        random_domain_name = fake.domain_name()
        random_url = fake.url()
        random_ipv4 = fake.ipv4()

        cursor.execute("INSERT INTO internet_data (random_email, random_domain_name, random_url, random_ipv4) VALUES (?, ?, ?, ?)",
                    (random_email, random_domain_name, random_url, random_ipv4))

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_fake_data()