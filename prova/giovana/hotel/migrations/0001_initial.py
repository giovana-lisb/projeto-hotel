# Generated by Django 4.0.5 on 2022-06-22 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TidoEstadia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hospede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('Cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Estadia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(max_length=100)),
                ('data', models.DateField()),
                ('observacao', models.CharField(max_length=500)),
                ('Hospede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hospede')),
                ('Produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.produto')),
                ('TidoEstadia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.tidoestadia')),
            ],
        ),
    ]
