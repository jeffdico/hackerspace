# Generated by Django 2.0.13 on 2019-03-12 22:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quest_manager', '0005_auto_20190312_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='import_id',
            field=models.UUIDField(default=uuid.uuid4,
                                   help_text='Only edit this if you want to link to a quest in another system so that when importing from that other system, it will update this quest. Otherwise do not edit this or it will break existing links!',
                                   unique=True),
        ),
    ]