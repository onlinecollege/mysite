# Generated by Django 3.2.5 on 2021-07-16 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0010_paper_year_in_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman REAL'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
    ]
