# Generated by Django 4.1.7 on 2023-03-31 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_jobs_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='arquivo_final',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
