# Generated by Django 3.2.5 on 2021-07-16 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0014_alter_paper_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='paper_image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='paper',
            name='subject',
            field=models.CharField(choices=[('Isl I', 'Islamiat I'), ('Eng I', 'English I'), ('AD I', 'Animal Diversity I'), ('PD I', 'Plant Diversity I'), ('Maths', 'Essential Maths'), ('Isl II', 'Islamiat Ii'), ('Eng II', 'English Ii'), ('AD II', 'Animal Diversity Ii'), ('PD II', 'Plant Diversity Ii'), ('Chem I', 'Chemistry I'), ('Biostat', 'Biomaths And Biostats'), ('CB', 'Cell Biology'), ('MB', 'Molecular Biology'), ('Chem II', 'Chemistry Ii'), ('EVS', 'Environmental Science'), ('DEV', 'Developmental Biology'), ('AP', 'Animal Physiology'), ('PP', 'Plant Physiology'), ('Biophy', 'Biophysics'), ('Micro', 'Microbiology'), ('Immuno', 'Immunology'), ('Gen', 'Genetics'), ('Bioinfo', 'Bioinformatics And It'), ('Biochem', 'Biochemistry'), ('Eco', 'Ecology'), ('Evo', 'Organic Evolution'), ('TIB', 'Techniques In Biology')], default='', max_length=32),
        ),
    ]
