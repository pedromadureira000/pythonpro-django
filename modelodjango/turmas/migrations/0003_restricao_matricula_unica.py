# Generated by Django 3.2.4 on 2021-06-24 11:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turmas', '0002_criacao_matricula'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matricula',
            options={'ordering': ['turma', 'data']},
        ),
        migrations.AlterUniqueTogether(
            name='matricula',
            unique_together={('usuario', 'turma')},
        ),
    ]
