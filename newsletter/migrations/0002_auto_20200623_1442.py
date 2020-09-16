# Generated by Django 2.1.15 on 2020-06-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="subscription", name="first_name",),
        migrations.RemoveField(model_name="subscription", name="last_name",),
        migrations.AddField(
            model_name="subscription",
            name="name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
