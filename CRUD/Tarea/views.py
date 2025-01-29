from django.shortcuts import render
from Tarea.models import Tarea

# Create your views here.
def Create(request):

    if request.method == "POST":

        title=request.POST["Create"]
        description=request.POST["Description"]
        date=request.POST["Fecha"]

        Tarea.objects.create(titulo=title, descripcion=description, fecha_vencimiento=date) 

        return render(request, 'index.html')   

    return render(request, 'index.html')

def wait(request):

    ctx={
        #para obtener todos los datos de una tabla, se ocupa generar una instancia y con el all() es para 
        # extraer los datos de la mismas
        "ver":Tarea.objects.all()
    }

    return render(request, 'pendientes.html',ctx)

def editar(request):

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


    return render(request, 'editar.html')