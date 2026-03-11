class URL:
    BASE_URL = "https://stellarburgers.education-services.ru" # ссылка на сайт
    CR_USER_ENDPOINT = f"{BASE_URL}/api/auth/register" # создание пользователя
    LOG_USER_ENDPOINT = f"{BASE_URL}/api/auth/login" # логин пользователя
    ORDER_ENDPOINT = f"{BASE_URL}/api/orders" # создание заказа
    DELETE_USER = f"{BASE_URL}/api/auth/user" # эндпоинт для удаления пользователя