# Generated by Django 2.2 on 2020-11-17 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_auto_20201115_2107'),
        ('notifications', '0008_auto_20201115_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='thread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='messenger.Thread'),
        ),
    ]
