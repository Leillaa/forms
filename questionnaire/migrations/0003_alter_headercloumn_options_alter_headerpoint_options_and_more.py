# Generated by Django 4.2.8 on 2023-12-20 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_headercloumn_headerpoint_point_header_cloumn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headercloumn',
            options={'ordering': ['num_col'], 'verbose_name': 'Заголовок', 'verbose_name_plural': 'Заголовки'},
        ),
        migrations.AlterModelOptions(
            name='headerpoint',
            options={'verbose_name': 'Название колонки', 'verbose_name_plural': 'Название колонок'},
        ),
        migrations.AlterField(
            model_name='headerpoint',
            name='header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.headercloumn'),
        ),
        migrations.AlterField(
            model_name='headerpoint',
            name='point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.point'),
        ),
        migrations.AlterField(
            model_name='point',
            name='header_cloumn',
            field=models.ManyToManyField(related_name='points', through='questionnaire.HeaderPoint', to='questionnaire.headercloumn'),
        ),
        migrations.AddConstraint(
            model_name='headerpoint',
            constraint=models.UniqueConstraint(fields=('point', 'header'), name='unique_header_in_table'),
        ),
    ]
