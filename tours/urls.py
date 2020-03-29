from django.urls import path
from tours.views import MainView, DepartureView, TourView

urlpatterns = [
    path('', MainView.as_view()),
    path('departure/<str:departure_id>', DepartureView.as_view(), name='departure_url'),
    path('tour/<int:tour_id>', TourView.as_view(), name='tour_url'),
]