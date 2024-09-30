from django.contrib import admin
from .models import Mot

@admin.register(Mot)
class MotAdmin(admin.ModelAdmin):
    list_display = ('mot_sar', 'mot_fr', 'type_mot')
    search_fields = ('mot_sar', 'mot_fr', 'type_mot')

# Register the model to be managed in the admin interface
