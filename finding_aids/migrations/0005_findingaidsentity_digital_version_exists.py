# Generated by Django 2.2.12 on 2020-07-31 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finding_aids', '0004_auto_20190704_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='findingaidsentity',
            name='digital_version_exists',
            field=models.BooleanField(default=False),
        ),
    ]