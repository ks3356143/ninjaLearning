# Generated by Django 4.1.7 on 2023-06-28 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ninjaapp', '0002_alter_project_language_alter_project_member_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='round',
            options={'ordering': ('-create_datetime',), 'verbose_name': '轮次信息', 'verbose_name_plural': '轮次信息'},
        ),
        migrations.AlterField(
            model_name='round',
            name='project',
            field=models.ForeignKey(db_constraint=False, help_text='归属项目', on_delete=django.db.models.deletion.CASCADE, related_name='pField', related_query_name='pQuery', to='ninjaapp.project', verbose_name='归属项目'),
        ),
    ]
