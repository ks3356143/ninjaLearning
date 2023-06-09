# Generated by Django 4.1.7 on 2023-06-28 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ninjaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.JSONField(blank=True, default=[], help_text='被测语言', null=True, verbose_name='被测语言'),
        ),
        migrations.AlterField(
            model_name='project',
            name='member',
            field=models.JSONField(blank=True, default=[], help_text='项目成员', null=True, verbose_name='项目成员'),
        ),
        migrations.AlterField(
            model_name='project',
            name='standard',
            field=models.JSONField(blank=True, default=[], help_text='依据标准', null=True, verbose_name='依据标准'),
        ),
        migrations.AlterField(
            model_name='project',
            name='test_level',
            field=models.JSONField(blank=True, default=[], help_text='测试级别', null=True, verbose_name='测试级别'),
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(help_text='Id', primary_key=True, serialize=False, verbose_name='Id')),
                ('remark', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('update_datetime', models.DateField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('sort', models.IntegerField(blank=True, default=1, help_text='显示排序', null=True, verbose_name='显示排序')),
                ('ident', models.CharField(blank=True, help_text='轮次标识', max_length=64, null=True, verbose_name='轮次标识')),
                ('name', models.CharField(blank=True, help_text='轮次名称', max_length=64, null=True, verbose_name='轮次名称')),
                ('beginTime', models.DateField(auto_now_add=True, help_text='开始时间', null=True, verbose_name='开始时间')),
                ('endTime', models.DateField(auto_now_add=True, help_text='结束时间', null=True, verbose_name='结束时间')),
                ('speedGrade', models.CharField(blank=True, help_text='速度等级', max_length=64, null=True, verbose_name='速度等级')),
                ('package', models.CharField(blank=True, help_text='封装', max_length=64, null=True, verbose_name='封装')),
                ('grade', models.CharField(blank=True, help_text='等级', max_length=64, null=True, verbose_name='等级')),
                ('best_condition_voltage', models.CharField(blank=True, help_text='最优工况电压', max_length=64, null=True, verbose_name='最优工况电压')),
                ('best_condition_tem', models.CharField(blank=True, help_text='最优工况温度', max_length=64, null=True, verbose_name='最优工况温度')),
                ('typical_condition_voltage', models.CharField(blank=True, help_text='典型工况电压', max_length=64, null=True, verbose_name='典型工况电压')),
                ('typical_condition_tem', models.CharField(blank=True, help_text='典型工况温度', max_length=64, null=True, verbose_name='典型工况温度')),
                ('low_condition_voltage', models.CharField(blank=True, help_text='最低工况电压', max_length=64, null=True, verbose_name='最低工况电压')),
                ('low_condition_tem', models.CharField(blank=True, help_text='最低工况温度', max_length=64, null=True, verbose_name='最低工况温度')),
                ('level', models.CharField(default='0', help_text='树状级别第一级', max_length=15, verbose_name='树状级别第一级')),
                ('key', models.CharField(help_text='给前端的树状级别', max_length=15, verbose_name='给前端的树状级别')),
                ('title', models.CharField(help_text='给前端的name', max_length=15, verbose_name='给前端的name')),
                ('project', models.ForeignKey(db_constraint=False, help_text='归属项目', on_delete=django.db.models.deletion.CASCADE, related_name='pField', to='ninjaapp.project', verbose_name='归属项目')),
            ],
            options={
                'verbose_name': '核心模型',
                'verbose_name_plural': '核心模型',
                'abstract': False,
            },
        ),
    ]
