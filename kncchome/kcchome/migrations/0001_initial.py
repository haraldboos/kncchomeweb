# Generated by Django 5.0.3 on 2024-03-17 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nevbar',
            fields=[
                ('nevbrtext', models.TextField(max_length=10, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='1-for show 0 for not show')),
            ],
        ),
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='nevdrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, help_text='1-for show 0 for not show')),
                ('nevbar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kcchome.nevbar')),
            ],
        ),
    ]