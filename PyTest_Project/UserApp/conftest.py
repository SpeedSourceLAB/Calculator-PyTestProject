import pytest

@pytest.fixture(scope='session')
def database_connection():
    print("Database Connection Established")
    return True

@pytest.fixture(scope='session')
def ui_open():
    return True

@pytest.fixture
def numbers():
    a=9
    b=3
    return a,b