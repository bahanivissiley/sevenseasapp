from django.contrib import admin
from main.models import Therapist, ContactMessage

# Register your models here.
from .models import Questionnaire

admin.site.register(Questionnaire)

@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone')  # Colonnes visibles dans la liste
    list_filter = ('specialization',)  # Filtres sur la droite
    search_fields = ('name', 'specialization')  # Barre de recherche

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email')


admin.site.site_header = "Gestion du site SevenSeas"
admin.site.site_title = "Admin | SecenSeas"
admin.site.index_title = "Bienvenue sur le panneau d'administration"
