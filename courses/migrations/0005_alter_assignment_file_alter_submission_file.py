# Generated by Django 4.1 on 2023-04-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_assignment_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='file',
            field=models.FileField(blank=True, upload_to='assignments/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='file',
            field=models.FileField(blank=True, upload_to='submissions/%Y/%m/%d/'),
        ),
    ]
