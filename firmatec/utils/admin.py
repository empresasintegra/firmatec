from django.contrib import admin

# Register your models here.
"""Utils Admin."""

# Django
# django-import-export
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
#Models
from utils.models import Region, Provincia, Ciudad, Cliente, Planta, Cargo, Departamento


class RegionSetResource(resources.ModelResource):

    class Meta:
        model = Region
        fields = ('id', 'nombre', 'status', )


class ProvinciaSetResource(resources.ModelResource):
    region = fields.Field(column_name='region', attribute='region', widget=ForeignKeyWidget(Region, 'nombre'))

    class Meta:
        model = Provincia
        fields = ('id', 'nombre', 'region', 'status', )


class CiudadSetResource(resources.ModelResource):
    provincia = fields.Field(column_name='provincia', attribute='provincia', widget=ForeignKeyWidget(Provincia, 'nombre'))

    class Meta:
        model = Ciudad
        fields = ('id', 'nombre', 'provincia', 'status', )


class ClienteSetResource(resources.ModelResource):

    class Meta:
        model = Cliente
        fields = ('id', 'codigo', 'rut', 'razon_social', 'ciudad', 'direccion_comercial', )


class PlantaSetResource(resources.ModelResource):
    cliente = fields.Field(column_name='cliente', attribute='cliente', widget=ForeignKeyWidget(Cliente, 'razon_social'))

    class Meta:
        model = Planta
        fields = ('id', 'codigo', 'nombre', 'cliente', 'ciudad', 'direccion_comercial', 'provincia', 'region', 'rut_representante', 'representante_legal')


class CargoSetResource(resources.ModelResource):

    class Meta:
        model = Cargo
        fields = ('id', 'nombre', 'status', )


class DepartamentoSetResource(resources.ModelResource):

    class Meta:
        model = Departamento
        fields = ('id', 'nombre', 'status', )


@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """RegionAdmin model admin."""

    resource_class = RegionSetResource
    fields = ('nombre', )
    list_display = ('id', 'nombre',)
    search_fields = ['nombre', ]


@admin.register(Provincia)
class ProvinciaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """ProvinciaAdmin model admin."""

    resource_class = ProvinciaSetResource
    fields = ('region', 'nombre', )
    list_display = ('id', 'nombre', 'region',)
    list_filter = ['region', ]
    search_fields = ('nombre', 'region__nombre')


@admin.register(Ciudad)
class CiudadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """CiudadAdmin model admin."""

    resource_class = CiudadSetResource
    fields = ('provincia', 'nombre', )
    list_display = ('id', 'nombre', 'provincia',)
    list_filter = ['provincia', ]
    search_fields = ('nombre', 'provincia__nombre')


@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """ClienteAdmin model admin."""

    resource_class = ClienteSetResource
    fields = ('codigo', 'rut', 'razon_social', 'region', 'provincia', 'ciudad', 'direccion_comercial', )
    list_display = ('id', 'rut', 'razon_social', 'ciudad', 'codigo',)
    search_fields = ['razon_social', ]


@admin.register(Planta)
class PlantaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """PlantaAdmin model admin."""

    resource_class = PlantaSetResource
    fields = ('codigo', 'cliente', 'nombre', 'region', 'provincia', 'ciudad', 'direccion_comercial', 'rut_representante', 'representante_legal', )
    list_display = ('id', 'nombre', 'cliente', 'ciudad', 'representante_legal', 'codigo')
    list_filter = ['cliente', ]
    search_fields = ('codigo', 'nombre', 'cliente__nombre')


@admin.register(Cargo)
class CargoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """CargoAdmin model admin."""

    resource_class = CargoSetResource
    fields = ('nombre', )
    list_display = ('id', 'nombre',)
    search_fields = ['nombre', ]


@admin.register(Departamento)
class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """DepartamentoAdmin model admin."""

    resource_class = DepartamentoSetResource
    fields = ('nombre', )
    list_display = ('id', 'nombre',)
    search_fields = ['nombre', ]

# admin.site.register(Region)
