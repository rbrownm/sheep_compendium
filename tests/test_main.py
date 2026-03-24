from fastapi.testclient import TestClient
from main import app
client = TestClient(app)


def test_read_sheep():

    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {
        "id":1,
        "name":"Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():

    sheep_data_name = {
        "id":7,
        "name":"Lemon",
        "breed":"Suffolk",
        "sex": "ewe"
    }

    response = client.post("/sheep", json=sheep_data_name)

    assert response.status_code == 201

    assert response.json() == sheep_data_name

    response_2 = client.get("/sheep/7")

    assert response_2.status_code == 200

    assert response_2.json() == sheep_data_name





