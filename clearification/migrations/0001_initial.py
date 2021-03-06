# Generated by Django 2.1.7 on 2019-06-29 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contest', '0006_auto_20181121_1906'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='clearifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declare_time', models.DateTimeField(auto_now_add=True)),
                ('clearification_text', models.TextField(max_length=1000)),
                ('judge_ignored', models.BooleanField(default=False)),
                ('judge_answer', models.TextField(default='', max_length=4000)),
                ('associated_contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.contest')),
                ('associated_problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.contest_problemset')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
