from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand_id = models.IntegerField()
    status = models.CharField(max_length=50, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.supplier_name

class Purchase(models.Model):
    invoice_no = models.CharField(max_length=50, unique=True)
    invoice_date = models.DateTimeField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_no

class Sale(models.Model):
    invoice_no = models.CharField(max_length=50, unique=True)
    invoice_date = models.DateTimeField()
    customer_name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    totalamount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_no



class PurchaseDetail(models.Model):
    purchase_master = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.status

class SaleDetail(models.Model):
    sale_master = models.ForeignKey(Sale, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.amount
