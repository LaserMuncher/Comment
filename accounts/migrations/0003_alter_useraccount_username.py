# Generated by Django 3.2.8 on 2023-10-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_useraccount_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]