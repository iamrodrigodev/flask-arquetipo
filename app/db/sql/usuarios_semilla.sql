INSERT INTO autenticacion.roles (id, nombre) VALUES (1, 'ADMINISTRADOR') ON CONFLICT (nombre) DO NOTHING;
INSERT INTO autenticacion.roles (id, nombre) VALUES (2, 'USUARIO') ON CONFLICT (nombre) DO NOTHING;

-- Las contraseñas están hasheadas usando bcrypt (soportado nativamente por nuestro passlib).
-- La contraseña para ambas cuentas es: Admin123!

INSERT INTO autenticacion.usuarios (nombre, apellidos, correo, clave, telefono, activo, rol_id, fecha_creacion, fecha_actualizacion) 
VALUES (
    'Admin', 
    'Sistema', 
    'admin@sistema.com', 
    '$2b$12$lW9E/PwDVWWQ9WbWgq9Dn.Wp2ahyNMbVoxJFGQ1kE/kvgTbeAeX0e', 
    '999999999', 
    true, 
    1, 
    CURRENT_TIMESTAMP, 
    CURRENT_TIMESTAMP
)
ON CONFLICT (correo) DO NOTHING;

INSERT INTO autenticacion.usuarios (nombre, apellidos, correo, clave, telefono, activo, rol_id, fecha_creacion, fecha_actualizacion) 
VALUES (
    'Usuario', 
    'Demo', 
    'usuario@demo.com', 
    '$2b$12$lW9E/PwDVWWQ9WbWgq9Dn.Wp2ahyNMbVoxJFGQ1kE/kvgTbeAeX0e', 
    '888888888', 
    true, 
    2, 
    CURRENT_TIMESTAMP, 
    CURRENT_TIMESTAMP
)
ON CONFLICT (correo) DO NOTHING;
