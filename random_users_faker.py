import csv
from faker import Faker

fake = Faker()

# Generate example data
num_rows = 30
data = []
for i in range(num_rows):
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    address = fake.address()
    phone = fake.phone_number()
    data.append([username, email, password, address, phone])

# Write data to CSV file
filename = 'example_data3.csv'
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Username', 'Email', 'Password', 'Address', 'Phone Number'])
    for row in data:
        writer.writerow(row)
print(f"Example data written to {filename}.")