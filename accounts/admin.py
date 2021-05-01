from django.contrib import admin
from .models import User, Player, Coach, Skills
# Register your models here.
admin.site.register(User)
admin.site.register(Coach)
admin.site.register(Player)
admin.site.register(Skills)
