from django.db import models


class Category(models.Model):

    name = models.CharField('Nome', max_length=50)
    slug = models.SlugField('Identificador', max_length=100)

    created_at = models.DateTimeField('Criado', auto_now_add=True)
    modified_at = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']


class Product(models.Model):

    name = models.CharField('Nome', max_length=50)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE, verbose_name='Categoria')
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=10)

    created_at = models.DateTimeField('Criado', auto_now_add=True)
    modified_at = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']