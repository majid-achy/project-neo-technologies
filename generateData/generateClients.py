import csv
import random
import datetime

def get_client_name():
    first_names = ["John", "Jane", "Michael", "Emily", "David", "Olivia"]
    last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown"]
    return random.choice(first_names) + " " + random.choice(last_names)

def get_client_email(name):
    return name.lower().replace(" ",".") + "@test.com"

def get_client_date_of_birth():
    start_date = datetime.datetime(1950, 1, 1, 00, 00, 00)
    end_date = datetime.datetime(2000, 1, 1, 00, 00, 00)
    random_date = random.random() * (end_date - start_date) + start_date
    return random_date.strftime("%Y-%m-%d")

def get_client_country():
    countries = ["United States", "Canada", "United Kingdom", "France", "Germany"]
    return random.choice(countries)


def get_account_balance():
    return round(random.uniform(0, 100000), 2)

def generate_client_data(num_clients):
    data = []
    for i in range(num_clients):
        client_id = i + 1
        name = get_client_name()
        email = get_client_email(name)
        date_of_birth = get_client_date_of_birth()
        country = get_client_country()
        account_balance = get_account_balance()
        data.append([client_id, name, email, date_of_birth, country, account_balance])
    return data

def write_csv_file(data, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["client_id", "name", "email", "date_of_birth", "country", "account_balance"])
        writer.writerows(data)


if __name__ == "__main__":
    number_of_clients = 1000 
    filename = "clients.csv"
    data = generate_client_data(number_of_clients)
    write_csv_file(data, filename)
    print(f"Generated {number_of_clients} clients. CSV file saved to: {filename}")