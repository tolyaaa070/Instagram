from django.contrib import admin
from .models import (UserProfile, Post,
                     PostLike, Save,
                     SaveItem, Comment,
                     CommentLike, Follow, Story)
from modeltranslation.admin import TranslationAdmin

@admin.register(UserProfile , Post)
class UserProfileAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(PostLike)
admin.site.register(Save)
admin.site.register(SaveItem)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(Follow)
admin.site.register(Story)


