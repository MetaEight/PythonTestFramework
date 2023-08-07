from variables import Uri
from utils.test_data.testData import get_value as TD


def test_create_new_user(reqres_api):
    user_name = TD('ApiTestData', 'new_user_name')
    user_job = TD('ApiTestData', 'new_user_job')

    input_data = {
        "name": user_name,
        "job": user_job
    }
    response = reqres_api.post(path=Uri.get_user, data=input_data)
    responseJson = response.json()

    assert response.status_code == 201, f"Error, expected status code 201 instead {response.status_code}"
    assert responseJson['name'] == user_name, f"Error, expected user name '{user_name}' instead '{responseJson['name']}'"
    assert responseJson['job'] == user_job, f"Error, expected job '{user_job}' instead '{responseJson['job']}'"
    assert int(responseJson['id']) > 0, f"Error, user id is incorrect"


def test_fetch_user(reqres_api):
    path = f'{Uri.get_user}/2'
    email = TD('ApiTestData', 'expected_email')
    first_name = TD('ApiTestData', 'expected_first_name')
    last_name = TD('ApiTestData', 'expected_last_name')

    response = reqres_api.get(path=path)
    responseJson = response.json()

    assert response.status_code == 200, f"Error, expected status code 200 instead {response.status_code}"
    assert responseJson['data']['id'] == 2, f"Error, expected user id '2' instead '{responseJson['data']['id']}'"
    assert responseJson['data']['email'] == email, f"Error, expected user email '{email}' instead '{responseJson['data']['email']}'"
    assert responseJson['data']['first_name'] == first_name, f"Error, expected user first name '{first_name}' instead '{responseJson['data']['first_name']}'"
    assert responseJson['data']['last_name'] == last_name, f"Error, expected user last name '{last_name}' instead '{responseJson['data']['last_name']}'"


def test_get_nonexistent_user_data(reqres_api):
    path = f'{Uri.get_user}/999'
    response = reqres_api.get(path=path)

    assert response.status_code == 404, f"Error, expected status code 404 instead {response.status_code}"


def test_get_list_users(reqres_api):
    path = f'{Uri.user_list}=2'

    response = reqres_api.get(path=path)
    responseJson = response.json()

    assert response.status_code == 200, f"Error, expected status code 200 instead {response.status_code}"
    assert responseJson['page'] == 2, f"Error, expected page '2' instead '{responseJson['page']}'"
    assert len(responseJson['data']) == responseJson['per_page'],\
        f"Error, expected '{responseJson['per_page']}' users per page instead '{len(responseJson['data'])}'"


def test_successful_registration(reqres_api):
    email = TD('ApiTestData', 'new_user_email')
    password = TD('ApiTestData', 'new_user_password')
    input_data = {
        "email": email,
        "password": password
    }

    response = reqres_api.post(path=Uri.register_user, data=input_data)
    responseJson = response.json()

    assert response.status_code == 200, f"Error, expected status code 200 instead {response.status_code}"
    assert len(responseJson['token']) > 0, f"Error, expected token instead '{responseJson['token']}'"


def test_unsuccessful_registration(reqres_api):
    email = TD('ApiTestData', 'new_user_email')
    input_data = {
        "email": email
    }

    response = reqres_api.post(path=Uri.register_user, data=input_data)
    responseJson = response.json()

    assert response.status_code == 400, f"Error, expected status code 400 instead {response.status_code}"
    assert responseJson['error'] == 'Missing password', \
        f"Expected error message 'Missing password' instead '{responseJson['error']}'"
