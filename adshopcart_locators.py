from faker import Faker

fake = Faker(locale='en_CA')
advantageshopping_url = 'https://www.advantageonlineshopping.com/#/'
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
