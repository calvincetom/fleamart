from django.urls import path
from Main.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]