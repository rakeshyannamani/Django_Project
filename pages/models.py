from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title


class Customer(models.Model):
    customer_name = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name


class Product(models.Model):
    product_name = models.CharField(max_length=20)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_num = models.CharField(max_length=20)
    order_date = models.DateTimeField('Order Received')
    order_value = models.IntegerField(blank=True, null=True)
    invoice_date = models.DateTimeField('Invoice Raised')
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name = models.ManyToManyField(Product)

    def __str__(self):
        return self.order_num
