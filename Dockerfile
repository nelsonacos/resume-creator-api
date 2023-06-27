# Usa la imagen base de Python 3.10
FROM python:3.10

# Establece la variable de entorno PYTHONUNBUFFERED en 1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el resto del código del proyecto al directorio de trabajo
COPY . .

# Expone el puerto 8000 (o el puerto que utilices en tu proyecto Django)
EXPOSE 8000

# Comando para ejecutar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]