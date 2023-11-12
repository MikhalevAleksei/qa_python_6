from dataclasses import dataclass


class Urls:
    # Главная страница
    url_main = 'https://qa-scooter.praktikum-services.ru/'


@dataclass
class Answers:
    one: str = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    two: str = "Пока что у нас так: один заказ — один самокат. \Если хотите " \
               "покататься с друзьями, можете просто сделать несколько " \
               "\заказов — один за другим."

    three: str = "Допустим, вы оформляете заказ на 8 мая. \Мы привозим " \
                 "самокат 8 мая в течение дня. \Отсчёт времени аренды " \
                 "начинается с момента, когда вы оплатите заказ курьеру. " \
                 "\Если мы привезли самокат 8 мая в 20:30, суточная аренда " \
                 "\закончится 9 мая в 20:30."

    four: str = "Только начиная с завтрашнего дня. \Но скоро станем " \
                "расторопнее."

    five: str = "Пока что нет! Но если что-то срочное — всегда можно " \
                "позвонить \в поддержку по красивому номеру 1010."

    six: str = "Самокат приезжает к вам с полной зарядкой. Этого хватает на " \
               "\восемь суток — даже если будете кататься без передышек и " \
               "\во сне. Зарядка не понадобится."

    seven: str = "Да, пока самокат не привезли. Штрафа не будет, " \
                 "\объяснительной записки тоже не попросим. Все же свои."

    eight: str = "Да, обязательно. Всем самокатов! \И Москве, и Московской " \
                 "области."


@dataclass()
class Person:
    name: str
    lastname: str
    adress: str
    metro: str
    phone: str
