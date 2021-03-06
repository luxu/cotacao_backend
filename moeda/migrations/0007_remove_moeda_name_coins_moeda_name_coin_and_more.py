# Generated by Django 4.0 on 2021-12-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("moeda", "0006_moeda_name_coins"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="moeda",
            name="name_coins",
        ),
        migrations.AddField(
            model_name="moeda",
            name="name_coin",
            field=models.CharField(
                choices=[("Real", "Real"), ("Iene", "Iene"), ("Euro", "Euro")],
                max_length=5,
                null=True,
                verbose_name="Moeda",
            ),
        ),
        migrations.AlterField(
            model_name="moeda",
            name="initials",
            field=models.CharField(
                choices=[("BRL", "BRL"), ("JPY", "JPY"), ("EUR", "EUR")],
                max_length=3,
                null=True,
                verbose_name="Sigla da moeda",
            ),
        ),
    ]
