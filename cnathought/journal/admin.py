from django.contrib import admin

# Register your models here.

from .models import Thought, Profile

admin.site.register(Thought)

admin.site.register(Profile)