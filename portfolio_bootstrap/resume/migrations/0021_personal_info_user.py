# Generated by Django 4.2.2 on 2023-07-18 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("resume", "0020_portfoliodetails_alter_experience_job_discription_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="personal_info",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
