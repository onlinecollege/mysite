# Generated by Django 3.2.5 on 2021-08-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0024_alter_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]