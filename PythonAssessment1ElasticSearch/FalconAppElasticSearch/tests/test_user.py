# import falcon
# import pytest
# from falcon import testing
# from FalconAppElasticSearch.controller.main_controller import MainController
#
#
# @pytest.fixture
# def client():
#     app = falcon.App()
#     controller = MainController()
#     app.add_route('/users', controller)
#     app.add_route('/users/{email}', controller)
#     return testing.TestClient(app)
#
# # Add a new user successfully
# def test_post_user_success(client, mocker):
#     mock_save = mocker.patch('FalconAppElasticSearch.models.user_model.User.convert_to_dict', return_value=None)
#     response = client.simulate_post('/users', json={'name': 'John Doe', 'email': 'john@example.com', 'age': 30})
#     assert response.status == falcon.HTTP_200
#     assert response.json == {'Message': 'User added successfully'}
#     mock_save.assert_called_once_with('John Doe', 'john@example.com', 30)
#
# #Test missing fields
# def test_post_route_missing_fields(client):
#     data = {'name': 'John'}
#     response = client.simulate_post('/users', json=data)
#     assert response.status_code == 400
#     assert response.json == {'title': 'Missing required fields : Name, email, and age are required'}
#
# #Invalid Email
# def test_post_route_invalid_email(client):
#     data = {'name': 'John','email':'aswin','age':23}
#     response = client.simulate_post('/users', json=data)
#     assert response.status_code == 400
#     assert response.json == {'title':'Invalid email'}
#
# #Email already exists
# def test_create_user_email_already_exists(client,mocker):
#     mock_get_collection = mocker.patch('FalconAppElasticSearch.models.mongodb_model.MongoDBModel.get_collection')
#     mock_collection = mock_get_collection.return_value
#     mock_collection.find_one.return_value = {'email': 'john@example.com'}
#     response = client.simulate_post('/users',
#                                          json={'name': 'John Doe', 'email': 'john@example.com', 'age': 30})
#     assert response.status == falcon.HTTP_400
#     assert response.json == {'title': 'Email already exists'}
#
# #Invalid age
# def test_post_route_invalid_age(client):
#     data = {'name': 'John','email':'aswin@com','age':"as"}
#     response = client.simulate_post('/users', json=data)
#     assert response.status_code == 400
#     assert response.json == {'title':'Age should be digit'}
#
# #get user not exist
# def test_get_route_user_not_exist(client, mocker):
#     mocker.patch('FalconAppElasticSearch.models.user_model.User.find_by_email', return_value=None)
#     response = client.simulate_get('/users/{aswin@gmail.com}')
#     assert response.status == falcon.HTTP_404
#     assert response.json == {'Message': 'User not exist'}
#
# #Invalid email
# def test_get_route_invalid_email(client):
#         response = client.simulate_get('/users/aswin')
#         assert response.status_code == 400
#         assert response.json == {'title': 'Invalid email'}
#
# #Get user by email
# def test_get_route_user_exist(client,mocker):
#     mock_user = {'name': 'Arun', 'email': 'arun@gmail.com', 'age': 30}
#     mocker.patch('FalconAppElasticSearch.models.user_model.User.find_by_email', return_value=mock_user)
#     response = client.simulate_get('/users/{arun@gmail.com}')
#     assert response.status_code == 200
#     assert response.json == mock_user
#
