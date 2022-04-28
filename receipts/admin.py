from django.contrib import admin
from .models import Receipt

# Register your models here.

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'image')
    search_fields = ['id']
    list_filter = ('created_at', )

admin.site.register(Receipt, ReceiptAdmin)