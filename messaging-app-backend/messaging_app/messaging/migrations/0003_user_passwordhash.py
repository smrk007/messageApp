# Generated by Django 4.0.2 on 2022-02-03 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_remove_user_passwordhash'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passwordHash',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
