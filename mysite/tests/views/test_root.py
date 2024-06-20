import pytest
from django.urls import reverse

@pytest.mark.django_db

def test_root_view(client):
    url = reverse('root')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'RootView'
