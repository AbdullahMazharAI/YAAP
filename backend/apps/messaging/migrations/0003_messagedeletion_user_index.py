"""Add index on MessageDeletion.user for faster visible_to() subquery"""
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_rename_conv_updated_idx_conversatio_updated_c163ba_idx_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='messagedeletion',
            index=models.Index(fields=['user'], name='msg_deletion_user_idx'),
        ),
    ]
