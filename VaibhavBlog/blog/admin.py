from django.contrib import admin
from .models import Post, Category


# Register your models here.

# for configurations of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'discription', 'url', 'add_date',)
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','content','url','cat')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)

    # https: // cdn.tiny.cloud / 1 / YOUR_API_KEY / tinymce / 5 / tinymce.min.js
    # class Media:
    #     js =('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/script.js',)
admin.site.register(Post,PostAdmin)
admin.site.register(Category, CategoryAdmin)
