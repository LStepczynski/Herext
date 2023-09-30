from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("register", views.register_page, name="register"),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_page, name="logout"),
    path("chatrooms", views.chatrooms_page, name="chatrooms"),
    path("chatroom/<int:id>", views.chatroom_page, name="chatroom"),
    path("create-chatroom", views.create_chatroom_page, name="create_chatroom"),
]

