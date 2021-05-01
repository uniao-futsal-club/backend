from django.contrib import admin
from .models import Team, Training, Contract

# Register your models here.
admin.site.register(Team)
admin.site.register(Training)
admin.site.register(Contract)
