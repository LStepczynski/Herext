# Generated by Django 4.2.5 on 2023-10-01 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_chatroom_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
