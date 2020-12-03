# Generated by Django 3.1.3 on 2020-12-03 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_key', models.CharField(db_index=True, max_length=40, verbose_name='Chave do carrinho')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Item do carrinho',
                'verbose_name_plural': 'Itens dos carrinhos',
                'unique_together': {('cart_key', 'product')},
            },
        ),
    ]
