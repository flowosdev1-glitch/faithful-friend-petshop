from django.contrib import admin
from .models import Category, Product, Service, AppointmentRequest, ContactMessage

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Service)

@admin.register(AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'owner_name', 'service', 'preferred_date', 'preferred_time', 'status')
    list_filter = ('status', 'preferred_date', 'service')
    search_fields = ('pet_name', 'owner_name', 'email', 'phone')

admin.site.register(ContactMessage)