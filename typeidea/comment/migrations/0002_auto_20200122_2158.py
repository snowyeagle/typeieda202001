# Generated by Django 2.2.3 on 2020-01-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete='CASCADE', to='blog.Post', verbose_name='评论目标'),
        ),
    ]