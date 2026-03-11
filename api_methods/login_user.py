import requests
import allure
from url import URL

class UserLogin:

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(payload):        
        return requests.post(URL.LOG_USER_ENDPOINT, json=payload)

    @classmethod
    @allure.step("Получение accessToken пользователя")
    def get_access_token(cls, payload):        
        response = cls.login_user(payload)        
        
        if response.status_code == 200:            
            return response.json().get("accessToken")
        return None
