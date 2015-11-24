from django.contrib import auth
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from juguetes.models import Donacion, Donante, EstadoJuguete, Juguete

# Create your views here.

def index(request):
	plantilla = "index.html"
	return render(request, plantilla)

def cliente(request):
	plantilla = "cliente.html"
	return render(request, plantilla)

def log_in(request):
	plantilla = "login.html"
	return render(request, plantilla)

def log_out(request):
	if request.user.is_authenticated():
		auth.logout(request)
	return HttpResponseRedirect('/')

def donacion(request, id):
	if request.user.is_authenticated() and request.user.is_superuser:
		msj = ""
		objeto = Donacion.objects.get(id=id)
		if request.method == 'POST':
			apellidos = request.POST['apellidos']
			identificacion = request.POST['identificacion']
			nombres = request.POST['nombres']
			donante = objeto.donante
			if donante.identificacion != identificacion:
				donante = Donante.objects.filter(identificacion=identificacion)
				if donante:
					donante = Donante.objects.get(identificacion=identificacion)
					donante.apellidos = apellidos
					donante.nombres = nombres
				else:
					donante = Donante.objects.create_object(apellidos, identificacion, nombres)
			else:
				donante.apellidos = apellidos
				donante.nombres = nombres
			donante.save()
			descripcion = request.POST['descripcion']
			juguete = objeto.juguete
			juguete.descripcion = request.POST['descripcion']
			juguete.estado = EstadoJuguete.objects.get(id=request.POST['estado'])
			if request.FILES.get('imagen', ''):
				juguete.imagen = request.FILES['imagen']
			juguete.save()
			donacion = objeto
			donacion.donante = donante
			donacion.juguete = juguete
			donacion.save()
			msj = "Donación modificada"
		estados = EstadoJuguete.objects.all()
		plantilla = "donacion.html"
		return render(request, plantilla, {'objeto':objeto, 'estados':estados, 'msj':msj})
	else:
		return HttpResponseRedirect('/')

def donaciones(request):
	if request.user.is_authenticated() and request.user.is_superuser:
		plantilla = "donaciones.html"
		lista = Donacion.objects.all()
		return render(request, plantilla, {'lista':lista})
	else:
		return HttpResponseRedirect('/')

def donacion_eliminar(request, id):
	if request.user.is_authenticated() and request.user.is_superuser:
		if request.method == 'POST':
			objeto = Donacion.objects.get(id=id)
			objeto.delete()
		return HttpResponseRedirect("/donacion/listado")
	else:
		return HttpResponseRedirect('/')

def donacion_nuevo(request):
	if request.user.is_authenticated():
		msj = ""
		if request.method == 'POST':
			apellidos = request.POST['apellidos']
			identificacion = request.POST['identificacion']
			nombres = request.POST['nombres']
			donante = Donante.objects.filter(identificacion=identificacion)
			if donante:
				donante = Donante.objects.get(identificacion=identificacion)
				donante.apellidos = apellidos
				donante.nombres = nombres
			else:
				donante = Donante.objects.create_object(apellidos, identificacion, nombres)
			donante.save()
			descripcion = request.POST['descripcion']
			estado = EstadoJuguete.objects.get(id=request.POST['estado'])
			imagen = None
			if request.FILES.get('imagen', ''):
				imagen = request.FILES['imagen']
			juguete = Juguete.objects.create_object(descripcion, estado, imagen)
			juguete.save()
			donacion = Donacion.objects.create_object(donante, juguete)
			donacion.save()
			msj = "Donación guardada"
		estados = EstadoJuguete.objects.all()
		plantilla = "donacion_nuevo.html"
		return render(request, plantilla, {'estados':estados, 'msj':msj})
	else:
		return HttpResponseRedirect('/')

def donante(request, id):
	if request.user.is_authenticated() and request.user.is_superuser:
		msj = ""
		objeto = Donante.objects.get(id=id)
		if request.method == 'POST':
			identificacion = request.POST['identificacion']
			if objeto.identificacion != identificacion:
				model = Donante.objects.filter(identificacion=identificacion)
			if model:
				msj = "Existe donante con la identificación ingresada"
			else:
				model = objeto
				model.apellidos = request.POST['apellidos']
				model.nombres = request.POST['nombres']
				model.identificacion = identificacion
				model.save()
				msj = "Donante modificado"
		plantilla = "donante.html"
		return render(request, plantilla, {'objeto':objeto, 'msj':msj})
	else:
		return HttpResponseRedirect('/')

def donantes(request):
	if request.user.is_authenticated() and request.user.is_superuser:
		plantilla = "donantes.html"
		lista = Donante.objects.all()
		return render(request, plantilla, {'lista':lista})
	else:
		return HttpResponseRedirect('/')

