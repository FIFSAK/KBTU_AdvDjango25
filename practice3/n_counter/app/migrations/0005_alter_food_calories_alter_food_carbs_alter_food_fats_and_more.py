# Generated by Django 5.1.6 on 2025-02-23 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_consume_date_alter_food_calories_alter_food_carbs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='fats',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='proteins',
            field=models.FloatField(default=0),
        ),
    ]
