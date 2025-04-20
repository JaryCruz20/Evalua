# Imagen
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .
COPY app.py .
COPY static ./static
COPY templates ./templates

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Variables de entorno 
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV DATABASE_URL="postgresql://wcruz:QdRmLDrQb78oXKKByl8k484k2aXdBs59@dpg-cvmpjc3e5dus739m9hk0-a/test_oz3h"


EXPOSE 8080

# Comando de inicio
CMD ["app.run(host='0.0.0.0', port=5000"]