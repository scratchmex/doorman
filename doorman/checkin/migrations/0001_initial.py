# Generated by Django 3.1.3 on 2020-11-11 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ext_number", models.PositiveSmallIntegerField()),
                ("street", models.CharField(max_length=50)),
                ("int_number", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("suburb", models.CharField(blank=True, max_length=50, null=True)),
                ("postal_code", models.PositiveIntegerField(blank=True, null=True)),
                ("city", models.CharField(blank=True, max_length=50, null=True)),
                ("state", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "country",
                    models.CharField(
                        blank=True, default="Mexico", max_length=50, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Checkin",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time_created", models.DateTimeField(auto_now_add=True)),
                ("verified", models.BooleanField(default=False)),
                ("time_verified", models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="House",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Owner",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Plate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Visitor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
    ]