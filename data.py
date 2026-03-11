class TestData:
    text_create_missing_field = "Email, password and name are required fields"
    text_create_duplicate = "User already exists"
    text_login_error = "email or password are incorrect"

    VALID_INGREDIENTS = [
        "61c0c5a71d1f82001bdaaa6d", # id флюоресцентной булки R2-D3
        "61c0c5a71d1f82001bdaaa72", # id соуса Spicy-X
        "61c0c5a71d1f82001bdaaa70"  # id говяжьего метеорита (отбивной)
    ]
    
    text_order_no_ingredients = "Ingredient ids must be provided"
    text_order_no_auth = "You should be authorised"
    text_invalid_hash = "Internal server error"