def donante_eliminar(request, id):
	if request.user.is_authenticated() and request.user.is_superuser:
		if request.method == 'POST':
			objeto = Donante.objects.get(id=id)
			objeto.delete()
		return HttpResponseRedirect("/donante/listado")
	else:
		return HttpResponseRedirect('/')

def donante_nuevo(request):
	if request.user.is_authenticated() and request.user.is_superuser:
		msj=""
		if request.method == 'POST':
			identificacion = request.POST['identificacion']
			nombres = request.POST['nombres']
			apellidos = request.POST['apellidos']
			model = Donante.objects.filter(identificacion=identificacion)
			if model:
				msj = "Existe donante con la identificación ingresada"
			else:
				model = Donante.objects.create_object(apellidos, identificacion, nombres)
				model.save()
				msj = "Donante guardado"
		plantilla = "donante_nuevo.html"
		return render(request, plantilla, {'msj':msj})
	else:
		return HttpResponseRedirect('/')

def estado(request, id):
	if request.user.is_authenticated() and request.user.is_superuser:
		msj = ""
		objeto = EstadoJuguete.objects.get(id=id)
		if request.method == "POST":
			descripcion = request.POST['descripcion']
			model = None
			if objeto.descripcion != descripcion:
				model = EstadoJuguete.objects.filter(descripcion=descripcion)
			if model:
				msj = "Existe estado con la descripción ingresada"
			else:
				model = objeto
				model.descripcion = descripcion
				model.save()
				msj = "Estado modificado"
		plantilla = "estado.html"
		return render(request, plantilla, {'objeto':objeto, 'msj':msj})
	else:
		return HttpResponseRedirect('/')

def estados(request):
	if request.user.is_authenticated() and request.user.is_superuser:
		plantilla = "estados.html"
		lista = EstadoJuguete.objects.all()
		return render(request, plantilla, {'lista':lista})
	else:
		return HttpResponseRedirect('/')

def estado_eliminar(request, id):
	if request.user.is_authenticated() and request.user.is_superuser:
		if request.method == 'POST':
			objeto = EstadoJuguete.objects.get(id=id)
			objeto.delete()
		return HttpResponseRedirect("/estado/listado")
	else:
		return HttpResponseRedirect('/')

def estado_nuevo(request):
	if request.user.is_authenticated() and request.user.is_superuser:
		msj = ""
		if request.method == "POST":
			descripcion = request.POST['descripcion']
			model = EstadoJuguete.objects.filter(descripcion=descripcion)
			if model:
				msj = "Existe estado con la descripción ingresada"
			else:
				model = EstadoJuguete.objects.create_object(descripcion)
				model.save()
				msj = "Estado guardado"
		plantilla = "estado_nuevo.html"
		return render(request, plantilla, {'msj':msj})
	else:
		return HttpResponseRedirect('/')

def juguete(request, id):
	if request.user.is_authenticated() and request.user.is_superuser:
		msj = ""
		objeto = Juguete.objects.get(id=id)
		if request.method == 'POST':
			model = objeto
			model.descripcion = request.POST['descripcion']
			model.estado = EstadoJuguete.objects.get(id=request.POST['estado'])
			if request.FILES.get('imagen', ''):
				model.imagen = request.FILES['imagen']
			msj = "Juguete modificado"
			model.save()
		plantilla = "juguete.html"
		estados = EstadoJuguete.objects.all()
		return render(request, plantilla, {'objeto':objeto, 'estados':estados, 'msj':msj})
	else:
		return HttpResponseRedirect('/')

def juguetes(request):
	if request.user.is_authenticated() and request.user.is_superuser:
		plantilla = "juguetes.html"
		lista = Juguete.objects.all()
		return render(request, plantilla, {'lista':lista})
	else:
		return HttpResponseRedirect('/')

def juguete_eliminar(request, id):
	if request.user.is_authenticated() and request.user.is_superuser:
		if request.method == 'POST':
			objeto = Juguete.objects.get(id=id)
			objeto.delete()
		return HttpResponseRedirect("/juguete/listado")
	else:
		return HttpResponseRedirect('/')

def juguete_nuevo(request):
	if request.user.is_authenticated() and request.user.is_superuser:
		msj = ""
		if request.method == 'POST':
			descripcion = request.POST['descripcion']
			estado = EstadoJuguete.objects.get(id=request.POST['estado'])
			imagen = None
			if request.FILES.get('imagen', ''):
				imagen = request.FILES['imagen']
			model = Juguete.objects.create_object(descripcion, estado, imagen)
			model.save()
			msj = "Juguete guardado"
		plantilla = "juguete_nuevo.html"
		estados = EstadoJuguete.objects.all()
		return render(request, plantilla, {'estados':estados, 'msj':msj})
	else:
		return HttpResponseRedirect('/')