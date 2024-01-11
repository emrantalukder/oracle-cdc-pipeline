from faker import Faker
import oracledb
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Database connection parameters
username = 'sys'
password = 'oracle'
dsn = 'localhost:1521/ORCLCDB'

# Establish a connection
conn = oracledb.connect(user=username, password=password, dsn=dsn, mode=oracledb.SYSDBA)
cursor = conn.cursor()

# Generate and insert data into Customers table
for _ in range(100):  # Generate data for 100 customers
    customer_id = fake.random_int(min=1, max=100)
    first_name = fake.first_name()
    last_name = fake.last_name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()
    cursor.execute("INSERT INTO C##MYUSER.Customers (CustomerID, FirstName, LastName, DateOfBirth, Address, Phone, Email) VALUES (:1, :2, :3, :4, :5, :6, :7)",
                   (customer_id, first_name, last_name, dob, address, phone, email))

# Generate and insert data into Policies table
policy_types = ['Health', 'Auto', 'Life', 'Property']
for _ in range(100):
    customer_id = fake.random_int(min=1, max=100)
    policy_id = fake.random_int(min=1, max=100)
    policy_type = random.choice(policy_types)
    start_date = fake.date_between(start_date='-5y', end_date='today')
    end_date = start_date + timedelta(days=365 * random.randint(1, 5))  # Policy duration between 1 to 5 years
    premium = round(random.uniform(500, 5000), 2)
    cursor.execute("INSERT INTO C##MYUSER.Policies (PolicyID, CustomerID, PolicyType, StartDate, EndDate, Premium) VALUES (:1, :2, :3, :4, :5, :6)",
                   (policy_id, customer_id, policy_type, start_date, end_date, premium))

# Generate and insert data into Claims table
for _ in range(200):  # Generate data for 200 claims
    claim_id = fake.random_int(min=1, max=100)
    policy_id = fake.random_int(min=1, max=100)  # Assuming policy IDs are from 1 to 100
    date_of_claim = fake.date_between(start_date='-3y', end_date='today')
    amount = round(random.uniform(100, 10000), 2)
    status = random.choice(['Pending', 'Approved', 'Denied'])
    cursor.execute("INSERT INTO C##MYUSER.Claims (ClaimID, PolicyID, DateOfClaim, Amount, Status) VALUES (:1, :2, :3, :4, :5)",
                   (claim_id, policy_id, date_of_claim, amount, status))

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("Mock data generated successfully.")
