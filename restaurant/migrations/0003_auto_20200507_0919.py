# Generated by Django 3.0.6 on 2020-05-07 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='order',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menu', to='restaurant.Menu'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
