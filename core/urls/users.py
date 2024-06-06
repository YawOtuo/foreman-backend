from django.urls import path

from core.views.user import UserDetail, UserList

urlpatterns = [
    path('', UserList.as_view(), name='users_list'),
    path('<int:pk>/', UserDetail.as_view(), name='users_detail'),
]
