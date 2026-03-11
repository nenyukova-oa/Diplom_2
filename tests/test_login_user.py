import pytest
import allure

from api_methods.login_user import UserLogin
from api_methods.create_user import UserReg
from data import TestData

class TestUserLogin:


    @allure.title("Успешная авторизация под существующим пользователем")
    def test_login_user_success(self, user_data):        
        UserReg.register_new_user(user_data)
        
        login_payload = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        
        response = UserLogin.login_user(login_payload)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    
    @pytest.mark.parametrize("wrong_field", ["email", "password"])
    def test_login_user_with_wrong_credentials_error(self, user_data, wrong_field):
        allure.dynamic.title(f"Код ответа 401, сообщение '{TestData.text_login_error}' в теле ответа при неверном пароле или email")
        
        UserReg.register_new_user(user_data)
        
        login_payload = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        login_payload[wrong_field] = "wrong_" + login_payload[wrong_field]
        
        response = UserLogin.login_user(login_payload)
        
        assert response.status_code == 401
        assert response.json()["message"] == TestData.text_login_error

   