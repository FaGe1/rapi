# Generated by Django 4.1.4 on 2022-12-09 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tg_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('tg_id', models.CharField(max_length=60)),
                ('is_in_crm', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField()),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.tg_user')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.offer')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('developers', models.ManyToManyField(to='api.tg_user')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='man', to='api.tg_user')),
                ('tasks', models.ManyToManyField(to='api.task')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.tg_user'),
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('dev_chat_id', models.CharField(max_length=100)),
                ('cus_chat_id', models.CharField(max_length=100)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.tg_user')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.offer')),
            ],
        ),
    ]
