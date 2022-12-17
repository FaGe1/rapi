from django.contrib import admin
from .models import *

myModels = [
    Project,
    Offer,
    Tg_user,
    Conversation,
    Task,
    Service
    ]
admin.site.register(myModels)
