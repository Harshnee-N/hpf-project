from django.urls import path
from .views import BookingRequestCreateView, LSASearchView

urlpatterns = [
    path(
        'api/v1/bookings/',
        BookingRequestCreateView.as_view(),
        name='create-booking'
    ),
    path(
        'api/v1/lsas/search/',
        LSASearchView.as_view(),
        name='lsa-search'
    ),
]