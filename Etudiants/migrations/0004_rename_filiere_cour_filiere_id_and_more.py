# Generated by Django 4.1.7 on 2023-02-28 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiants', '0003_rename_filiere_id_cour_filiere_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cour',
            old_name='filiere',
            new_name='filiere_id',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='cour',
            new_name='cour_id',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='student',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='filiere',
            new_name='filiere_id',
        ),
    ]
