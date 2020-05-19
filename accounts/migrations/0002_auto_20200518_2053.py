# Generated by Django 2.1 on 2020-05-18 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_user', to='accounts.Profile')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_user', to='accounts.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='follow_set',
            field=models.ManyToManyField(blank=True, through='accounts.Follow', to='accounts.Profile'),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('from_user', 'to_user')},
        ),
    ]
