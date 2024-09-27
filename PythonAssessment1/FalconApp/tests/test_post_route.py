import pytest
from mongomock import MongoClient
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

@pytest.fixture
def mock_client():
    return MongoClient()

@pytest.fixture
def mock_db(mock_client):
    return mock_client['falcon_db']

class TestPost:
    #Test missing fields
    def test_post_route_missing_fields(self, client):
        data = {'name': 'John'}
        response = client.simulate_post('/users', json=data)
        assert response.status_code == 400
        assert response.json == {'title': 'Missing required fields : Name, email, and age are required'}

    #Invalid Email
    def test_post_route_invalid_email(self, client):
        data = {'name': 'John','email':'aswin','age':23}
        response = client.simulate_post('/users', json=data)
        assert response.status_code == 400
        assert response.json == {'title':'Invalid email'}

    #User Added successfully
    def test_post_route_user_success(self, client):
        data = {'name': 'John','email':'aswin@21','age':23}
        response = client.simulate_post('/users', json=data)
        assert response.status_code == 200
        assert response.json == {'Message': 'User added successfully'}
    #Email Already exists
    def test_post_route_email_already_exists(self, client, mock_db):
        data = {'name': 'Aswin', 'email': 'john@example.com', 'age': 30}
        client.simulate_post('/users', json=data)
        data = {'name': 'Jane', 'email': 'john@example.com', 'age': 25}
        response = client.simulate_post('/users', json=data)
        assert response.status_code == 400
        assert response.json == {'title':'Email already exists'}

    #Invalid age
    def test_post_route_invalid_age(self, client):
        data = {'name': 'John','email':'aswin@com','age':"as"}
        response = client.simulate_post('/users', json=data)
        assert response.status_code == 400
        assert response.json == {'title':'Age should be digit'}

    #Drop the collection
    def tear_down(self):
        self.drop_collection('users')
