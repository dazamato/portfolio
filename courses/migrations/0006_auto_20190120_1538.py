# Generated by Django 2.1.3 on 2019-01-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_course_isfree'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='video',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=5, max_length=5),
        ),
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]