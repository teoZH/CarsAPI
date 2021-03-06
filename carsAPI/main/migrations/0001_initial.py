# Generated by Django 4.0.4 on 2022-04-28 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_models', to='main.carbrand')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('first_reg', models.DateField(blank=True, null=True)),
                ('odometer', models.IntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_brands', to='main.carbrand')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_models', to='main.carmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_cars', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
