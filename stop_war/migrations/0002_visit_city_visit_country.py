# Generated by Django 4.0.3 on 2022-03-04 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stop_war', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='city',
            field=models.CharField(default='Not determined', max_length=100),
        ),
        migrations.AddField(
            model_name='visit',
            name='country',
            field=models.CharField(default='Not determined', max_length=50),
        ),
    ]
