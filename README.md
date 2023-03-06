# Use the faker Python Module to Create Random Data 

Import the Faker Module:
```python 
import csv
from faker import Faker
```
here we will also use CSV as we want to write to a CSV file. 

```python
fake = Faker()

# Generate example data
num_rows = 30 # ammend according to how much data you require in integers
data = []
for i in range(num_rows):
    username = fake.user_name() # fake username
    email = fake.email() # fake email 
    password = fake.password() # fake password 
    address = fake.address() # fake address 
    phone = fake.phone_number() # fake phone number
    data.append([username, email, password, address, phone]) # append the data

# Write data to CSV file
filename = 'example_data3.csv' # feel free to change CSV name
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Username', 'Email', 'Password', 'Address', 'Phone Number']) # add/remove as needed based on info on for loop above
    for row in data:
        writer.writerow(row)
print(f"Example data written to {filename}.")
```

The above code will just create some example data with 30 rows for you based on: username, email, password, address & phone number, simply modify as you need to. 

for more info see the documentation here:

[Faker Documentation](https://faker.readthedocs.io/en/master/index.html)

