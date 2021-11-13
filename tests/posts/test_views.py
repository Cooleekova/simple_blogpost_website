import pytest
# from django.urls import reverse
# from rest_framework.status import HTTP_302_FOUND
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() == 1


#
# # проверка редиректа неавторизованного пользователя
# # вместо получения списка постов на login page
# @pytest.mark.django_db
# def test_get_posts(auth_client, post_factory):
#     # создаём десять постов
#     post_factory(_quantity=10)
#     url = reverse("posts:posts")
#     # совершаем запрос GET к API по URL
#     resp = auth_client.get(url)
#     assert resp.status_code == HTTP_302_FOUND
