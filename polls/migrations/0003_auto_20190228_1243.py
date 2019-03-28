# Generated by Django 2.1.5 on 2019-02-28 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190228_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='voted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]