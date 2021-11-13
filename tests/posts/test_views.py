import pytest
from django.urls import reverse
from rest_framework.status import HTTP_302_FOUND


# проверка получения списка постов
@pytest.mark.django_db
def test_get_posts(client, post_factory):

    # создаём десять постов
    post_factory(_quantity=10)
    url = reverse("posts:posts")
    # совершаем запрос GET к API по URL
    resp = client.get(url)
    assert resp.status_code == HTTP_302_FOUND

