from django.db import models
from datetime import datetime

# Created models here.
class Tg_user(models.Model):
    name = models.CharField (max_length=60)
    tg_id = models.CharField(max_length=60)
    is_in_crm = models.BooleanField(default=False)
    def __str__(self):
        return self.name + " tg id:" + self.tg_id

class Offer(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    deadline = models.DateTimeField()
    customer = models.ForeignKey(Tg_user,on_delete=models.PROTECT)
    #TODO status = models.Choices прописать статусы
    def __str__(self):
        return self.title

class Conversation(models.Model):
    title = models.CharField(max_length=100)
    dev_chat_id = models.CharField(max_length=100)
    cus_chat_id = models.CharField(max_length=100)
    developer = models.ForeignKey(Tg_user,on_delete=models.PROTECT)
    customer = models.ForeignKey(Tg_user,on_delete=models.PROTECT,related_name='customer')
    offer = models.ForeignKey(Offer,on_delete=models.PROTECT)
    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now=True)
    offer = models.ForeignKey(Offer,on_delete=models.PROTECT)
    developer = models.ForeignKey(Tg_user,on_delete=models.PROTECT)
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField (max_length=60)
    developers = models.ManyToManyField(Tg_user)
    manager = models.ForeignKey(Tg_user,on_delete=models.PROTECT,related_name='manager')
    tasks = models.ManyToManyField(Task)
    def __str__(self):
        return self.title

class Template(models.Model):
    text = models.CharField (max_length=60)
    manager = models.ForeignKey(Tg_user,on_delete=models.PROTECT)
    def __str__(self):
        return self.title

class Message(models.Model):
    created = models.DateTimeField(auto_now=True)
    text = models.CharField (max_length=60)
    from_name = models.CharField (max_length=60)
    from_id = models.CharField(max_length=60)
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField (max_length=60)
    project = models.ForeignKey(Project,on_delete=models.PROTECT)
    def __str__(self):
        return self.title

class Event(models.Model):
    type = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now=True)
    cheaked = models.BooleanField(default=False)
    from_who = models.CharField(max_length=60)

    def __str__(self):
        return self.title






