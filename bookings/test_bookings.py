import pytest
from rest_framework.test import APIClient

from .models import Parent, LSAProfile


@pytest.fixture
def setup_data():
    parent = Parent.objects.create(
        name="Test Parent",
        email="parent@test.com",
        phone="9876543210"
    )

    lsa = LSAProfile.objects.create(
        name="Test LSA",
        email="lsa@test.com",
        skills="Autism, ADHD",
        is_active=True
    )

    return parent, lsa


@pytest.mark.django_db
def test_booking_success(setup_data):
    parent, lsa = setup_data
    client = APIClient()

    response = client.post(
        "/api/v1/bookings/",
        {
            "parent": parent.id,
            "lsa": lsa.id,
            "start_time": "2026-08-15T10:00:00Z",
            "end_time": "2026-08-15T11:00:00Z",
        },
        format="json"
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_booking_invalid_time(setup_data):
    parent, lsa = setup_data
    client = APIClient()

    response = client.post(
        "/api/v1/bookings/",
        {
            "parent": parent.id,
            "lsa": lsa.id,
            "start_time": "2026-08-15T11:00:00Z",
            "end_time": "2026-08-15T10:00:00Z",
        },
        format="json"
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_booking_missing_parent():
    client = APIClient()

    response = client.post(
        "/api/v1/bookings/",
        {
            "lsa": 1,
            "start_time": "2026-08-15T10:00:00Z",
            "end_time": "2026-08-15T11:00:00Z",
        },
        format="json"
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_lsa_search_by_skill(setup_data):
    _, lsa = setup_data
    client = APIClient()

    response = client.get(
        "/api/v1/lsas/search/?skill=Autism"
    )

    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_lsa_search_available(setup_data):
    _, lsa = setup_data
    client = APIClient()

    response = client.get(
        "/api/v1/lsas/search/?available=true"
    )

    assert response.status_code == 200
    assert len(response.data) == 1