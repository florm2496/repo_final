# Generated by Django 3.0.6 on 2020-05-18 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subdepto', '0002_auto_20200518_0854'),
        ('users', '0002_user_depto'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subdepto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subdepto', to='subdepto.Subdepto'),
            preserve_default=False,
        ),
    ]
