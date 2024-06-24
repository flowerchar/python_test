import allure
import requests
from python_requests.utils.log_util import logger
import jsonpath
@allure.feature("宠物商店管理")
class TestPetstore:

    def setup_class(self):
        self.base_url = 'https://petsore.swagger.io/v2/pet'
        self.search_url = self.base_url + '/findByStatus'
        self.pet_id = 9223372000001084222
        self.delete_url = self.base_url + f'/{self.pet_id}'
        self.pet_status = 'available'
        self.add_pet_info = {
            "id": self.pet_id,
            "category": {
                "id": 1,
                "name": "cat"
            },
            "name": "miao",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 5,
                    "name": "cute"
                }
            ],
            "status": self.pet_status
        }
        self.update_name = "miao-hogwarts"
        self.update_pet_info = {
            "id": self.pet_id,
            "category": {
                "id": 1,
                "name": "cat"
            },
            "name": self.update_name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 5,
                    "name": "cute"
                }
            ],
            "status": self.pet_status
        }
        self.search_param = {
            "status": self.pet_status
        }
        self.proxy = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888"
        }

    @allure.story("宠物商店管理接口测试")
    def test_pet_manager(self):
        with allure.step("添加宠物"):
            add_r = requests.post(self.base_url, json=self.add_pet_info, proxies=self.proxy, verify=False)
            logger.info(f"add pet response: {add_r.text}")
            assert add_r.status_code == 200
        with allure.step("查询宠物"):
            search_r = requests.get(self.search_url, params=self.search_param, proxies=self.proxy, verify=False)
            logger.info(f"search pet response: {search_r.text}")
            assert search_r.status_code == 200
            assert self.pet_id in jsonpath.jsonpath(search_r.json(), "$..id")
        with allure.step("更新宠物"):
            update_r = requests.put(self.base_url, json=self.update_pet_info, proxies=self.proxy, verify=False)
            logger.info(f"update pet response: {update_r.text}")
            assert update_r.status_code == 200
            assert self.update_name in jsonpath.jsonpath(search_r.json(), "$..name")
        with allure.step("删除宠物"):
            delete_r = requests.delete(self.delete_url, proxies=self.proxy, verify=False)
            logger.info(f"delete pet response: {delete_r.text}")
            assert delete_r.status_code == 200
            assert self.pet_id not in jsonpath.jsonpath(delete_r.json(), "$..id")

