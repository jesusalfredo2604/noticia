# Generated by Django 3.1.7 on 2021-04-03 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alcance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alcance', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('fecha', models.DateTimeField()),
                ('resumen', models.TextField(blank=True)),
                ('weblink', models.URLField(null=True)),
                ('alcance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticias.alcance')),
                ('autor', models.ManyToManyField(blank=True, to='noticias.Autor')),
                ('campo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticias.campo')),
                ('revista', models.ManyToManyField(blank=True, to='noticias.Revista')),
            ],
        ),
    ]
