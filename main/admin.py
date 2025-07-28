from django.contrib import admin
from .models import HeroSection

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'projects_completed', 'years_experience', 'happy_clients')
