# Generated by Django 3.0.5 on 2020-06-09 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingPageTester', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=100)),
                ('page_url', models.URLField(max_length=300)),
                ('page_traffic', models.FloatField()),
                ('page_status', models.IntegerField()),
                ('page_signups', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='traffic',
            name='stats',
            field=models.FloatField(),
        ),
    ]