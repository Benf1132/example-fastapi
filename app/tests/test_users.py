import pytest
from jose import jwt
from app import schemas
from app.config import settings

# import pytest
# from app.calculations import test1, test2


# @pytest.fixture
# def test1():
#     return 

# @pytest.mark.parametrize("x, y, result", [
#     (3,2,5),
#     (7,1,8),
#     (12,4,16)
# ])

# def test_test1(x, y, result):
#     assert test1(x,y) == result

# def test_test2_error(x, y, result):
#     with pytest.raises(Exception):
#         assert test1(x,y) == result

# Run this with:
#           pytest -v -x -s --disable-warnings  app\tests\test_users.py
#           v(verbose): Expounds Passed/Failed
#           x: stops all tests when it reaches the first fail
#           s: show print statements

# def test_root(client):
#     res = client.get("/")
#     assert res.json().get('message') == 'Hello World'
#     assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email": "testuser2@gmail.com", "password": "password234", "phone_number": "0000000001"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == 'testuser2@gmail.com'
    # assert res.json().get('email') == 'testuser2@gmail.com'
    assert res.status_code == 201

def test_login_user(test_user, client):
    res = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ("wrongEmail@gmail.com", "password234", 403),
    ("testuser2@gmail.com", "wrongPassword", 403),
    ("wrongEmail@gmail.com", "wrongPassword", 403),
    (None, "password234", 403), # 422
    ("testuser2@gmail.com", None, 403) # 422   
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
 
    assert res.status_code == status_code
    # assert res.json().get('detail') == "Invalid Credentials"