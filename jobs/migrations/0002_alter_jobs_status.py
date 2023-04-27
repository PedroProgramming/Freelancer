# Generated by Django 4.1.7 on 2023-03-31 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('C', 'Em criaçao'), ('AA', 'Arguardando aprovação'), ('F', 'Finalizado')], default='C', max_length=2),
        ),
    ]
