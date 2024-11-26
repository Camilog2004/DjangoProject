from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from app.models import Usuario, Control, Prueba, Respuesta, Estado


def login_view(request):
    if request.method == "POST":
        nombre_usuario = request.POST.get("nombre")
        contrasena = request.POST.get("contrasena")
        anio = request.POST.get("anio")
        semestre = request.POST.get("semestre")

        # Verificar credenciales
        try:
            usuario = Usuario.objects.get(nombre=nombre_usuario,contrasena=contrasena)
            request.session['usuario_id'] = usuario.id_usuario
            request.session['anio'] = anio
            request.session['semestre'] = semestre

            return redirect('principal')
        except Usuario.DoesNotExist:
            return render(request, "login.html")

    return render(request, "login.html")

def principal_view(request):
    usuario_id = request.session.get('usuario_id')
    anio = request.session.get('anio')
    semestre = request.session.get('semestre')

    if usuario_id and anio and semestre:
        # Obtener los controles asociados al usuario, año y semestre
        controles = Control.objects.filter(anio=anio, semestre=semestre, id_usuario=usuario_id)
        return render(request, "principal.html", {"controles": controles})

        # Redirigir al login si no hay datos en la sesión
    return redirect('login')

def diseno_view(request,control_id):
    control = get_object_or_404(Control, id_control=control_id)
    prueba = Prueba.objects.filter(id_control=control_id).first()
    respuestas=Respuesta.objects.filter(id_control=control_id).order_by('id_respuesta')

    if request.method == 'POST':
        try:
            with transaction.atomic():
                fecha_ejecucion = request.POST.get('execution_date')
                ejecutante = request.POST.get('prueba_ejecutante')
                comentario = request.POST.get('prueba_comentarios')

                if prueba:
                    prueba.fecha_ejecucion = fecha_ejecucion
                    prueba.ejecutante = ejecutante
                    prueba.comentario_recorrido = comentario
                else:
                    prueba = Prueba(
                        id_control=control,
                        fecha_ejecucion=fecha_ejecucion,
                        ejecutante=ejecutante,
                        comentario_recorrido=comentario
                    )
                prueba.save()

                todas_son_si = True
                # Actualizar las respuestas
                for index, respuesta in enumerate(respuestas, start=1):
                    respuesta_valor = request.POST.get(f'respuesta_{index}')
                    explicacion_valor = request.POST.get(f'explicacion_{index}')

                    respuesta.respuesta = respuesta_valor
                    respuesta.explicacion = explicacion_valor
                    respuesta.save()

                    if respuesta_valor.lower() != "si":
                        todas_son_si = False

                if todas_son_si:
                    control.conclusion_diseno ="Satisfactorio"
                else:
                    control.conclusion_diseno ="Insatisfactorio"
                control.save()

                return redirect('principal')
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'diseno.html', {'control': control,'prueba': prueba,'respuestas':respuestas})


def encabezado_view(request, control_id):
    control = get_object_or_404(Control, id_control=control_id)


    if request.method == "POST":
        control.fecha_elaboracion = request.POST.get('control_creation_date', control.fecha_elaboracion)

        estado_string = request.POST.get('control_status')
        if estado_string == "Terminado" and control.conclusion_diseno == "No evaluado":
            return JsonResponse({'error': 'Debes realizar la prueba de diseno primero'}, status=400)

        estado = Estado.objects.get(estado=estado_string)
        control.id_estado = estado



        control.horas_invertidas = request.POST.get('control_total_hours')
        control.recursos_consultados = request.POST.get('control_resources')

        control.save()

        return redirect('principal')


    return render(request, 'encabezado.html', {'control': control})