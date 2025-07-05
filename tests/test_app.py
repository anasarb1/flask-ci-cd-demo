from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
