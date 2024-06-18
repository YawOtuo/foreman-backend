from django.urls import path

from core.views.user import UserDetail, UserGetOrCreateByUid, UserList

urlpatterns = [
    path('', UserList.as_view(), name='users_list'),
    path('get-or-create-user-by-uid/', UserGetOrCreateByUid.as_view(), name='users_list'),

    path('<int:pk>/', UserDetail.as_view(), name='users_detail'),
]
