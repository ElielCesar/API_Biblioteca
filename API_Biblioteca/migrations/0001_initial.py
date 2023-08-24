# Generated by Django 4.2.4 on 2023-08-24 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('idade', models.PositiveIntegerField()),
                ('cidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('data_pub', models.PositiveIntegerField()),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField(auto_now_add=True)),
                ('leitor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='API_Biblioteca.leitor')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='API_Biblioteca.livro')),
            ],
        ),
    ]