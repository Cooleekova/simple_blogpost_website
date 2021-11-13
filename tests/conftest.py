import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def post_factory():
    def factory(**kwargs):
        return baker.make('Post', **kwargs)
    return factory

