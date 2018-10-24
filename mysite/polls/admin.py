from django.contrib import admin
from django.utils.html import format_html

from .models import CollectionsMaster, MerchantMaster, DealsAudit, DealsCollections


class CollectionMasterAdmin(admin.ModelAdmin):
    list_display = ['title', 'small_img_url', 'header', 'status']
    list_filter = ['publish_date', 'title']
    # fields = [('title', 'header_subtitle','is_header'), ('updated_at', 'small_img_url')]
    # fieldsets = (
    #     ('Title Change Section', {
    #         'fields': ('title', 'header_subtitle')
    #     }),
    #     ('Small Image Section',{
    #         'fields': ('small_img_url', 'is_header')
    #     })
    # )

    #show

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.small_img_url.url))

    # image_tag.short_description = 'Image'

    # list_display= ['image_tag']

    search_fields = ('title', 'publish_date')

    #Show icon in header
    def header(self, obj):
        return obj.is_header > 0
    
    header.boolean= True


    #Adding Actions to the Master
    actions = ["Change_Status_to_False", "Change_Status_to_True"]

    def Change_Status_to_False(self, request, queryset):
        queryset.update(status=False)

    def Change_Status_to_True(self, request, queryset):
        queryset.update(status=True)




class DealsCollectionsAdmin(admin.ModelAdmin):
    list_display = ("deal_id", "collection_id")

class MerchantMasterAdmin(admin.ModelAdmin):
    list_display = ('merchant_id', 'merchant_name')

class DealsAuditAdmin(admin.ModelAdmin):
    list_display = ('audit_id', 'deal_id')


admin.site.register(CollectionsMaster, CollectionMasterAdmin)
admin.site.register(MerchantMaster, MerchantMasterAdmin)
admin.site.register(DealsAudit, DealsAuditAdmin)
admin.site.register(DealsCollections, DealsCollectionsAdmin)
