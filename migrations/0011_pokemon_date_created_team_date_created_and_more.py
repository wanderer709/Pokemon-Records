# Generated by Django 4.0.1 on 2022-04-13 19:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0010_pokemon_type1_pokemon_type2'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='team',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='gender',
            field=models.CharField(blank=True, choices=[('♂', 'Male'), ('♀', 'Female'), (' ', 'Genderless')], default=' ', max_length=1, null=True),
        ),
    ]