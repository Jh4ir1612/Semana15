# Llama Flask App

Este proyecto es una aplicación web simple construida con Flask que utiliza el modelo Llama para generar texto a partir de un prompt proporcionado por el usuario.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos:

```
llama-flask-app
├── app.py                # Punto de entrada de la aplicación Flask
├── requirements.txt      # Dependencias necesarias para el proyecto
├── .env                  # Variables de entorno, incluyendo el token de Hugging Face
├── templates
│   └── index.html        # Plantilla HTML para la interfaz de usuario
└── README.md             # Documentación del proyecto
```

## Requisitos

Asegúrate de tener Python 3.7 o superior instalado en tu sistema. También necesitarás instalar las dependencias listadas en `requirements.txt`.

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Navega al directorio del proyecto.
3. Crea un entorno virtual (opcional pero recomendado):

   ```
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

4. Instala las dependencias:

   ```
   pip install -r requirements.txt
   ```

5. Crea un archivo `.env` en la raíz del proyecto y agrega tu token de Hugging Face:

   ```
   HF_TOKEN=tu_token_aqui
   ```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Uso

1. Abre tu navegador y ve a `http://127.0.0.1:5000/`.
2. Ingresa un prompt en el campo proporcionado y envíalo para recibir una respuesta generada por el modelo Llama.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, siéntete libre de abrir un issue o enviar un pull request.