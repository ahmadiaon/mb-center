# Generated by Django 4.0.6 on 2022-07-20 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='details',
            field=models.CharField(default='none', max_length=500),
        ),
        migrations.AddField(
            model_name='feature',
            name='name',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
