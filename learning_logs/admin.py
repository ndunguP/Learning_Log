from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Topic, Entry
from .models import Topic
admin.site.register(Topic)
admin.site.register(Entry)
