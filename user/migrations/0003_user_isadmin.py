# Generated by Django 2.1.7 on 2019-09-24 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190622_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isAdmin',
            field=models.BooleanField(db_column='is_admin', default=False),
        ),
    ]
