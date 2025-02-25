# Generated by Django 3.0.4 on 2021-10-25 10:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_opfileinput_tissue_types_file_storage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meshfileinfo',
            old_name='maxFluence',
            new_name='thresholdFluence',
        ),
        migrations.AddField(
            model_name='tclinput',
            name='thresholdFluence',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
