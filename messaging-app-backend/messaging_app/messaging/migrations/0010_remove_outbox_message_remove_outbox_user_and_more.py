# Generated by Django 4.0.2 on 2022-02-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0009_alter_inbox_message_alter_inbox_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outbox',
            name='message',
        ),
        migrations.RemoveField(
            model_name='outbox',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='receiverDel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='senderDel',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Inbox',
        ),
        migrations.DeleteModel(
            name='Outbox',
        ),
    ]
