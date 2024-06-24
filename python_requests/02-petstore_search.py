import allure
import requests
import pytest
from python_requests.utils.log_util import logger

@allure.feature('宠物搜索商店')
class TestPetStoreSearch:

    def setup_class(self):
        self.base_url = 'https://petstore.swagger.io/v2/pet'
        self.search_url = self.base_url + '/findByStatus'

    # def test_search_pet(self):
    #     pet_store = {
    #         "status": "available"
    #     }
    #     r = requests.get(self.search_url, params=pet_store)
    #     logger.info(r.text)
    #     print(r.json()[0])
    #     assert r.status_code == 200
    #     assert r.json() != []
    #     assert 'id' in r.json()[0]

    @allure.story("宠物搜索接口冒烟用例")
    @pytest.mark.parametrize('status', ['available', 'pending', 'sold'],
                             ids=['available1', 'pending2', 'sold3'])
    def test_search_pet_params(self, status):
        pet_store = {
            "status": status
        }
        r = requests.get(self.search_url, params=pet_store)
        logger.info(r.text)
        print(r.json()[0])
        assert r.status_code == 200
        assert r.json() != []
        assert 'id' in r.json()[0]

    @allure.story("宠物搜索接口异常用例")
    @pytest.mark.parametrize('status', ['111', '', 'abc'],ids=['1111', '2222', '3333'])
    def test_search_pet_params_failure(self, status):
        pet_store = {
            "status": status
        }
        r = requests.get(self.search_url, params=pet_store)
        logger.info(r.text)
        assert r.status_code == 200
        assert r.json() == []

    @allure.story("宠物搜索接口不传参数异常用例")
    def test_search_none_params(self):
        r = requests.get(self.search_url)
        logger.info(r.text)
        assert r.status_code == 200
        assert r.json() == []

    @allure.story("宠物搜索接口传入错误参数异常用例")
    def test_search_wrong_param(self):
        pet_store = {
            "key": "available"
        }
        r = requests.get(self.search_url, params=pet_store)
        logger.info(r.text)
        assert r.status_code == 200
        assert r.json() == []