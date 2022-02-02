# Generated by Django 4.0.2 on 2022-02-02 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.TimeField()),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('passwordHash', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Outbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messaging.message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messaging.user')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='messaging.user'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='messaging.user'),
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField()),
                ('read', models.BooleanField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messaging.message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messaging.user')),
            ],
        ),
    ]
