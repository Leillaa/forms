# Generated by Django 4.2.8 on 2023-12-18 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questionnaire', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата опроса')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surveys', to='questionnaire.questionnaire', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Ответ на опрос',
                'verbose_name_plural': 'Ответы на опросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questionnaire.question')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surveys', to='survey.survey')),
            ],
        ),
    ]
