# Generated by Django 4.0.4 on 2022-05-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingApp', '0003_alter_reserved_r_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserved',
            name='r_id',
        ),
        migrations.AddField(
            model_name='reserved',
            name='house_name',
            field=models.CharField(default='', max_length=150),
        ),
    ]