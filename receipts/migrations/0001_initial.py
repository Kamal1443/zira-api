# Generated by Django 4.0.4 on 2022-04-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
