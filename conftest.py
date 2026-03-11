import pytest
import requests
from url import URL
from generator import *
from api_methods.create_user import UserReg
from api_methods.login_user import UserLogin
from data import TestData

# Генерация данных и удаление пользователя после теста
@pytest.fixture
def user_data():
    
    payload = {
        "email": generate_random_email(),
        "password": generate_random_string(10),
        "name": generate_random_string(10)
    }

    yield payload
    
    login_response = UserLogin.login_user(payload)
    if login_response.status_code == 200:
        token = login_response.json().get('accessToken')        
        requests.delete(URL.DELETE_USER, headers={"Authorization": token})

# Фикстура для получения токена авторизованного пользователя
@pytest.fixture
def auth_token(user_data):    
    UserReg.register_new_user(user_data)   
    response = UserLogin.login_user(user_data)
    token = response.json().get('accessToken')
    return token

# Фикстура с набором валидных ингредиентов
@pytest.fixture
def ingredients_payload():    
    return {"ingredients": TestData.VALID_INGREDIENTS}
    
    

