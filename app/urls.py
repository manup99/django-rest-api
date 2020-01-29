from django.urls import path
from .views import StatusDeleteAPIView,StatusListAPI,StatusAPIView,StatusGETApi,StatusUpdateAPIView,StatusCreateAPIView,StatusDetailAPIView


urlpatterns=[
    path('',StatusAPIView.as_view()),
    #path('get/<int:id>',StatusGETApi.as_view()),
    path('get/<int:id>',StatusDetailAPIView.as_view()),
    path('update/<int:id>', StatusUpdateAPIView.as_view()),
    path('create',StatusCreateAPIView.as_view()),
    # path('<int:id>/update',StatusUpdateAPI.as_view()),
    path('delete/<int:id>',StatusDeleteAPIView.as_view())

]