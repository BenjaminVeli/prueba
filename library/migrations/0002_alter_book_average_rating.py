# Generated by Django 4.1.3 on 2022-12-02 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='average_rating',
            field=models.CharField(max_length=100),
        ),
    ]