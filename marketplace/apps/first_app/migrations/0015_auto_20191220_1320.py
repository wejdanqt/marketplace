# Generated by Django 3.0 on 2019-12-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0014_auto_20191220_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=45),
        ),
    ]
