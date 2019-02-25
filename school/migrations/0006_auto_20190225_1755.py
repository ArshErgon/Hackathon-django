# Generated by Django 2.1.7 on 2019-02-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20190225_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentregistration',
            old_name='student_id',
            new_name='student_age',
        ),
        migrations.AddField(
            model_name='studentregistration',
            name='student_class',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
    ]