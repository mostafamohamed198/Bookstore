from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(categories)
admin.site.register(books)
admin.site.register(chapters)
admin.site.register(rewards)
admin.site.register(comments)
admin.site.register(test)
admin.site.register(requests)
