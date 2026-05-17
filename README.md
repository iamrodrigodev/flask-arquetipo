# Guía de Inicio Rápido - Flask Arquetipo

Sigue estos pasos para levantar el entorno de desarrollo:

### 1. Levantar la Base de Datos (PostgreSQL)
Ejecuta el siguiente comando para iniciar el contenedor de la base de datos:
```bash
docker run -d --name postgres-arquetipo -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=arquetipo_db postgres:latest
```

### 2. Configurar el Entorno Virtual de Python
Crea y activa el entorno virtual:

**En Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**En Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
Una vez activado el entorno, instala las librerías necesarias:
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno
Copia el archivo de ejemplo y ajusta tus credenciales si es necesario:
```bash
copy .env.example .env
```

### 5. Iniciar el Servidor
Ejecuta la aplicación:
```bash
python app.py
```

El servidor estará disponible en `http://localhost:5000`.
Las tablas y los datos iniciales (Admin/Usuario) se crearán automáticamente al primer arranque.
