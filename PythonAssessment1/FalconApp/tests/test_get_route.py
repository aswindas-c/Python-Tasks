import pytest
from falcon import testing
from FalconApp.main import app
import mongomock

@pytest.fixture
def mongomock_patch():
    with mongomock.patch(servers=(('localhost', 27017),)):
        yield

@pytest.fixture
def client(mongomock_patch):
    return testing.TestClient(app)
class TestGet:

    def test_get_route_user_not_exist(self,client):
        response = client.simulate_get('/users/asw@example.com')
        assert response.status_code == 404
        assert response.json == {'Message': 'User not exist'}

    def test_get_route_user_exist(self,client):
        data = {'name': 'Aswin', 'email': 'aswin@example.com', 'age': 30}
        client.simulate_post('/users', json=data)
        response = client.simulate_get('/users/aswin@example.com')
        assert response.status_code == 200
        assert response.json == data

    def test_get_route_invalid_email(self,client):
        response = client.simulate_get('/users/aswin')
        assert response.status_code == 400
        assert response.json == {'title': 'Invalid email'}