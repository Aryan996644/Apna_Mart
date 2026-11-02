from django.contrib import admin
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, \
ProductImages, ProductReview, Wishlist, Address, ContactUs

class ProductImagesAdmin(admin.TabularInline):
	model = ProductImages

class ProductAdmin(admin.ModelAdmin):
	inlines = [ProductImagesAdmin]
	list_display = ['user', 'title', 'product_image', 'price','category', 'vendor', 'featured', 'product_status', 'pid']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'category_image', 'cid']

class VendorAdmin(admin.ModelAdmin):
	list_display = ['title', 'vendor_image', 'vid']

class CartOrderItemsInline(admin.TabularInline):
	model = CartOrderItems
	extra = 0
	readonly_fields = ['order_img', 'item', 'qty', 'price', 'total', 'invoice_no']

class CartOrderAdmin(admin.ModelAdmin):
	inlines = [CartOrderItemsInline]
	list_display = ['oid', 'user', 'full_name', 'phone', 'price', 'paid_status', 'product_status', 'payment_method', 'order_date']
	list_editable = ['paid_status', 'product_status']
	list_filter = ['paid_status', 'product_status', 'payment_method', 'order_date']
	search_fields = ['oid', 'full_name', 'email', 'phone', 'address']

class CartOrderItemsAdmin(admin.ModelAdmin):
	list_display = ['order', 'invoice_no', 'item', 'order_img', 'qty', 'price', 'total']

class ProductReviewAdmin(admin.ModelAdmin):
	list_display = ['user', 'product', 'rating', 'review', 'date']
	list_filter = ['rating', 'date']
	search_fields = ['user__username', 'product__title', 'review']

class WishlistAdmin(admin.ModelAdmin):
	list_display = ['user', 'product', 'date']

class ContactUsAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'message']
	search_fields = ['name', 'email', 'message']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(ContactUs, ContactUsAdmin)

