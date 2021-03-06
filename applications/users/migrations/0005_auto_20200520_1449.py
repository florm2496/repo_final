# Generated by Django 3.0.6 on 2020-05-20 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prueba1', '0001_initial'),
        ('subdepto', '0002_auto_20200518_0854'),
        ('users', '0004_auto_20200520_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='depto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='departamento', to='prueba1.Departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='subdepto',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='subdepto', to='subdepto.Subdepto'),
            preserve_default=False,
        ),
    ]
