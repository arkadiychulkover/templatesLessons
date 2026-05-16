from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imagePath = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name} - ${self.price} - {self.description} - Created at: {self.created_at} - Updated at: {self.updated_at} - Image Path: {self.imagePath}"
     

    class Meta:
        db_table = 'dj_product2'

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Seller(models.Model):

    class PositionChoices(models.TextChoices):
        SELLER = "seller", "Продавець"
        HEAD_SELLER = "head_seller", "Головний продавець"
        SALES_MANAGER = "sales_manager", "Керівник відділу продажів"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()
    position = models.CharField(
        max_length=20,
        choices=PositionChoices.choices
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()

#     def __str__(self):
#         return self.name


class Sale(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="sales"
    )
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name="sales"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="sales"
    )
    sale_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Продаж #{self.id}"