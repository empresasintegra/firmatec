from django.db import models

# Create your models here.
# Crum User
from crum import get_current_user
from smart_selects.db_fields import GroupedForeignKey


class BaseModel(models.Model):
    """Project base model.

    BaseModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + created_by (User Model): Store the user to created the object.
        + modified (DateTime): Store the last datetime the object was modified.
        + madified_by (User Model): Store the user to modified the object.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on  which the object was created.'
    )
    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_created_by",
        blank=True,
        null=True,
        default=None
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on  which the object was last modified.'
    )
    modified_by = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_modified_by",
        blank=True,
        null=True,
        default=None
    )

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']


class Region(models.Model):
    """Modelo Region.
    """


    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    """Modelo Provincia.
    """

    
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    """Modelo Ciudad.
    """


    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    """Modelo Cliente. """

    codigo = models.CharField(
        'código',
        help_text='Identificador único de sistema de gestión.',
        max_length=6,
        unique=True,
        blank=True,
        null=True
    )
    rut = models.CharField(
        max_length=12,
        unique=True,
        error_messages={
            'unique': 'Ya existe un cliente con este RUT registrado.'
        }
    )
    razon_social = models.CharField(max_length=80)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True) 
    provincia = GroupedForeignKey(Provincia, "region", on_delete=models.SET_NULL, null=True, blank=True)
    ciudad = GroupedForeignKey(Ciudad, "provincia", null=True, blank=True)
    # region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    # provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True, blank=True)
    # ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True, blank=True)
    direccion_comercial = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.razon_social


class Planta(models.Model):
    """Modelo Planta.
    """

    codigo = models.CharField(
        'código',
        help_text='Identificador único de sistema de gestión.',
        max_length=6,
        unique=True,
        blank=True,
        null=True
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True) 
    provincia = GroupedForeignKey(Provincia, "region", null=True, blank=True)
    ciudad = GroupedForeignKey(Ciudad, "provincia", null=True, blank=True)
    direccion_comercial = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    rut_representante = models.CharField(
        max_length=12,
        null=True,
        blank=True
    )
    representante_legal = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Cargo(models.Model):
    """Modelo Cargo.
    """

    nombre = models.CharField(
        max_length=120,
        unique=True
    )
    status = models.BooleanField(
        default=True,
        help_text='Para desactivar este cargo, deshabilite esta casilla.'
    )

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    """Modelo Departamento.
    """

    nombre = models.CharField(
        max_length=120,
        unique=True
    )
    status = models.BooleanField(
        default=True,
        help_text='Para desactivar este departamento, deshabilite esta casilla.'
    )

    def __str__(self):
        return self.nombre
