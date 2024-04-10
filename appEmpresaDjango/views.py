from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Departamento
from .serializers import DepartamentoSerializer

class DepartamentoListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the departamento items for given requested user
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
    #permission_classes = [permissions.IsAuthenticated]

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
        Deletes the todo item with given departamento id if exists
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