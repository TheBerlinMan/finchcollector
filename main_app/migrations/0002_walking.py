# Generated by Django 4.2.10 on 2024-02-29 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Walking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('length', models.IntegerField()),
                ('stuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.stuff')),
            ],
        ),
    ]
