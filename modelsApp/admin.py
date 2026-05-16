from django.contrib import admin
from .models import Reader, Book, Product, Project, Sale, Seller, Task, Customer

# admin.site.register(Reader)
# admin.site.register(Book)

# class TaskInline(admin.TabularInline):
#     model = Task
#     extra = 1
#     fileds = ('name', 'description', 'progress')

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'description', 'created_at', 'updated_at', 'imagePath')
#     search_fields = ('name', 'description')
#     list_filter = ('created_at', 'updated_at')

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'created_at', 'updated_at')
#     inlines = [TaskInline]

#     def display_progress(self, obj):
#         return f"{obj.progress}%"

# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('project', 'name', 'description', 'progress')
#     search_fields = ('name', 'description')
#     list_filter = ('project',)



admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Sale)   