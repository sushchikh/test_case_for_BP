from .locators import YandexLocators
from .base_page import BasePage

animals_wiki = {}

class AnimalSearch(BasePage):
    def get_first_output_ya_search_engine(self, animal):
        input_form = self.browser.find_element(*YandexLocators.YANDEX_SEARCH_FIELD)
        input_form.send_keys(animal)
        submit_btn = self.browser.find_element(*YandexLocators.SUBMIT_BTN)
        submit_btn.click()
        get_search_engine_output = self.browser.find_element(*YandexLocators.SEARCH_ENGINE_OUTPUT)
        animals_wiki[animal] = get_search_engine_output.get_attribute("href")

class ShowAnimalWiki():
    """
    Вывод словаря в отдельный класс реализован для возможности в будущем обрататывать словарь не принтом, а например
    пушить в базу данных, или еще что-нибудь в таком духе
    """
    def print_animals_wiki(self):
        print()
        for animal_key, animal_value in animals_wiki.items():
            print(f"Зверь: {animal_key}, ссылка: {animal_value} ")
