# Generated by Django 3.2.5 on 2021-07-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210728_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Punjabi', 'Punjabi')], default='English', max_length=40),
        ),
    ]