# Generated by Django 5.0.6 on 2024-05-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_availablefor_category_fieldresearch_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='topic_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
