from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """
    Base class that includes all the things we want for every model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Wishlist(BaseModel):
    """
    Model representing a list
    """
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=32)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ListItem(BaseModel):
    """
    Model representing an item in a list
    """
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name="list_items")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Upvote(BaseModel):
    """
    Model representing an upvote
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list_item = models.ForeignKey(ListItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.id}:{self.list_item.id}" 