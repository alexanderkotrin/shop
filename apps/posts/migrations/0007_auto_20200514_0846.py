# Generated by Django 3.0.6 on 2020-05-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20200514_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]