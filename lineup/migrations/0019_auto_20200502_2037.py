# Generated by Django 3.0.5 on 2020-05-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineup', '0018_auto_20200502_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='From',
            new_name='End',
        ),
        migrations.AddField(
            model_name='show',
            name='Start',
            field=models.TimeField(null=True),
        ),
    ]