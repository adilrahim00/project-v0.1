from django.contrib import admin
from .models import Product

# Register the Product model in the admin panel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')  # Fields to display in the list view
    search_fields = ('name', 'category')  # Enable searching by name and category
    list_filter = ('category',)  # Filter products by category
    ordering = ('-created_at',)  # Order products by creation date (most recent first)

    # Optionally, customize the fields you want to be able to edit when adding/editing a product
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'category', 'image')
        }),
    )

    # Allow the image to be displayed in the admin panel with a specific size
    def image_preview(self, obj):
        return f'<img src="{obj.image.url}" width="100" height="100" />'
    image_preview.allow_tags = True
    image_preview.short_description = 'Image'

