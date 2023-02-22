from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

router = DefaultRouter()

models = ['user', 'email', 'password', 'phone', 'picture']

# adding routers
for k in range(len(models)):
    eval("router.register('{}', {}ViewSet,basename='{}')".format(models[k], str(models[k]).capitalize(), models[k]) )

urlpatterns = [
    # token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('login/', LoginViewSet.as_view({"get":"post"}), name='login'),
    path('register/', UserViewSet.as_view({"get":"register"}), name='register'),
    path('profile/<int:pk>/', UserViewSet.as_view({"get":"profile"}), name='profile'),

]

urlpatterns += router.urls