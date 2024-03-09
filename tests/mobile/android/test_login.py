import os

from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_login(android_mobile_management):
    with step('закрыть выбор языка'):
        if browser.element((AppiumBy.ID, 'ru.litres.android:id/dialog_close_btn')).should(be.existing):
            browser.element((AppiumBy.ID, 'ru.litres.android:id/dialog_close_btn')).click()
        else:
            pass
    with step('закрыть всплывающее окно выбора эротики'):
        if browser.element((AppiumBy.ID, 'ru.litres.android:id/btnEnableAdultContent')).should(be.existing):
            browser.element((AppiumBy.ID, 'ru.litres.android:id/btnEnableAdultContent')).click()
        else:
            pass
    with step('закрыть крестик'):
        if browser.element((AppiumBy.ID, 'ru.litres.android:id/circleButtonSubscriptionPaywallClose')).should(be.existing):
            browser.element((AppiumBy.ID, 'ru.litres.android:id/circleButtonSubscriptionPaywallClose')).click()
        else:
            pass
    with step('Перейти в раздел профиль'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/ll_profile_menu_item')).click()
    with step('Нажать кнопку login'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/login_button')).click()
    with step('Ввести mail'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/loginEditText')).type(f'{os.getenv("USER_LOGIN")}')
        browser.element((AppiumBy.ID, 'ru.litres.android:id/continueButton')).click()
    with step('Ввести пароль'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/passwordEditText')).type(f'{os.getenv("USER_PASSWORD")}')
        browser.element((AppiumBy.ID, 'ru.litres.android:id/continueButton')).click()
    with step('Проверить успешный логин'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/user_login')).should(have.text(f'{os.getenv("USER_LOGIN")}'))
