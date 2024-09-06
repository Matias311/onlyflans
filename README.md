# ONLYFLANS

ONLYFLANS es una aplicación web de ventas de postres creada con Python y Django.

### Tecnologías

- Python 3
- Django 5

### Descripción

ONLYFLANS es una plataforma para vender y comprar postres caseros. Los usuarios pueden navegar por una variedad de postres, agregarlos a su carrito de compras y realizar pedidos.

### Características

- Registro e inicio de sesión de usuarios
- Navegación de postres disponibles
- Agregado de postres (solo admin)
- Gestión de pedidos por parte de los administradores
- Formulario de contacto

### Instalación y Configuración

#### Requisitos Previos

- Python 3.x
- Pip (gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado)

#### Pasos de Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd onlyflans
   ```

2. Crea y activa un entorno virtual:

   ```bash
   virtualenv venv
   source venv/Scripts/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en un archivo `.env` (opcional):

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   ```

5. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py makemigrations
   ```

   ```bash
   python manage.py migrate
   ```

6. Crea un superusuario para acceder al panel de administración:

   ```bash
   python manage.py createsuperuser
   ```

7. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

### Uso

1. Abre tu navegador web y navega a `http://localhost:8000/` para ver la página de inicio.
2. Usa el panel de administración en `http://localhost:8000/admin/` para gestionar el contenido de la aplicación.

### Rutas

- `/` - Página principal
- `/about` - Página sobre el negocio
- `/welcome` - Pagina donde aparecen productos privados (solo para usuarios registrados)
- `/contacto` - Pagina donde hay un formulario para poder contactarse con el dueño de la pagina
- `/detalle/flan_uuid` - Pagina donde se muestra el detalle del producto
- `/detalle_privados/flan_uuid` - Pagina donde aparecen los flanes privados (solo para usuarios registrados)
- `/profile` - Pagina donde aparecen los datos del usuario
- `/register` - Pagina donde se puede crear un nuevo usuario
- `/agregar/flan` - Pagina donde se puede agregar un nuevo producto a la base de datos (solo puede acceder el admin)
  Para mayor informacion entrar al archivio urls.py de la aplicacion web

### Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva característica (`git checkout -b feature/nueva-caracteristica`).
3. Haz commit de tus cambios (`git commit -am 'Añadida nueva característica'`).
4. Empuja tu rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.
