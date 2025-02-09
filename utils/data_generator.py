from faker import Faker

fake = Faker()

def generate_user_data():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password()
    }
