# Generated by Django 4.2.14 on 2024-11-16 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('notifications', '0002_alter_notification_caregiver_alter_notification_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_viewed',
            field=models.BooleanField(default=False, help_text='Whether the notification has been viewed.'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(help_text='The user who triggered the notification.', limit_choices_to={'role': 'EU'}, on_delete=django.db.models.deletion.CASCADE, related_name='user_notifications', to='accounts.userprofile'),
        ),
    ]