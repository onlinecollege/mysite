# Generated by Django 3.2.5 on 2021-08-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0020_note_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
