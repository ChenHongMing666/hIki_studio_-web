# Generated by Django 4.1.7 on 2023-02-26 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='tietle',
            field=models.CharField(max_length=200, verbose_name='主题'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='添加的时间'),
        ),
        migrations.CreateModel(
            name='Enty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='正文')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='添加的时间')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.topic', verbose_name='主题')),
            ],
            options={
                'verbose_name_plural': 'enties',
            },
        ),
    ]
