# Generated by Django 4.1.7 on 2023-03-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="journal",
            name="lot",
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name="journal",
            name="pair",
            field=models.CharField(
                choices=[
                    ("EUR/USD", "EUR/USD"),
                    ("USD/JPY", "USD/JPY"),
                    ("GBP/USD", "GBP/USD"),
                    ("USD/CHF", "USD/CHF"),
                    ("AUD/USD", "AUD/USD"),
                    ("USD/CAD", "USD/CAD"),
                    ("NZD/USD", "NZD/USD"),
                    ("EUR/GBP", "EUR/GBP"),
                    ("EUR/JPY", "EUR/JPY"),
                    ("GBP/JPY", "GBP/JPY"),
                    ("CHF/JPY", "CHF/JPY"),
                    ("AUD/JPY", "AUD/JPY"),
                    ("CAD/JPY", "CAD/JPY"),
                    ("NZD/JPY", "NZD/JPY"),
                    ("GBP/CHF", "GBP/CHF"),
                    ("EUR/CAD", "EUR/CAD"),
                    ("EUR/AUD", "EUR/AUD"),
                    ("AUD/CAD", "AUD/CAD"),
                    ("AUD/NZD", "AUD/NZD"),
                    ("NZD/CAD", "NZD/CAD"),
                    ("EUR/CHF", "EUR/CHF"),
                    ("USD/HKD", "USD/HKD"),
                    ("USD/MXN", "USD/MXN"),
                    ("USD/SGD", "USD/SGD"),
                    ("USD/TRY", "USD/TRY"),
                    ("USD/ZAR", "USD/ZAR"),
                ],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="journal",
            name="stop_loss",
            field=models.DecimalField(
                blank=True, decimal_places=5, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="journal",
            name="take_profit",
            field=models.DecimalField(
                blank=True, decimal_places=5, max_digits=10, null=True
            ),
        ),
    ]