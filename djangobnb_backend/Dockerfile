FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /usr/src/djangobnb_backend

# Configuración de Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y netcat-openbsd
RUN apt-get update && apt-get install -y libpq-dev gcc

# Actualizar pip
RUN pip install --upgrade pip

# Copiar dependencias y instalarlas
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copiar y preparar el entrypoint
COPY ./entrypoint.sh ./entrypoint.sh
RUN sed -i 's/\r$//g' ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# Copiar el código fuente
COPY . .

# Configurar el ENTRYPOINT y el CMD
ENTRYPOINT ["./entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
