# Generated by Django 2.2.4 on 2020-03-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minor', '0004_auto_20200319_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='group_message',
            field=models.TextField(blank=True, default='No message', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='mentor_message',
            field=models.TextField(blank=True, default='No message', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='hod_feedback',
            field=models.CharField(default='No feedback', max_length=1500),
        ),
        migrations.AlterField(
            model_name='project',
            name='mentor_feedback',
            field=models.CharField(default='No feedback', max_length=1500),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default='No status', max_length=1500),
        ),
    ]