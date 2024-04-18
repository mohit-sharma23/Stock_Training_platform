# Generated by Django 4.1.2 on 2024-01-15 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('Stock_Game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.IntegerField()),
                ('reg_room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock_Game.room')),
                ('reg_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.profile')),
            ],
        ),
    ]
