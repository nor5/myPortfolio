# Generated by Django 4.0.4 on 2023-01-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_title_skills_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=200)),
                ('program', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Timeline',
            new_name='WorkExperience',
        ),
    ]
