# Generated by Django 4.2.2 on 2023-07-16 05:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0019_rename_github_personal_info_www_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PortfolioDetails",
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
                ("project_name", models.CharField(max_length=20)),
                ("project_description", models.TextField(max_length=600)),
                (
                    "project_url",
                    models.URLField(validators=[django.core.validators.URLValidator]),
                ),
                ("project_date", models.DateField(blank=True, null=True)),
                (
                    "project_image1",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to="Media"
                    ),
                ),
                (
                    "project_image2",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to="Media"
                    ),
                ),
                (
                    "project_image3",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to="Media"
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name="experience",
            name="job_discription",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="personal_info",
            name="phone",
            field=models.CharField(max_length=40),
        ),
    ]
