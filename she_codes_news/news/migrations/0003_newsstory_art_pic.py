# Generated by Django 3.0.8 on 2020-08-31 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200825_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='art_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]