# Generated by Django 3.1.3 on 2020-12-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='links',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
