import pytest



def test_get_posts(api_client):
    response = api_client.get(api_client.base_url + "/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_single_post(api_client):
    post_id = 1
    url = api_client.base_url + f"/posts/{post_id}"

    response = api_client.get(url)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == post_id
    assert "userId" in data
    assert "title" in data
    assert "body" in data

def test_get_post_not_found(api_client):
    post_id = 999999
    url = api_client.base_url + f"/posts/{post_id}"

    response = api_client.get(url)

    assert response.status_code in (200, 404)

    data = response.json()
    assert isinstance(data, dict)
    if "id" in data:
        assert data["id"] != post_id

def test_create_post(api_client):
    payload = {
         "title": "My test title",
        "body": "My test text",
        "userId": 1
        }
    response = api_client.post(api_client.base_url + "/posts/", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    assert "id" in data

def test_lets_put(api_client):                          # создаем тест
    url = api_client.base_url + "/posts/1"              # make url
    payload = {
        "id": 1,
    "title": "New title",                               # sending data
    "body": "New body",
    "userId": 1
    }
    response = api_client.put(url, json=payload)        # check that we are getting a response in json

    assert response.status_code in (200, 201)           # putting data codes
    
    data = response.json()
    assert isinstance(data, dict)

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    
def test_lets_delete(api_client):
    url = api_client.base_url + "/posts/1"

    response = api_client.delete(url)

    assert response.status_code in [200]

















    

