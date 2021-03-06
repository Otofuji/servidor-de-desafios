# Generated by Django 3.0.2 on 2020-02-04 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('exercicio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Exercicio')),
                ('replit_url', models.CharField(blank=True, max_length=1024)),
            ],
            options={
                'verbose_name_plural': 'tutoriais',
            },
            bases=('core.exercicio',),
        ),
        migrations.CreateModel(
            name='AcessoAoTutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_acesso', models.DateTimeField(auto_now_add=True, verbose_name='primeiro acesso')),
                ('ultimo_acesso', models.DateTimeField(auto_now=True, verbose_name='ultimo acesso')),
                ('total_acessos', models.IntegerField(default=0)),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.Tutorial')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'acessos ao tutorial',
            },
        ),
    ]
