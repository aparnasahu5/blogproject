# Generated by Django 4.2.7 on 2023-12-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("theblog", "0006_alter_post_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="snippet",
            field=models.CharField(
                default="click blog title to open post", max_length=255
            ),
        ),
    ]
