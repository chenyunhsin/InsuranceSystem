# Generated by Django 5.0.1 on 2024-01-10 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Policyholder",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=10, unique=True)),
                ("name", models.CharField(max_length=25)),
                ("registration_date", models.DateTimeField(auto_now_add=True)),
                (
                    "introducer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="policyholders",
                        to="policyholders.policyholder",
                    ),
                ),
            ],
        ),
    ]