# Generated by Django 4.2.14 on 2024-11-15 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('communication', '0005_merge_0002_alter_icon_caregiver_0004_alter_icon_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='caregiver',
            field=models.ForeignKey(default=None, limit_choices_to={'role': 'CG'}, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='accounts.userprofile'),
            preserve_default=False,
        ),
    ]