# Generated by Django 3.1.7 on 2021-02-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210227_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='asset',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
