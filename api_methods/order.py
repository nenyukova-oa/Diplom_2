import requests
import allure
from url import URL

class OrderMethods:

    @staticmethod
    @allure.step("Формирование тела запроса для создания заказа")
    def get_order_payload(ingredients=None):
        
        if ingredients is None:
            return {"ingredients": []} 
        return {"ingredients": ingredients}

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload, headers=None):

        return requests.post(URL.ORDER_ENDPOINT, json=payload, headers=headers)

    @staticmethod
    @allure.step("Получение списка заказов конкретного пользователя")
    def get_user_orders(headers=None):
        
        return requests.get(URL.ORDER_ENDPOINT, headers=headers)