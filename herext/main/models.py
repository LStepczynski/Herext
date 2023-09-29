from django.db import models


class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()
    owner = models.CharField(max_length=100)
    creation_date = models.DateField()

    def __str__(self) -> str:
        return self.name

class Text(models.Model):
    content = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    creation_date = models.DateField()
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.chat_room}"


# # Create your models here.
# class Account(models.Model):
#     username = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=200)
#     admin = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return self.username

