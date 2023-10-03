from django.db import models


class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()
    owner = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Text(models.Model):
    content = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.chat_room}"

class DeletedChatRoom(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()
    owner = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class DeletedText(models.Model):
    content = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    creation_date = models.DateTimeField()
    chat_room = models.ForeignKey(DeletedChatRoom, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.chat_room}"

