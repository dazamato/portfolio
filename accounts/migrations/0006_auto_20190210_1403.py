# Generated by Django 2.1.3 on 2019-02-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='teacher',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='Данные не предоставлены еще', max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, default='Данные не предоставлены еще', max_length=30),
        ),
    ]
