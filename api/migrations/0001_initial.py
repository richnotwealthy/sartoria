# Generated by Django 2.2 on 2019-04-21 06:50

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
            name='Bin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='SartoriaUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('auth_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.SartoriaUser')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('image', models.ImageField(upload_to='uploaded_image_data/')),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Bin')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.SartoriaUser')),
                ('tags', models.ManyToManyField(to='api.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='bin',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.SartoriaUser'),
        ),
    ]