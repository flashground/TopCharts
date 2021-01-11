from django.contrib import admin
from .models import Chart, Station


@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ('station','added_date','created_date')
    list_filter = ('station','added_date','created_date')
    list_select_related = ('station',)
    readonly_fields = ('added_date','created_date')
    fields = ('station','data', ('added_date','created_date','updated_date'))


class ChartAdminTabularInline(admin.TabularInline):
    model = Chart
    ordering = ['-added_date']
    readonly_fields = ('added_date','created_date')


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    inlines = [ChartAdminTabularInline,]
    list_display = ([field.name for field in Station._meta.get_fields()][1:])
    list_filter = ('active','created_date')
    list_editable = ('active',)
    ordering = ['id']
    readonly_fields = ('thumbnail_logo','created_date','updated_date')
    fieldsets = (
        (None, {
            'fields': (('name','active'),'description','slug')
        }),
        ('Datetime', {
            'fields': ('created_date','updated_date'),
        }),
        ('Images', {
            'fields': (('logo_path', 'thumbnail_logo'),),
        }),
    )