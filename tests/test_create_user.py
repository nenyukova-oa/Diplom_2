import pytest
import allure

from api_methods.create_user import UserReg
from generator import *
from data import TestData


class TestCreateUser:

    @allure.title("Успешное создание пользователя")
    def test_create_user_success(self, user_data):
        response = UserReg.register_new_user(user_data)     
                     
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()     

    
    def test_create_duplicate_user_fail(self, user_data):
        allure.dynamic.title(f"Код ответа 403, сообщение '{TestData.text_create_duplicate}' в теле ответа при регистрации существующего пользователя")
    
        UserReg.register_new_user(user_data)   
        response = UserReg.register_new_user(user_data)

        assert response.status_code == 403
        assert response.json()["message"] == TestData.text_create_duplicate


    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field_error(self, user_data, missing_field):
        allure.dynamic.title(f"Код ответа 403, сообщение '{TestData.text_create_missing_field}' в теле ответа при отсутствии поля {missing_field}")
        payload = user_data.copy()
        payload.pop(missing_field)

        response = UserReg.register_new_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == TestData.text_create_missing_field
        
