# Generated by Django 2.1.2 on 2018-10-08 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0005_auto_20181001_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('daily_value', models.PositiveIntegerField()),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal', to='core.Action')),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
    ]