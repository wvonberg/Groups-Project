# Generated by Django 3.1.2 on 2020-11-11 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Groups_App', '0003_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='org',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_orgs', to='Groups_App.user'),
            preserve_default=False,
        ),
    ]
