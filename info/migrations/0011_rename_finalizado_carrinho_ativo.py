# Generated by Django 4.1.5 on 2024-01-02 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_remove_carrinho_status_carrinho_confirmado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrinho',
            old_name='finalizado',
            new_name='ativo',
        ),
    ]
