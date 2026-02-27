from django.db import models #the ORM

# Create your models here.

class Department(models.Model): #table department
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model): #table course
    dept = models.ForeignKey(Department, on_delete=models.CASCADE) #attibute = dept (foreign key of Department table)
    title = models.CharField(max_length=100) #attribute2(char with the length of 100 chars)

    def __str__(self): #This is needed for printing objects/rows of this table 
        return self.title

class Account(models.Model): #table account
    name = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, unique=True)
    admin_status = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('checked_out', 'Checked Out'),
        ('abandoned', 'Abandoned'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} for {self.account.name}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    item_quantity = models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together = ('cart', 'product')

    def __str__(self): return f"{self.product.name} ({self.item_quantity})"