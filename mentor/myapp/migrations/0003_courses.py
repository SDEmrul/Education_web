# Generated by Django 5.1.3 on 2024-11-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=100)),
                ('c_name', models.CharField(max_length=100)),
                ('c_heading', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('c_pic', models.ImageField(upload_to='images/')),
                ('t_pic', models.ImageField(upload_to='images/')),
                ('price', models.DecimalField(decimal_places=6, max_digits=6)),
            ],
        ),
    ]
