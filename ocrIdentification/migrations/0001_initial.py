# Generated by Django 2.2 on 2021-10-09 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(blank=True, max_length=1000, null=True, verbose_name='image_url')),
                ('questions', models.CharField(blank=True, max_length=100, null=True, verbose_name='questions')),
                ('merchant', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='temp_mer_user', to='merchant.Merchant')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='templ_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
