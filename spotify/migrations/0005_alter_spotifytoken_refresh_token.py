# Generated by Django 4.0.5 on 2022-12-13 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0004_alter_spotifytoken_refresh_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='refresh_token',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
