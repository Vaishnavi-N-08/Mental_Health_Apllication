# Generated by Django 3.2.8 on 2022-01-12 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SoulPlace', '0002_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.DecimalField(decimal_places=0, max_digits=10)),
                ('suggestion', models.CharField(max_length=500)),
            ],
        ),
    ]
