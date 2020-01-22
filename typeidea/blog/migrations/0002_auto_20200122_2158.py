# Generated by Django 2.2.3 on 2020-01-22 13:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete='CASCADE', to='blog.Category', verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='owner',
            field=models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
