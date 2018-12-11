# superuser: root 123123...

from django.contrib import admin
from df_goods.models import TypeInfo,GoodsInfo

# Register your models here.
# 注册模型类  普通方法
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']
    list_per_page = 10
    search_fields = ['ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'gtitle', 'gunit', 'gclick', 'gprice', 'gpic', 'gkucun', 'gcontent', 'gjianjie']
    list_filter = ['gtitle']
    list_editable = ['gtitle', 'gkucun', 'gcontent', 'gjianjie']
    readonly_fields = ['gclick']
    search_fields = ['gtitle', 'gcontent', 'gjianjie']

admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)

