# Generated by Django 2.1.7 on 2019-02-25 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_ownerschool_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='student_school',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='RegisterSchool',
        ),
    ]
