# Generated by Django 4.2.3 on 2023-07-18 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default='django', max_length=255),
            preserve_default=False,
        ),
    ]
