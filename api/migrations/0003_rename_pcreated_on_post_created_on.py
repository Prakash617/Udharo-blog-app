# Generated by Django 4.0.6 on 2022-07-09 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post_pcreated_on_post_updated_on_alter_post_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pcreated_on',
            new_name='created_on',
        ),
    ]
