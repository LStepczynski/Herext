from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("register", views.register_page, name="register"),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_page, name="logout"),
    path("chatrooms", views.chatrooms_page, name="chatrooms"),
    path("chatroom/<int:id>", views.chatroom_page, name="chatroom"),
    path("chatroom/create", views.create_chatroom_page, name="create_chatroom"),
    path("chatroom/messages/<int:id>", views.chatroom_messages, name="chatroom_messages"),
    path("chatroom/delete/text/<int:chatid>/<int:textid>", views.delete_text_page, name="delete_text"),
    path("chatroom/delete/<int:chatid>", views.delete_chatroom_page, name="delete_chatroom"),
    path("chatroom/settings/<int:chatid>", views.chatroom_settings_page, name="chatroom_settings"),
    path("chatroom/remove-user/<int:chatid>/<str:user>", views.chatroom_remove_user_page, name="remove_user"),
    
]

