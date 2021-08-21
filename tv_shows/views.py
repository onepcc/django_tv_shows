from django.shortcuts import render, HttpResponse, redirect
from time import  localtime, strftime
from tv_shows.models import *
from django.contrib import messages #para mensajes de validaciones



def inicio(request):
 
    return redirect('/shows')

#Funcion para crear un nuevo show
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')

    if request.method == 'POST':
        print(request.POST)

        errors = Show.objects.basic_validator(request.POST)
        # compruebe si el diccionario de errores tiene algo en él
        if len(errors) > 0:
            # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
            for key, value in errors.items():
                messages.error(request, value)

            request.session['show_title']=request.POST['title_show']
            request.session['network_show']=request.POST['network_show']
            request.session['desc_show']=request.POST['desc_show']
            request.session['date_show']=request.POST['date_show']
            # redirigir al usuario al formulario para corregir los errores
            return redirect('/shows/new')
        
        else:
            # si el objeto de errores está vacío, eso significa que no hubo errores.
            # recuperar el blog para actualizarlo, realizar los cambios y guardar
            # leemos las variables del formulario
            request.session['show_title']=""
            request.session['network_show']=""
            request.session['desc_show']=""
            request.session['date_show']=""


            title_show= request.POST['title_show']
            network_show= request.POST['network_show']
            date_show= request.POST['date_show']
            desc_show= request.POST['desc_show']
                        
            # ejecutamos comando ORM para crear usauario, los campos deben coincidir con el modelo definido
            show_db = Show.objects.create(
                title = title_show,
                network = network_show,
                description = desc_show,
                release_date= date_show,
                )
            messages.success(request, f"Show creado correctamente el show {title_show}")
            print("Show CREADO CORRECTAMENTEE!!!", show_db)
            
            return redirect(f'/shows/{show_db.id}')

#FUNCION MUESTRA TODOS LOS SHOWS
def shows(request):

    shows=Show.objects.all() # se lee datos de la DB
    
    datos = {
        'saludo': 'TV Shows RESTfull',
        'tvshows': shows,
        
    }

    return render(request,'index2.html',datos)

#FUNCION MUESTRA INFORMACION DE SHOW PARTICULAR
def ver_show(request,val):
    print(request)
    print("Show a ver",val)
    show_info = Show.objects.get(id=val) #informacion del libro con id = val
    
    contexto ={
        'info_show':show_info,
    }
        
    return render(request, 'info_show.html', contexto)

#FUNCION EDITAR SHOW
def edit_show(request,val):
    if request.method == 'GET':
        show_info = Show.objects.get(id=val) #informacion del show con id = val
    
        datos ={
            'show':show_info,
        }

        return render(request,'edit_show.html',datos)

#FUNCION PROCESAR ACTUALIZACION SHOW
def update_show(request,val):
        print(request.POST)

        errors = Show.objects.basic_validator(request.POST)
        # compruebe si el diccionario de errores tiene algo en él
        if len(errors) > 0:
            # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
            for key, value in errors.items():
                messages.error(request, value)
            # redirigir al usuario al formulario para corregir los errores
            return redirect(f'/shows/{val}/edit')
        
        else:
            # si el objeto de errores está vacío, eso significa que no hubo errores.
            # recuperar el blog para actualizarlo, realizar los cambios y guardar
            # leemos las variables del formulario
            title_show= request.POST['title_show']
            network_show= request.POST['network_show']
            date_show= request.POST['date_show']
            desc_show= request.POST['desc_show']
            
            # ejecutamos comando ORM para actualizar tv show, los campos deben coincidir con el modelo definido
            tvupdate= Show.objects.get(id =val)
            
            tvupdate.title=title_show
            tvupdate.network=network_show
            tvupdate.release_date=date_show
            tvupdate.description=desc_show
            tvupdate.save()
            messages.success(request, F"Show {tvupdate.title} actualizado correctamente")
            
            print(f"Show {tvupdate.title} ACTUALIZADO CORRECTAMENTEE!!!")
            # redirigir a la ruta de exito
            return redirect(f'/shows/{tvupdate.id}')

#FUNCION BORRAR SHOW
def delete_show(request,val):
    show_borrar = Show.objects.get(id=val)

    # ejecutamos comando ORM para BORRAR tv show, los campos deben coincidir con el modelo definido
    show_borrar.delete()
 
    return redirect('/shows')


