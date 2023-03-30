import io
from rest_framework import serializers
from .models import Animal
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# ------------------------  На 2 уроке делали ---------------
# class AnimalSerialazer(serializers.ModelSerializer): # Сериализатор который работает с моделями
#     class Meta:
#         model = Animal
#         fields = ('title', 'category_id') # поля для сериализации
#
#
# # Преобразование объектов класса в json формат. Класс сериализвтора
# class AnimalModel:
#     def __init__(self, title, content):  # передаём параметры
#         self.title = title  # локальный атрибут
#         self.content = content


# def encode():
#     model = AnimalModel('Tiger', 'Content: Big Lines cat')
#     model_sr = AnimalSerialazer(model)  # прогнали через Сериализатор
#     print(model_sr.data, type(model_sr.data), sep='\n')  # выведим сериализованный данные (словарь) и тип
#     json = JSONRenderer().render(model_sr.data)  # преобразовывает в байтовую JSON строку
#     print(json)  # получаем байтовую строку (json) для клиента
#
#
#
# # Обратное преобразование с Json в объект строки (декодирование)
# def decode():
#     stream = io.BytesIO(b'{"title":"Tiger","content":"Content: Big Lines cat"}')  # имитируем запроса от клиента
#     data = JSONParser().parse(stream)
#     serializer = AnimalSerialazer(data=data)  # получаем объект сериализатора (декодируем)
#     serializer.is_valid()
#
#     print(serializer.validated_data)


#  py manage.py shell запустить оболочку shell
# в оболочку импортируем from drfapp.serializers import encode
# запускуаем функ encode()
# quit() что бы выйти


# # Сериализатор который работает для моделек преобразовывает в JSON и обратно


# ------------------------  На 3 уроке делали ---------------

# Класс Сериализатор для модели Animal с подробным указанием полей
# class AnimalSerializer(serializers.Serializer):
#   title = serializers.CharField(max_length=255)
#   content = serializers.CharField()
#   time_create = serializers.DateTimeField(read_only=True)  # только для чтения
#   time_update = serializers.DateTimeField(read_only=True)  # только для чтения
#   is_published = serializers.BooleanField(default=True)  # по умолчанию
#   category_id = serializers.IntegerField()
#
#   # метод Сериализатора для добавления данных через Postman
#   def create(self, validated_data):
#       return Animal.objects.create(**validated_data)
#
#   # метод Сериализатора для изменения сущ данных
#   def update(self, instance, validated_data):  # instance объект модельки
#       instance.title = validated_data.get("title", instance.title)
#       instance.content = validated_data.get("content", instance.content)
#       instance.time_update = validated_data.get("time_update", instance.time_update)
#       instance.is_published = validated_data.get("is_published", instance.is_published)
#       instance.category_id = validated_data.get("category_id", instance.category_id)
#       instance.save()
#       return instance

# ----------------------------------------------------------------------------------

# Упрощённый вариант Класс Сериализатор для модели Animal
class AnimalSerializer(serializers.ModelSerializer):  # на прямую связывается с моделями и упращает работу
    class Meta:
        model = Animal
        # fields = ('title', 'content', 'category')  # если хотим указать все поля  "__all__"
        fields = "__all__"



















