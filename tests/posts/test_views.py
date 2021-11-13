import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK


# проверка получения списка постов
@pytest.mark.django_db
def test_get_posts(client, post_factory):
    # создаём десять постов
    post_factory(_quantity=10)
    url = reverse("posts-list")
    # совершаем запрос GET к API по URL
    resp = client.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json
    # проверяем, что вернувшийся json содержит десять записей
    assert len(resp_json) == 10
