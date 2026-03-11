import allure
from data import TestData

from api_methods.order import OrderMethods

class TestOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_auth_success(self, auth_token, ingredients_payload):
        
        headers = {"Authorization": auth_token}
        response = OrderMethods.create_order(ingredients_payload, headers=headers)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauth_success(self, ingredients_payload):
        
        response = OrderMethods.create_order(ingredients_payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    
    def test_create_order_no_ingredients_error(self, auth_token):
        allure.dynamic.title(f"Код ответа 400, сообщение '{TestData.text_order_no_ingredients}' в теле ответа при заказе без ингридиентов")
        headers = {"Authorization": auth_token}        
        payload = {"ingredients": []}
        response = OrderMethods.create_order(payload, headers=headers)

        assert response.status_code == 400
        assert response.json()["message"] == TestData.text_order_no_ingredients

    
    def test_create_order_invalid_hash_error(self):
        allure.dynamic.title(f"Код ответа 500, сообщение '{TestData.text_invalid_hash}' в теле ответа при заказе с неверным хешем ингредиента")
        
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d_INVALID"]}
        response = OrderMethods.create_order(payload)
        
        assert response.status_code == 500        

    @allure.title("Получение заказов конкретного авторизованного пользователя")
    def test_get_user_orders_auth_success(self, auth_token):
        headers = {"Authorization": auth_token}
        response = OrderMethods.get_user_orders(headers=headers)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "orders" in response.json()

    
    def test_get_user_orders_unauth_error(self):
        allure.dynamic.title(f"Код ответа 401, сообщение '{TestData.text_order_no_auth}' в теле ответа при заказе без ингридиентов")
        
        response = OrderMethods.get_user_orders()

        assert response.status_code == 401
        assert response.json()["message"] == TestData.text_order_no_auth
