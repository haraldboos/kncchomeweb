# Generated by Django 5.0.3 on 2024-03-17 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kcchome', '0005_nevdrop_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nevdrop',
            name='order',
        ),
    ]
