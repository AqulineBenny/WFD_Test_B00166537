from django.db import models

class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    manufacturer_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    
    def __str__(self):
        return self.manufacturer_name

class CarModel(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    body_style = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    engine_size = models.DecimalField(max_digits=4, decimal_places=1)
    
    def __str__(self):
        return self.model_name

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    vin = models.CharField(max_length=17, unique=True)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.vin} - {self.car_model.model_name}"

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Sale {self.sale_id} - {self.car}"

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service_date = models.DateField()
    service_type = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"Service {self.service_id} - {self.car}"