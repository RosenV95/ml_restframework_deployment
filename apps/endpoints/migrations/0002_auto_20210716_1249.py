# Generated by Django 3.1.7 on 2021-07-16 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlalgorithmstatus',
            name='parent_mlalgorithm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='endpoints.mlalgorithm'),
        ),
        migrations.CreateModel(
            name='ABTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('created_by', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('summary', models.CharField(blank=True, max_length=10000, null=True)),
                ('parent_mlalgorithm_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_mlaglorithm_1', to='endpoints.mlalgorithm')),
                ('parent_mlalgorithm_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_mlaglorithm_2', to='endpoints.mlalgorithm')),
            ],
        ),
    ]
