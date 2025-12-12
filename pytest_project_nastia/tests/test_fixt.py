import pytest

@pytest.fixture
def client_profile():
    return {"id": 7, "name": "Nastia", "status": "active"}

def test_client_id_is_int(client_profile):
    assert type(client_profile["id"]) is int

def test_client_is_active(client_profile):
    assert client_profile["status"] == "active"

    