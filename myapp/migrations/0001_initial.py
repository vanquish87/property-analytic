# Generated by Django 4.0.5 on 2022-07-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('rent', models.IntegerField()),
                ('emi', models.IntegerField()),
                ('tax', models.IntegerField()),
                ('exp', models.IntegerField()),
            ],
        ),
    ]