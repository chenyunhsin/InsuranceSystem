# Generated by Django 5.0.1 on 2024-01-10 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("policyholders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="policyholder",
            name="introducer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="policyholders",
                to="policyholders.policyholder",
            ),
        ),
    ]
