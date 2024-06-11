# Generated by Django 5.0.6 on 2024-06-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('year_release', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=15)),
                ('genre', models.ManyToManyField(to='games_genres.genre')),
            ],
        ),
    ]