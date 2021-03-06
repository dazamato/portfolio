# Generated by Django 2.1.3 on 2019-02-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190210_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='teacher',
        ),
        migrations.AddField(
            model_name='user',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cv/', verbose_name='cv'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='user.png', upload_to='profile_pic/'),
        ),
    ]
