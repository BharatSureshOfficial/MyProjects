# Generated by Django 4.2.1 on 2023-05-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="date",
            field=models.DateField(default="1996-12-13"),
            preserve_default=False,
        ),
    ]
