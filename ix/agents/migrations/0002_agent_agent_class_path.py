# Generated by Django 4.2 on 2023-04-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agents", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="agent",
            name="agent_class_path",
            field=models.CharField(
                default="ix.agents.auto_agent.AutoAgent", max_length=255
            ),
            preserve_default=False,
        ),
    ]
