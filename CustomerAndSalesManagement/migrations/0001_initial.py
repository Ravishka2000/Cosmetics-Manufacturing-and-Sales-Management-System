# Generated by Django 4.1.1 on 2022-09-22 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EmployeeManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('username', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile_number', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=200, null=True)),
                ('order_status', models.CharField(blank=True, choices=[('Order confirmed', 'Order confirmed'), ('Packaging up the order', 'Packaging up the order'), ('Order shipped', 'Order shipped'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], default='Order confirmed', max_length=50, null=True)),
                ('net_total', models.FloatField(null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CustomerAndSalesManagement.customer')),
            ],
        ),
        migrations.CreateModel(
            name='SalesProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('selling_price', models.FloatField(null=True)),
                ('production_price', models.FloatField(null=True)),
                ('retail_price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('', 'Select a category..'), ('S', 'Skin Cosmetic'), ('N', 'Nail Cosmetic'), ('H', 'Hair Cosmetic'), ('O', 'Other Categories')], max_length=1, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('product_image', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('vote_total', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_ratio', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SalesTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200, null=True)),
                ('team_description', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
                ('no_of_employees', models.IntegerField(default=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(choices=[('Western Province', 'Western Province'), ('Southern Province', 'Southern Province'), ('Eastern Province', 'Eastern Province'), ('Central Province', 'Central Province'), ('Northcentral Province', 'Northcentral Province'), ('Northern Province', 'Northern Province'), ('Northwest Province', 'Northwest Province'), ('Uwa Province', 'Uwa Province')], max_length=200, null=True)),
                ('zipcode', models.CharField(max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CustomerAndSalesManagement.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CustomerAndSalesManagement.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CustomerAndSalesManagement.salesproduct')),
            ],
        ),
        migrations.CreateModel(
            name='SalesTeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CustomerAndSalesManagement.salesteam')),
                ('team_member', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EmployeeManagement.employees')),
            ],
        ),
        migrations.CreateModel(
            name='SalesTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200, null=True)),
                ('task_description', models.CharField(max_length=200, null=True)),
                ('progress', models.IntegerField(blank=True, default=0, null=True)),
                ('task_status', models.CharField(choices=[('Assigned', 'Assigned'), ('Status Pending', 'Task Pending'), ('Task Completed', 'Task Completed')], default='Assigned', max_length=20, null=True)),
                ('sales_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CustomerAndSalesManagement.salesteam')),
            ],
        ),
        migrations.AddField(
            model_name='salesproduct',
            name='tags',
            field=models.ManyToManyField(null=True, to='CustomerAndSalesManagement.tag'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CustomerAndSalesManagement.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CustomerAndSalesManagement.salesproduct')),
            ],
        ),
        migrations.CreateModel(
            name='BulkOrderRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('mobile_number', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('street_address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('province', models.CharField(choices=[('Western Province', 'Western Province'), ('Southern Province', 'Southern Province'), ('Eastern Province', 'Eastern Province'), ('Central Province', 'Central Province'), ('Northcentral Province', 'Northcentral Province'), ('Northern Province', 'Northern Province'), ('Northwest Province', 'Northwest Province'), ('Uwa Province', 'Uwa Province')], max_length=200, null=True)),
                ('zip_code', models.IntegerField(null=True)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('request_status', models.CharField(max_length=20, null=True)),
                ('customer_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CustomerAndSalesManagement.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_review', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CustomerAndSalesManagement.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerAndSalesManagement.salesproduct')),
            ],
            options={
                'unique_together': {('customer', 'product')},
            },
        ),
    ]
