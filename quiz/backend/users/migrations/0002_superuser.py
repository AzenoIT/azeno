# Generated by Django 4.1.7 on 2023-03-16 09:25
import os

from django.db import migrations


def create_superuser(apps, schema_editor):
    User = apps.get_model('users', 'CustomUser')

    DJ_SU_NAME = os.environ.get('DJ_SU_NAME')
    DJ_SU_EMAIL = os.environ.get('DJ_SU_EMAIL')
    DJ_SU_PASSWORD = os.environ.get('DJ_SU_PASSWORD')

    User.objects.create_superuser(
        email=DJ_SU_EMAIL,
        username=DJ_SU_NAME,
        password=DJ_SU_PASSWORD
    )

def delete_superuser(apps, schema_editor):
    User = apps.get_model('users', 'CustomUser')
    admin = User.objects.get(email=os.environ.get('DJ_SU_EMAIL'))
    if admin.is_superuser:
        admin.delete()
    else:
        raise IndexError('User with id = 1 is not an admin.')



class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser, delete_superuser)
    ]
