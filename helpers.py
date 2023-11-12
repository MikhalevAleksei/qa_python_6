from faker import Faker

from data import Person

faker_ru = Faker('ru_Ru')
Faker.seed()

def generated_person():
    yield Person(
        name = faker_ru.first_name(),
        lastname = faker_ru.last_name(),
        adress = faker_ru.adress(),
        phone = faker_ru.phone_number()
    )