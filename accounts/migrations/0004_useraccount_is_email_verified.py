# Generated by Django 4.2.4 on 2023-10-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_useraccount_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
