# Generated by Django 5.1.4 on 2024-12-11 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_remove_item_created_item_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
    ]
