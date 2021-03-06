from django.urls import path
from .views import UserView, SingleUserView

app_name = 'app'


urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', SingleUserView.as_view()),
]