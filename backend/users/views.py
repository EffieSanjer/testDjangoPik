from rest_framework.generics import CreateAPIView

from users.serializers import UserRegistrationSerializer


class UserRegistrationView(CreateAPIView):
    authentication_classes = []
    serializer_class = UserRegistrationSerializer
