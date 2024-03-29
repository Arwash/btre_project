from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
class listing (models.Model):
    realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
    #above field is to connect the listing with its realtor which has its own model/table in the database. We connect them using the  foreign key
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/') # this 'photos/%y/%m/%d/ will save the uploaded photos to this location inside the media folder, since any media in Django goes to the media folder.
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True) 
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True) 
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True) 
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True) 
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True) 
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default = datetime.now , blank = True)
    def __str__(self):
        return self.title
