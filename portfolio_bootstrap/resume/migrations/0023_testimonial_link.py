# Generated by Django 4.2.2 on 2023-07-18 06:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0022_remove_personal_info_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="testimonial",
            name="link",
            field=models.URLField(
                blank=True, null=True, validators=[django.core.validators.URLValidator]
            ),
        ),
    ]
