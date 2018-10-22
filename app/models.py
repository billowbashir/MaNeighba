from django.db import models
from django.contrib.auth.models import User

class Neighbourhood(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    population=models.IntegerField()
    admin=models.ForeignKey(User,on_delete=models.CASCADE)

# create_neigborhood()
# delete_neigborhood()
# find_neigborhood(neigborhood_id)
# update_neighborhood()
# update_occupants()


class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='profile_photos/')
    bio=models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)



class Business(models.Model):
    name=models.CharField(max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email=models.EmailField()


# create_business()
# delete_business()
# find_business(business_id)
# update_business()
