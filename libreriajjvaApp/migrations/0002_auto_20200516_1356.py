# Generated by Django 3.0.6 on 2020-05-16 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreriajjvaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autores',
            options={'managed': False, 'ordering': ['id_autor']},
        ),
        migrations.AlterModelOptions(
            name='categorias',
            options={'managed': False, 'ordering': ['id_categoria']},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'managed': False, 'ordering': ['id_cliente']},
        ),
    ]
