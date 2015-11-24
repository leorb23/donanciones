from django.db import models

# Create your models here.

class EstadoJugueteManager(models.Manager):
	def create_object(self, descripcion):
		objeto = self.create(descripcion=descripcion)
		return objeto

class EstadoJuguete(models.Model):
	descripcion = models.CharField(unique=True, max_length=100, null=False)
	objects = EstadoJugueteManager()

	def __str__(self):
		return self.descripcion

class DonanteManager(models.Manager):
	def create_object(self, apellidos, identificacion, nombres):
		objeto = self.create(apellidos=apellidos, identificacion=identificacion, nombres=nombres)
		return objeto

class Donante(models.Model):
	apellidos = models.CharField(max_length=150, null=False)
	identificacion = models.CharField(unique=True, max_length=15, null=False)
	nombres = models.CharField(max_length=150, null=False)
	objects = DonanteManager()

	def __str__(self):
		return self.nombres + " " + self.apellidos

class JugueteManager(models.Manager):
	def create_object(self, descripcion, estado, imagen):
		objeto = self.create(descripcion=descripcion, estado=estado, imagen=imagen)
		return objeto

class Juguete(models.Model):
	descripcion = models.TextField(null=False)
	estado = models.ForeignKey(EstadoJuguete)
	imagen = models.ImageField(upload_to='juguetes/', null=True)
	objects = JugueteManager()

	def __str__(self):
		return self.descripcion

class DonacionManager(models.Manager):
	def create_object(self, donante, juguete):
		objeto = self.create(donante=donante, juguete=juguete)
		return objeto

class Donacion(models.Model):
	donante = models.ForeignKey(Donante)
	fecha = models.DateTimeField(auto_now=True)
	juguete = models.ForeignKey(Juguete)
	objects = DonacionManager()