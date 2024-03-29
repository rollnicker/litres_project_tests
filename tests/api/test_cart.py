import allure
from allure_commons._allure import step
from jsonschema import validate

from litres_project.utils.logging import request_litres
from litres_project.utils.open_schemas import load_schema
from tests.api.conftest import BASE_URL, ADD_TO_CART_URL, CART_URL


@allure.epic('Cart')
@allure.tag('api', 'positive')
@allure.title("Проверка добавления в корзину")
def test_add_to_cart():
    response = request_litres(base_url=BASE_URL,
                              method='PUT',
                              url=ADD_TO_CART_URL,
                              headers={"Content-Type": "application/json"},
                              json={"art_ids": [70400188]})
    body = response.json()
    validate(body,
             schema=load_schema("add_to_cart_schema.json"))
    assert response.status_code == 200


@allure.epic('Cart')
@allure.tag('api', 'positive')
@allure.title("Проверка открытия корзины")
def test_check_cart_schema():
    response = request_litres(base_url=BASE_URL,
                              method='GET',
                              url=CART_URL,
                              headers={"Content-Type": "application/json"}
                              )
    body = response.json()
    validate(body,
             schema=load_schema("cart_status_schema.json"))
    assert response.status_code == 200
    assert response.json()['payload']['data']['count'] == 0


@allure.epic('Cart')
@allure.tag('api', 'positive')
@allure.title("Проверка добавления в корзину нескольких книг ")
def test_add_two_books_to_cart():
    with step("add to cart 1 book"):
        response = request_litres(base_url=BASE_URL,
                                  method='PUT',
                                  url=ADD_TO_CART_URL,
                                  headers={"Content-Type": "application/json"},
                                  json={"art_ids": [70400188]})
        cookie = response.cookies
    with step("add to cart other book"):
        response2 = request_litres(base_url=BASE_URL,
                                   method='PUT',
                                   url=ADD_TO_CART_URL,
                                   headers={"Content-Type": "application/json"},
                                   json={"art_ids": [63353991]},
                                   cookies=cookie)
    with step("check 2 books were added to cart"):
        assert response2.status_code == 200
        assert response2.json()['payload']['data']['added_art_ids'] == [70400188, 63353991]


@allure.epic('Cart')
@allure.tag('api', 'positive')
@allure.title("Проверка отображения в корзине добавленной книги")
def test_check_book_in_cart():
    with step("add to cart 1 book"):
        cookie = request_litres(base_url=BASE_URL, method='PUT',
                                url=ADD_TO_CART_URL,
                                headers={"Content-Type": "application/json"},
                                json={"art_ids": [70400188]}).cookies
    with step("open cart and check added book"):
        response = request_litres(base_url=BASE_URL,
                                  method='GET',
                                  url=CART_URL,
                                  headers={"Content-Type": "application/json"},
                                  cookies=cookie
                                  )
        assert response.status_code == 200
        assert response.json()['payload']['data']['arts_in_cart'] == [70400188]
