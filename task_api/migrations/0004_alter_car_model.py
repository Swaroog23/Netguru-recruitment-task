# Generated by Django 3.2.7 on 2021-09-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_api', '0003_alter_carrating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
