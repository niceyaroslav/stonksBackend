# Generated by Django 3.1.7 on 2021-03-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210302_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='current_value_of_asset',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=50, null=True),
        ),
    ]