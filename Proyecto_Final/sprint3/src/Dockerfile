
# imagen base ligera de Python
FROM python:3.9-slim

# directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos y luego instalar las dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

#  ejecutar la aplicación
CMD ["python", "app.py"]    
