import allure
from selene import browser, have


class FavouritePage:
    def __init__(self):
        self.favourite_books_list = browser.all('.ArtInfo-modules__title_1UysF')
        self.no_favourite_books_message = browser.element('.EmptyState-module__empty__content_2lpJ-')

    def check_first_liked_book_title(self, name):
        with allure.step(f'Проверить, что название "{name}" отображается в списке отложенных книг'):
            self.favourite_books_list[0].should(have.text(name))

    def check_no_favourite_books_message(self, text):
        with allure.step(f'Проверить, появилась текстовка "{text}" о пустом списке отложенных книг'):
            self.no_favourite_books_message.should(have.text(text))
