import pytest
from .pages.yandex_search_page import AnimalSearch, ShowAnimalWiki



@pytest.mark.parametrize('animal', ['заяц',
                               'волк',
                               'лиса'
                               ])
def test_get_first_search_engine_output(browser, animal):
    link = 'https://ya.ru/'
    page = AnimalSearch(browser, link)
    page.open()
    page.get_first_output_ya_search_engine(animal)


def test_show_animal_wiki():
    aw = ShowAnimalWiki()
    aw.print_animals_wiki()





