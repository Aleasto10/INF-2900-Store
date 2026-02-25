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

class Cart(models.Model):
    #id #INTEGER PRIMARY KEY AUTOINCREMENT
    account = models.ForeignKey( #INTEGER NOT NULL #FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
        'Accounts',
        on_delete=models.CASCADE
    )

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('checked_out', 'Checked Out'),
        ('abandoned', 'Abandoned'),
    ]
    status = models.CharField( #TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'checked_out', 'abandoned'))
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    time_created = models.DateTimeField(auto_now_add=True) #TEXT NOT NULL DEFAULT (datetime('now'))

    def __str__(self):
        return f"Cart {self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey( #INTEGER NOT NULL FOREIGN KEY (cart_id) REFERENCES carts(id) ON DELETE CASCADE
        Cart,
        related_name="items",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey( #INTEGER NOT NULL FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
        Product,
        on_delete=models.RESTRICT
    )
    item_quantity = models.PositiveIntegerField(default=1) #INTEGER NOT NULL DEFAULT 0 CHECK (item_quantity >= 0)
    
    class Meta: #PRIMARY KEY (cart_id, product_id)
        unique_together = ('cart', 'product')

    def __str__(self):
        return f"{self.product.name} ({self.item_quantity})"