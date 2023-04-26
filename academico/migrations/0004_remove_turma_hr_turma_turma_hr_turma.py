# Generated by Django 4.1.6 on 2023-04-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0003_horario_turma_hr_turma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='hr_turma',
        ),
        migrations.AddField(
            model_name='turma',
            name='hr_turma',
            field=models.ManyToManyField(related_name='horario', to='academico.horario'),
        ),
    ]