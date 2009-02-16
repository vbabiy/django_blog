from django.contrib import admin
from django_blog.blog.models import Post, Category, Tag

def tags(obj):
    return ", ".join([x.name for x in obj.tags.all()])

def categories(obj):
    return ", ".join([c.name for c in obj.categories.all()])

def author(obj):
    return obj.author.get_full_name()

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }
    date_hierarchy = 'date_published'
    list_display = ('title', 'status', author , 'date_created', 'date_modified', 'date_published', tags, categories)
    list_filter = ('status', 'tags', 'categories')
    search_fields = ('title', 'body')
    exclude = ('author',)
    
    def save_model(self, request, obj, *args, **kargs):
        obj.author = request.user;
        super(PostAdmin, self).save_model(request, obj, *args, **kargs)
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

