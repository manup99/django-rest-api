from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns=[
    # path('',StatusAPIView.as_view()),
    # #path('get/<int:id>',StatusGETApi.as_view()),
    # path('get/<int:id>',StatusDetailAPIView.as_view()),
    # path('update/<int:id>', StatusUpdateAPIView.as_view()),
    # path('create',StatusCreateAPIView.as_view()),
    # # path('<int:id>/update',StatusUpdateAPI.as_view()),
    # path('delete/<int:id>',StatusDeleteAPIView.as_view())
    path('',StatusView.as_view()),
    path('look/<int:id>',StatusView1.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth',AuthView.as_view()),
    path('auth1',LoginView.as_view()),
    ###API endpoint made using serializer
    path('auth/api',RegisterSerializerView.as_view())
]