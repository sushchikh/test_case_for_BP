from selenium.webdriver.common.by import By


class YandexLocators():
    YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, "input.input__input")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button.button")
    SEARCH_ENGINE_OUTPUT = (By.CSS_SELECTOR, "div.content__left li a")
