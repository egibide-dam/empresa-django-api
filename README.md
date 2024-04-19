# Empresa Django API

Enlace para acceder a la documentación generada con Swagger: [EmpresaDjango API](http://127.0.0.1:8000/swagger/)

- usuario/password de prueba: ilarra/1234

## Prerrequisitos

1. Instalar [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. En Windows, instalar [Scoop](https://scoop.sh) usando PowerShell:

    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
    ```

   Y después instalar los comandos necesarios:

    ```powershell
    scoop install make
    ```

## Puesta en marcha

1. Construir el contenedor donde se ejecuta la aplicación:

    ```shell
    make build
    ```

2. Arrancar el contenedor:

    ```shell
    make start
    ```

## Referencias

- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
