import requests
import allure

from url import URL

class UserReg:

    @staticmethod
    @allure.step("Регистрация пользователя")
    def register_new_user(payload):
        return requests.post(URL.CR_USER_ENDPOINT, data=payload)

