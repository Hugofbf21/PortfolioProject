# Generated by Django 4.0.4 on 2022-05-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_post_delete_tarefa'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='texto',
            field=models.TextField(default='Text'),
        ),
    ]
