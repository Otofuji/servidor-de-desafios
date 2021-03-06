# Generated by Django 3.0.2 on 2020-02-07 18:04

from django.db import migrations, models
import django.db.models.deletion
import teste_de_mesa.models
import teste_de_mesa.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesteDeMesa',
            fields=[
                ('exercicio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Exercicio')),
                ('codigo', teste_de_mesa.models.NonStrippingTextField()),
                ('gabarito', models.TextField(validators=[teste_de_mesa.validators.json_validator])),
            ],
            options={
                'verbose_name_plural': 'testes de mesa',
            },
            bases=('core.exercicio',),
        ),
    ]
