# Generated by Django 3.1.7 on 2021-03-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Data_source',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
