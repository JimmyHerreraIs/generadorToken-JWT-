# 🔐 Secure Auth API – FastAPI + JWT + Security Controls

API de autenticación desarrollada con **FastAPI**, enfocada en **seguridad ofensiva/defensiva**, control de acceso y diseño backend escalable.

---

## 🧠 Filosofía del proyecto

Este proyecto fue diseñado no solo para autenticar usuarios, sino para simular un entorno real donde se aplican medidas de **seguridad activas** frente a ataques comunes como:

* Fuerza bruta
* Manipulación de tokens
* Acceso no autorizado a endpoints críticos

---

## ⚙️ Stack tecnológico

* ⚡ FastAPI (alto rendimiento)
* 🐍 Python 3.12
* 🗄️ SQLAlchemy ORM
* 🔐 JWT (python-jose)
* 🔑 Passlib (bcrypt hashing)
* 📦 Pydantic (validación de datos)

---

## 🏗️ Arquitectura del proyecto

```id="cx1ywt"
app/
│
├── main.py                # Punto de entrada
├── database.py            # Configuración DB
│
├── models/                # Modelos ORM (User)
├── schemas/               # Validación (Pydantic)
├── routers/               # Endpoints (auth)
│   └── auth_router.py
│
├── utils/
│   ├── security.py        # JWT + hashing + auth logic
│   ├── crud.py            # Acceso a datos
│   ├── logger.py          # Logging de eventos
```

📌 Estructura modular inspirada en entornos productivos.

---

## 🔐 Seguridad implementada

### 1. 🔑 Hashing de contraseñas

* Uso de **bcrypt**
* Nunca se almacenan contraseñas en texto plano

---

### 2. 🪪 Autenticación con JWT

* Tokens firmados con HS256
* Payload con `sub` (username)
* Validación en cada request protegido

---

### 3. 🚫 Protección contra fuerza bruta

```python id="ts7w2i"
intentos_fallidos = {}
```

* Conteo de intentos por usuario/IP
* Bloqueo temporal tras múltiples fallos
* Registro de eventos sospechosos

---

### 4. 👑 Control de acceso (RBAC básico)

```python id="5gsvk7"
is_admin = Column(Boolean, default=True)
```

* Diferenciación entre usuarios normales y administradores
* Endpoint `/admin` protegido
* Validación de privilegios en backend

---

### 5. 📜 Logging de seguridad

```python id="v2p0bm"
log_event("Intento fallido", ip)
```

* Registro de intentos fallidos
* Registro de bloqueos
* Base para SIEM o auditoría

---

## 🚀 Endpoints principales

### 📝 Registro

```http id="9bjzvf"
POST /register
```

### 🔐 Login

```http id="n1pr8b"
POST /login
```

### 👑 Admin (protegido)

```http id="nt15qh"
GET /admin
Authorization: Bearer <token>
```

---

## 🔥 Flujo de autenticación

1. Usuario inicia sesión
2. Se valida contraseña (bcrypt)
3. Se genera JWT
4. Cliente envía token en headers
5. Backend valida token y permisos

---

## 🧪 Pruebas de seguridad realizadas

Este sistema fue probado manualmente simulando:

* ❌ Tokens inválidos
* ❌ Tokens modificados
* ❌ Acceso sin autorización
* ❌ Ataques de fuerza bruta

---

## ⚠️ Riesgos identificados (mentalidad hacker)

* 🔸 Uso de almacenamiento en memoria para intentos (no persistente)
* 🔸 Falta de expiración avanzada de tokens (refresh tokens)
* 🔸 Sin rate limiting a nivel de red

---

## 📈 Mejoras futuras

* 🔐 Refresh Tokens
* ⏱️ Expiración avanzada y rotación de tokens
* 🛡️ Rate limiting (middleware)
* 🌐 Deploy en cloud (Docker + Nginx)
* 📊 Integración con sistemas de monitoreo

---

## 🧠 Enfoque en ciberseguridad

Este proyecto refleja un enfoque **blue team + backend engineering**, donde se implementan controles defensivos desde el diseño.

---

## 👨‍💻 Autor

**Jimmy Herrera**

* Backend Developer
* Enfocado en Ciberseguridad
* Interesado en Pentesting y Secure Coding

---

## 💡 Nota final

Este proyecto no busca ser perfecto, sino demostrar cómo construir sistemas backend **seguros, auditables y escalables** desde cero.
