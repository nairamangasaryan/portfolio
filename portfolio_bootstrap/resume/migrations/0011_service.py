# Generated by Django 4.2.2 on 2023-07-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0010_personal_info_about"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("service_name", models.CharField(max_length=20)),
                ("service_description", models.TextField(max_length=200)),
            ],
        ),
    ]
