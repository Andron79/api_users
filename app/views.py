from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializers


class UserView(ListCreateAPIView):
    """Список пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializers


class SingleUserView(RetrieveUpdateDestroyAPIView):
    """Единичный пользователь"""

    queryset = User.objects.all()
    serializer_class = UserSerializers
