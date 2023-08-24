from rest_framework import serializers
from API_Biblioteca.models import *

class Livro_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'categoria', 'data_pub']


class Leitor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Leitor
        fields = ['id', 'nome', 'idade', 'cidade'] 

