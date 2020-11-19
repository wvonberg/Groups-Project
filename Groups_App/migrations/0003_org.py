# Generated by Django 3.1.2 on 2020-11-11 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groups_App', '0002_auto_20201110_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('members', models.ManyToManyField(related_name='orgs', to='Groups_App.User')),
            ],
        ),
    ]
