from django.db import models

# Create your models here.

class Rol(models.Model):
    id_rol = models.CharField(max_length=10, primary_key=True)
    rol = models.CharField(max_length=255)

    def __str__(self):
        return self.rol

class Usuario(models.Model):
    id_usuario = models.CharField(max_length=255, primary_key=True)
    nombre = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    id_estado = models.CharField(max_length=10, primary_key=True)
    estado = models.CharField(max_length=255)

    def __str__(self):
        return self.estado

class Control(models.Model):
    id_control = models.AutoField(primary_key=True)
    semestre = models.CharField(max_length=50, null=True, blank=True)
    anio = models.CharField(max_length=4, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    compania = models.CharField(max_length=255, null=True, blank=True)
    codigo = models.CharField(max_length=255, null=True, blank=True)
    tipologia = models.CharField(max_length=255, null=True, blank=True)
    frecuencia = models.CharField(max_length=255, null=True, blank=True)
    clasificacion = models.CharField(max_length=255, null=True, blank=True)
    descripcion_riesgo = models.TextField(null=True, blank=True)
    naturaleza = models.CharField(max_length=255, null=True, blank=True)
    objetivo = models.TextField(null=True, blank=True)
    conclusion_diseno = models.TextField(null=True, blank=True)
    ciclo = models.CharField(max_length=255, null=True, blank=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
    id_subproceso = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    descripcion_control = models.TextField(null=True, blank=True)
    supervisor = models.CharField(max_length=255, null=True, blank=True)
    fecha_elaboracion = models.DateField(null=True, blank=True)
    horas_invertidas = models.IntegerField(null=True, blank=True)
    recursos_consultados = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Prueba(models.Model):
    id_prueba = models.AutoField(primary_key=True)
    fecha_ejecucion = models.DateField()
    ejecutante = models.TextField()
    comentario_recorrido = models.TextField()
    id_control = models.ForeignKey(Control, on_delete=models.CASCADE)

    def __str__(self):
        return f"Prueba {self.id_prueba} - {self.fecha_ejecucion}"

class Pregunta(models.Model):
    id_pregunta = models.CharField(max_length=255, primary_key=True)
    texto = models.TextField()

    def __str__(self):
        return self.texto

class Respuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    id_control = models.ForeignKey(Control, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255, null=True, blank=True)
    explicacion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Respuesta {self.id_respuesta} a {self.id_pregunta}"

