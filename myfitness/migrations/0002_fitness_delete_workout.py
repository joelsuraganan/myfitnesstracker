# Generated by Django 4.2.7 on 2023-11-25 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfitness', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('date', models.DateField(default='25-11-2023')),
                ('lift', models.CharField(max_length=3)),
                ('reps', models.IntegerField(max_length=3)),
                ('weight', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
