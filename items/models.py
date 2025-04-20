from django.db import models

class Item(models.Model):
    itemID    = models.AutoField(primary_key=True)
    itemName  = models.CharField(max_length=100)
    day       = models.IntegerField()
    month     = models.IntegerField()
    year      = models.IntegerField()

    def __str__(self):
        return f"{self.itemName} ({self.itemID})"
