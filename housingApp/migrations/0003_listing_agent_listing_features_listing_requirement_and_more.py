# Generated by Django 4.0.4 on 2022-05-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingApp', '0002_listing_availability_alter_listing_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='agent',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='listing',
            name='features',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='listing',
            name='requirement',
            field=models.CharField(default='', max_length=750),
        ),
        migrations.AlterField(
            model_name='listing',
            name='location',
            field=models.CharField(help_text='Area Located in Town', max_length=50),
        ),
        migrations.AlterField(
            model_name='listing',
            name='town',
            field=models.CharField(help_text='The town where the property is located', max_length=50),
        ),
    ]
