# Generated by Django 3.0.8 on 2021-01-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empId', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('dept', models.CharField(max_length=200)),
            ],
        ),
    ]