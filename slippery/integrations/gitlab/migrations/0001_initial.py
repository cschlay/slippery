# Generated by Django 3.0.8 on 2020-07-04 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0007_auto_20200702_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]
