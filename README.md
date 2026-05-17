# Arquetipo Flask

## Guía de Inicio Rápido

### 1. Levantar la Base de Datos (PostgreSQL)
Utiliza Docker para iniciar una instancia lista para el arquetipo:
```bash
docker run -d --name postgres-arquetipo -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=arquetipo_db postgres:15-alpine
```

### 2. Configurar el Entorno de Python
Crea y activa el entorno virtual:

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configuración de Variables de Entorno
Copia el archivo de ejemplo y ajusta las claves si lo deseas:
```bash
copy .env.example .env
```

### 5. Iniciar el Servidor
```bash
python app.py
```
*El sistema creará automáticamente los esquemas, tablas e insertará los datos iniciales al arrancar.*

## Credenciales por Defecto
- **Administrador**: `admin@arquetipo.com` / `admin123`
- **Usuario**: `usuario@arquetipo.com` / `usuario123`
