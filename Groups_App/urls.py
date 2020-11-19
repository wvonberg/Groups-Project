from django.urls import path
from . import views

urlpatterns = [
    path('', views.take_to_main),
    path('main', views.main),
    path('register', views.register),
    path('login', views.login),
    path('groups', views.groups),
    path('logout', views.logout),
    path('create_org', views.create_org),
    path('groups/<int:group_id>',views.one_group),
    path('add_member/<int:group_id>', views.add_member),
    path('remove_member/<int:group_id>', views.remove_member),
    path('groups_partial/<int:group_id>',views.groups_partial),
]