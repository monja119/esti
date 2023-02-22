from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action

from rest_framework.permissions import AllowAny

from .serializers import *
from .models import *


class ObtainToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'email': user.name
        })

class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        try :
            # getting email
            user_email = Email.objects.get(email=email)

            # getting user as the email foreign
            user = User.objects.get(id=email.user)

            # getting the password
            user_password = Password.objects.get(user=user.id)

            if check_password(password, user_password):
                token = ObtainToken(user=user.id)
                # success login
                return Response(
                    {
                        'user data' :  user.data,
                        'token': token
                    }
                )

            else:
                # wrong password
                return Response(
                    'Wrong password'
                )

        except Email.DoesNotExist:
            return Response('Email does not exists')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def register(self, request):
        # request data
        user_name = request.data['name']
        user_matricule = request.data['matricule']
        user_email = request.data['email']
        user_password = request.data['password']

        user = User()
        user.name = user_name
        user.matricule = user_matricule
        user.save()

        email = Email()
        email.email = user_email
        email.user = user.id
        email.save()

        password = Password()
        password.password = make_password(user_password, hasher="default")
        password.user = user.id
        password.save()

        return Response(
            {
                'name': user.name,
                'matricule': user_matricule,
                'email': user_email,
            }
        )

    def get(self, request, pk):
        queryset = User.objects.get(id=pk)
        serializer = UserSerializer(queryset, many=False)

        return Response(serializer.data)

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer



class PasswordViewSet(viewsets.ModelViewSet):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

