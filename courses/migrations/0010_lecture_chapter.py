# Generated by Django 2.1.3 on 2019-01-23 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_lecture_attachments'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='chapter',
            field=models.CharField(default='Новый раздел', max_length=100),
        ),
    ]