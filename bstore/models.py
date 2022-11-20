from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class categories(models.Model):
    category = models.CharField(max_length=10)

class rewards(models.Model):
    rewardname = models.CharField(max_length=20)
    rewardimage = models.ImageField(upload_to='reward/', blank=True)


class books(models.Model):
    bookuser= models.ForeignKey('User', on_delete=models.CASCADE,  default= None, blank=True)
    name = models.CharField(max_length=80)
    slogan = models.CharField(max_length=200, null=True, default = None)
    cover = models.ImageField(upload_to='cover/', blank=True)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    authorname= models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    wordbyauthor = models.CharField(max_length=500)
    bookcategory=models.ForeignKey('categories',  related_name="bookcategory", default=None, blank=True, null=True, on_delete= models.CASCADE)
    authorimage = models.ImageField(upload_to='author/', default= None, blank=True)
    quantity=models.IntegerField(default=0)
    quote1 = models.CharField(max_length=100, blank=True, default=None, null=True)
    quote2 = models.CharField(max_length=100, blank=True, default=None, null=True)
    quote3 = models.CharField(max_length=100, blank=True, default=None, null=True)
    addtocart = models.ManyToManyField('User', default=None, blank=True, related_name='addd')
    bookrewards = models.ManyToManyField('rewards', default=None, null=True, blank=True)


class chapters(models.Model):
    chapterbook = models.ForeignKey('books', on_delete=models.CASCADE,  default= None)
    chapternumber = models.IntegerField()
    chapterdescription = models.CharField(max_length=260)



class comments(models.Model): 
    comment =  models.CharField(max_length= 100)
    commentuser = models.ForeignKey('User', on_delete=models.CASCADE, default=None)
    commentbook = models.ForeignKey('books', on_delete=models.CASCADE, default=None)

    def serialize(self):
        return {
            'comment': self.comment,
            'commentuser': self.commentuser,
            'commentbook': self.commentbook
        }

class test(models.Model):
    first = models.CharField(max_length=100)
    second = models.IntegerField()

    def serialize(self):
        return {
            'first': self.first,
            'second': self.second
        }

class requests (models.Model):
    requestedbooks = models.ManyToManyField('books',  default= None)
    requesteduser = models.ForeignKey('User', on_delete=models.CASCADE,default=None)
    requestaddress = models.CharField(max_length=500, default=None)
    requestphone = models.IntegerField(default=None)
    requestdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    finished = models.BooleanField(default=False)