# Generated by Django 4.1.4 on 2022-12-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=60)),
                ('from_name', models.CharField(max_length=60)),
                ('from_id', models.CharField(max_length=60)),
            ],
        ),
    ]
