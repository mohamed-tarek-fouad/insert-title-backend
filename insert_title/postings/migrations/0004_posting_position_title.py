# Generated by Django 4.0.5 on 2022-06-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0003_alter_posting_num_applicants'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='position_title',
            field=models.CharField(default='Data Analyst', max_length=150),
            preserve_default=False,
        ),
    ]