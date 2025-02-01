from django.shortcuts import render, get_list_or_404, HttpResponse, redirect
from Tarea.models import Tarea

# Create your views here.
#TAREAS
def task(request):

    ctx={
        #para obtener todos los datos de una tabla, se ocupa generar una instancia y con el all() es para 
        # extraer los datos de la mismas
        "ver":Tarea.objects.all()
    }

    return render(request, 'pendientes.html',ctx)


#editar
def edit(request,id):
    #este una funciona que si obtiene una lista de el id de la tabla Tareas o si no regresa un 404
    tarea_ = get_list_or_404(Tarea, id=id)

    ''' 
    if request.method=="POST":

        if 'form1' in request.POST:
            try:

                id_=request.POST["id_"]

                ctx_={
                    "info":Tarea.objects.get(id=id_)
                }

                return render(request, 'editar.html',ctx_)
        
            except ValueError:

                id_= None
        
        elif 'form2' in request.POST:

            idEdit=request.POST['id_']

            edit_=request.POST['edit_titulo']

            comple=request.POST.get('true')

            eliminar=request.POST.get('del') == "1"
            
            lol = Tarea.objects.get(id=idEdit)

            #Esta es una forma de en una sola linea obtener el POST y tambien de hacer el cambio en la base de datos
            #lol.titulo = Tarea.POST.get('edit_titulo')

            #pero como ya alamacene el titulo en una variabla para hacer la actualizacion es solo con la instancia que se creo
            #acceder a sus campos y actualizarla

            #Siempre que se trabaje con instancias se debe hacer llamar al save() para que los campos se actualizen

            if eliminar:
                lol.delete()

            if edit_:
                lol.titulo = edit_
                #Siempre que se trabaje con los checkbox por defecto devuelven 'on' o 'off'
                lol.completa = True if comple == 'on' else False
                lol.save()
                
            return render(request, 'editar.html')

    '''

    info ={
        'task': tarea_,
    }

    return render(request, 'editar.html', info )

def Create(request):

    if request.method == "POST":

        title=request.POST["Create"]
        description=request.POST["Description"]
        date=request.POST["Fecha"]

        Tarea.objects.create(titulo=title, descripcion=description, fecha_vencimiento=date) 

        return redirect('agregar')   

    return render(request, 'index.html')

def Eliminar(request, id):

    if request.method == 'POST':
        ala = Tarea.objects.get(id=id)

        edit_=request.POST['titulo']

        comple=request.POST.get('tr')

        date = request.POST.get('Date')

        eli = request.POST.get('del') == '1'

        if date:
            ala.fecha_vencimiento = date
            ala.save()
        
        if edit_:
            ala.titulo = edit_
            ala.save()   
            return redirect('inicio')
              
        if comple:
            #Siempre que se trabaje con los checkbox por defecto devuelven 'on' o 'off'
            ala.completa = True if comple == 'on' else False
            ala.save()
            return redirect('inicio')
        elif compile != 'on':
            ala.completa = False
            ala.save()
            return redirect('inicio')
        
        if eli:
            ala.delete()
            return redirect('inicio')
        else:
            return redirect('inicio')
        
        
    #De esta forma se puede usar una vista para solo procesar datos
    return HttpResponse(status=204)