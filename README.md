# EmpresaDjango API

Aplicación Django de ejemplo con API REST.

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

3. Acceder a [la aplicación](http://localhost:8000).

   > Usuario/Password de prueba: `ilarra/1234`

## Referencias

- [Simple JWT documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [djoser 2.2.2 documentation](https://djoser.readthedocs.io/en/latest/)
- [drf-yasg 1.21.7 documentation](https://drf-yasg.readthedocs.io/en/stable/)
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
