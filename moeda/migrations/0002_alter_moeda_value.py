# Generated by Django 4.0 on 2021-12-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("moeda", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="moeda",
            name="value",
            field=models.CharField(max_length=20, verbose_name="Valor"),
        ),
    ]
