# Generated by Django 4.2.7 on 2024-02-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_amounts_of_students_group_average_score_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='amounts_of_students',
        ),
        migrations.AlterField(
            model_name='group',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
