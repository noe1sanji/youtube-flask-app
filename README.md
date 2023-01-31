# YouTube Flask App

*Una aplicacion simple con Flask.*

En la pagina principal carga los videos mas populares (de acuerdo a la region), permite realizar busquedas, el estilo es sencillo pero voy a mejorarlo mas adelante asi como mas funcionalidades.


# Como ejecutar

Clone este repositorio.

```
git clone https://github.com/noe1sanji/youtube-flask-app.git
```

Entre al directorio que se acaba de crear.

```
cd youtube-flask-app
```

Creando el entorno virtual.

*Windows:*
```
python -m venv venv
```
*Linux/MacOS:*
```
python3 -m venv venv
```

Activando el entorno virtual.

*Windows (cmd):*
```
venv\Scripts\activate.bat
```
*Windows (PowerShell):*
```
venv\Scripts\activate.ps1
```
*Linux/MacOS:*
```
source venv/bin/activate
```

Instalando dependencias.

```
pip install -r requeriments.txt
```

Configurando variables.

```
export FLASK_APP=app
```

Cree un archivo .env y establezca la variable DEVELOPER_KEY con la clave de API.

Para crear la clave de API tiene que habilitar la API de YouTube en un proyecto, ir a [credenciales](https://code.google.com/apis/console/?hl=es) y generar la clave. Puede visitar la [documentacion](https://developers.google.com/youtube/registering_an_application?hl=es).

Dentro del archivo `app/__init__.py` modifique la variable `LANG` para establecer el lenguaje.

Estos son los enlaces a las librerias que necesitan esa variable para ver si su idioma esta soportado.

[Arrow](https://arrow.readthedocs.io/en/latest/api-guide.html#module-arrow.locales)
|
[humanize](https://python-humanize.readthedocs.io/en/latest/#localization)

Si necesita recargar la aplicacion cuando realice cambios configure la siguiente variable.

```
export FLASK_DEBUG=true
```

Ejecutando la aplicacion.

```
flask run
```

Ingrese a `http://127.0.0.1:5000`