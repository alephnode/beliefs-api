# Generated by Django 2.0.1 on 2018-01-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propositions', '0001_initial'),
        ('sources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='link',
            field=models.CharField(default='no source', max_length=100),
        ),
        migrations.AddField(
            model_name='source',
            name='propositions',
            field=models.ManyToManyField(related_name='sources_for_propositions', to='propositions.Proposition'),
        ),
    ]
