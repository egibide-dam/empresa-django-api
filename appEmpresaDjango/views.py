from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Departamento, Habilidad, Empleado
from .permissions import ReadOnlyPermission
from .serializers import DepartamentoSerializer, HabilidadSerializer, EmpleadoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class DepartamentoListApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    #permission_classes = {"get": [permissions.AllowAny], "post": [permissions.IsAuthenticated]}
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the departamento items
        '''
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Departamento with given data
        '''
        data = {
            'nombre': request.data.get('nombre'),
            'telefono': request.data.get('telefono'),
        }
        serializer = DepartamentoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartamentoDetailApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    def get_object(self, departamento_id):
        '''
        Helper method to get the object with given id
        '''
        try:
            return Departamento.objects.get(id=departamento_id)
        except Departamento.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, departamento_id, *args, **kwargs):
        '''
        Retrieves the Departamento with given departamento id
        '''
        departamento_instance = self.get_object(departamento_id)
        if not departamento_instance:
            return Response(
                {"res": "Object with departamento id  does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = DepartamentoSerializer(departamento_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, departamento_id, *args, **kwargs):
        '''
        Updates the departamento item with given id if exists
        '''
        departamento_instance = self.get_object(departamento_id)
        if not departamento_instance:
            return Response(
                {"res": "Object with departamento id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nombre': request.data.get('nombre'),
            'telefono': request.data.get('telefono')
        }
        serializer = DepartamentoSerializer(instance = departamento_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, departamento_id, *args, **kwargs):
        '''
        Deletes the departamento item with given id
        '''
        departamento_instance = self.get_object(departamento_id)
        if not departamento_instance:
            return Response(
                {"res": "Object with departamento id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        departamento_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )



class HabilidadListApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    #permission_classes = {"get": [permissions.AllowAny], "post": [permissions.IsAuthenticated]}
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the habilidades items
        '''
        habilidades = Habilidad.objects.all()
        serializer = HabilidadSerializer(habilidades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Habilidad with given data
        '''
        data = {
            'nombre': request.data.get('nombre'),
        }
        serializer = HabilidadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HabilidadDetailApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    def get_object(self, habilidad_id):
        '''
        Helper method to get the object with given id
        '''
        try:
            return Habilidad.objects.get(id=habilidad_id)
        except Habilidad.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, habilidad_id, *args, **kwargs):
        '''
        Retrieves the Habilidad with given departamento id
        '''
        habilidad_instance = self.get_object(habilidad_id)
        if not habilidad_instance:
            return Response(
                {"res": "Object with habilidad_id  does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = HabilidadSerializer(habilidad_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, habilidad_id, *args, **kwargs):
        '''
        Updates the habilidad item with given id if exists
        '''
        habilidad_instance = self.get_object(habilidad_id)
        if not habilidad_instance:
            return Response(
                {"res": "Object with habilidad id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nombre': request.data.get('nombre'),
        }
        serializer = HabilidadSerializer(instance = habilidad_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, habilidad_id, *args, **kwargs):
        '''
        Deletes the habilidad item with given id
        '''
        habilidad_instance = self.get_object(habilidad_id)
        if not habilidad_instance:
            return Response(
                {"res": "Object with habilidad id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        habilidad_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class EmpleadoListApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    #permission_classes = {"get": [permissions.AllowAny], "post": [permissions.IsAuthenticated]}
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the empleados items
        '''
        empleados = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Empleado with given data
        '''
        data = {
            'nombre': request.data.get('nombre'),
            'fecha_nacimiento':request.data.get('fecha_nacimiento'),
            'antiguedad':request.data.get('antiguedad'),
            'departamento':request.data.get('departamento'),
            'habilidades':request.data.get('habilidades'),
        }
        serializer = EmpleadoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpleadoDetailApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    def get_object(self, empleado_id):
        '''
        Helper method to get the object with given id
        '''
        try:
            return Empleado.objects.get(id=empleado_id)
        except Empleado.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, empleado_id, *args, **kwargs):
        '''
        Retrieves the Empleado with given id
        '''
        empleado_instance = self.get_object(empleado_id)
        if not empleado_instance:
            return Response(
                {"res": "Object with empleado_id  does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EmpleadoSerializer(empleado_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, empleado_id, *args, **kwargs):
        '''
        Updates the empleado item with given id if exists
        '''
        empleado_instance = self.get_object(empleado_id)
        if not empleado_instance:
            return Response(
                {"res": "Object with empleado id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nombre': request.data.get('nombre'),
        }
        serializer = EmpleadoSerializer(instance = empleado_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, empleado_id, *args, **kwargs):
        '''
        Deletes the empleado item with given id
        '''
        empleado_instance = self.get_object(empleado_id)
        if not empleado_instance:
            return Response(
                {"res": "Object with empleado id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        empleado_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )