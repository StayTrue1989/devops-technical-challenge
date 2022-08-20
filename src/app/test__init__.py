from fastapi.testclient import TestClient

from .__init__ import app

client = TestClient(app)

# Testing the example integer values from the devops challenge instructions.
def test_int():
    response = client.get("/sum/10/2")
    assert response.status_code == 200
    assert response.json() == {"sum": 12}


# Testing two floating point numbers.
def test_float():
    response = client.get("/sum/10.5/2.4")
    assert response.status_code == 200
    assert response.json() == {"sum": 12.9}


# String values should return an HTTP status code of 422 "Unprocessable Entity".
def test_string():
    response = client.get("/sum/notanumber/string")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "value1"],
                "msg": "value is not a valid integer",
                "type": "type_error.integer",
            },
            {
                "loc": ["path", "value1"],
                "msg": "value is not a valid float",
                "type": "type_error.float",
            },
            {
                "loc": ["path", "value2"],
                "msg": "value is not a valid integer",
                "type": "type_error.integer",
            },
            {
                "loc": ["path", "value2"],
                "msg": "value is not a valid float",
                "type": "type_error.float",
            },
        ]
    }


# Verify the Swagger documentation is accessible at /docs.
def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200
