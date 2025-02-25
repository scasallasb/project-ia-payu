# Proyecto IA PayU

Este proyecto contiene un backend y un frontend para la carga de archivos a un bucket de S3.

## Requisitos

- Node.js
- npm o yarn

## Instalación

### Backend

1. Navega al directorio del backend:

    ```sh
    cd project-ia-payu/backend_project
    ```

2. Instala las dependencias:

    ```sh
    npm install
    ```

3. Crea un archivo `.env` en el directorio  con las siguientes variables de entorno:

    ```env
    S3_BUCKET_NAME=tu-nombre-del-bucket
    AWS_ACCESS_KEY_ID=tu-access-key-id
    AWS_SECRET_ACCESS_KEY=tu-secret-access-key
    PORT=3001
    ```

4. Inicia el servidor:

    ```sh
    npm start
    ```

### Frontend

1. Navega al directorio del frontend:

    ```sh
    cd project-ia-payu/frontend_project/frontend
    ```

2. Instala las dependencias:

    ```sh
    npm install
    ```

3. Inicia la aplicación:

    ```sh
    npm start
    ```

## Uso

1. Abre tu navegador y navega a [http://localhost:3000](http://localhost:3000).
2. Utiliza la interfaz para cargar archivos al bucket de S3.

## Scripts Disponibles

### Backend

- `npm start`: Inicia el servidor backend.

### Frontend

- `npm start`: Inicia la aplicación en modo desarrollo.
- : Ejecuta las pruebas.
- `npm run build`: Construye la aplicación para producción.
- `npm run eject`: Ejecta la configuración de Create React App.

## Estructura del Proyecto

```plaintext
project-ia-payu/
├── backend_project/
│   ├── app.js
│   ├── controllers/
│   │   └── uploadController.js
│   ├── routes/
│   │   └── uploadRoutes.js
│   └── package.json
├── frontend_project/
│   └── frontend/
│       ├── public/
│       │   ├── index.html
│       │   └── manifest.json
│       ├── src/
│       │   ├── components/
│       │   │   └── FileUpload.js
│       │   ├── App.js
│       │   ├── App.css
│       │   ├── index.js
│       │   └── index.css
│       └── package.json
└── README.md