from django.contrib import admin

from .models import Note, Paper

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "name", "date")

# Register your models here.
admin.site.register(Note, NoteAdmin)
admin.site.register(Paper)
