# Generated by Django 3.2.1 on 2022-02-26 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artical',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('a_title', models.CharField(max_length=300)),
                ('a_auth_name', models.CharField(blank=True, default='无名', max_length=50, null=True)),
                ('a_publish_date', models.DateField()),
                ('a_publish_time', models.TimeField()),
                ('a_content', mdeditor.fields.MDTextField(default='', verbose_name='文章内容')),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'artical',
                'ordering': ['-a_publish_date', '-a_id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'topic',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField(verbose_name='评论内容')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='index.artical', verbose_name='评论文章')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
                ('pre_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='index.comment', verbose_name='父评论id')),
            ],
            options={
                'verbose_name_plural': 'comment',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Categroy',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=50)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.topic')),
            ],
            options={
                'db_table': 'categroy',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='artical',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.categroy'),
        ),
    ]
