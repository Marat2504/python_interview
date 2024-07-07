from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import signup


urlpatterns = [
    # Авторизация
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Обновление access token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Регистрация
    path('signup/', signup, name='signup'),
]