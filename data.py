import faker


def get_sign_up_data():
    faker = faker.Faker()
    email = fake.email()
    password = fake.password()
    return email, password