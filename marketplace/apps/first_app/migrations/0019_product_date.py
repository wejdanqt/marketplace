# Generated by Django 3.0 on 2019-12-31 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0018_auto_20191222_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
