# Generated by Django 3.2.5 on 2021-07-13 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('zipcode', models.CharField(max_length=5)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.car')),
            ],
        ),
    ]
