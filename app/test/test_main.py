from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fibonacci_1(): # n=1のとき
    response = client.get("/fib?n=1")
    assert response.status_code == 200
    assert response.json() == {"result": 1}

def test_fibonacci_99(): # n=99のとき
    response = client.get("/fib?n=99")
    assert response.status_code == 200
    assert response.json() == {"result": 218922995834555169026}

def test_zero(): # nが0のとき
    response = client.get("/fib?n=0")
    assert response.status_code == 422

def test_negative(): # nが負の数のとき
    response = client.get("/fib?n=-1")
    assert response.status_code == 422

def test_decimal(): # nが小数のとき
    response = client.get("/fib?n=3.5")
    assert response.status_code == 422

def test_string(): # nが文字列のとき
    response = client.get("/fib?n=abc")
    assert response.status_code == 422

def test_empty(): # nが指定されていないとき
    response = client.get("/fib?n=")
    assert response.status_code == 422