# Arquetipo Flask N-Tier (Arquitectura Profesional)

Este repositorio es una base sólida y profesional (arquetipo) diseñada para desarrolladores y estudiantes que buscan implementar servidores Flask siguiendo estándares de ingeniería de software de alto nivel, inspirados en la arquitectura N-Capas de Java (Spring Boot).

## 🚀 Características Principales

- **Arquitectura N-Tier**: Separación estricta de responsabilidades (Controladores, Servicios, Repositorios y Modelos).
- **Seguridad Robusta**: 
  - Autenticación basada en JWT (Bearer Token) mediante cabeceras HTTP.
  - Control de acceso basado en roles (ADMINISTRADOR y USUARIO).
  - Bloqueo automático de cuenta tras intentos fallidos de inicio de sesión.
- **Gestión de Datos Inteligente**:
  - Sincronización automática de tablas y esquemas en PostgreSQL.
  - Semilla de datos (Seeding) para roles y usuarios base.
  - Catálogo completo de ubicaciones (Departamentos, Provincias, Distritos de Perú) precargado mediante SQL.
- **Calidad de Código**:
  - Validación de datos y sanitización segura (XSS) directamente en la capa de DTOs.
  - Logs estructurados con ID de trazabilidad e IP del cliente para auditoría.
  - Manejo global de excepciones con respuestas JSON estandarizadas.
- **Interoperabilidad**: Colección de Postman incluida para pruebas inmediatas.

## 🛠️ Guía de Inicio Rápido

### 1. Levantar la Base de Datos (PostgreSQL)
Utiliza Docker para iniciar una instancia lista para el arquetipo:
```bash
docker run -d --name postgres-arquetipo -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=arquetipo_db postgres:latest
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
