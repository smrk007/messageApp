# Generated by Django 4.0.2 on 2022-02-03 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='passwordHash',
        ),
    ]