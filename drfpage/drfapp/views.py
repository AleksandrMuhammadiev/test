from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView  # главный класс среди всех класс
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView

from .models import Animal, Category
from .serializers import AnimalSerializer

from rest_framework.viewsets import ModelViewSet, GenericViewSet


# Create your views here.

# class AnimalAPIView(ListAPIView): # Класс наследуется от  ListAPIView
#     queryset = Animal.objects.all() # получем всех животных
#     serializer_class = AnimalSerialazer


# class AnimalAPIView(APIView):  # Наследуемся от корневого класса Который определяет представление и метод
#     def get(self, request):  # метод который будить отвечать за обработку get запросов
#         model = Animal.objects.all().values()
#         return Response({'posts': list(model)})
#
#     def post(self, request):  # метод который будить отвечать за post запрос и добавляет данный в БД
#         post_new = Animal.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             category_id=request.data['category_id']
#         )
#         return Response({'post': model_to_dict(post_new)})


# Данный класс и Сериализатор имеет методы get, post, save, put  delete
# class AnimalAPIView(APIView):  # Наследуемся от корневого класса Который определяет представление и метод
#
#     # метод который будить отвечать за обработку get запросов преобразование данных в json
#     def get(self, request):
#         model = Animal.objects.all()
#         return Response({'posts': AnimalSerializer(model, many=True).data})  # получаем байтовую json строку
#
#     # метод который будить отвечать за выполнение post запросов добавления данных в json
#     def post(self, request):  # метод который будить отвечать за post запрос и добавляет данный в БД
#         serializer = AnimalSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)  # проверки на валидацию данных полей
#         serializer.save()  # сохраняем  данные
#
#         # post_new = Animal.objects.create(  # добавление данных в указанные поля
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     category_id=request.data['category_id']
#         # )
#         # return Response({'post': AnimalSerialazer(post_new).data})
#
#         return Response({'post': serializer.data})  # сохранённые дынные преобразуем в json
#
#     # Метод для внесения изменения данных  в сущ поле под указанной id
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if pk:
#             try:
#                 instance = Animal.objects.get(pk=pk)  # получаем запись по ключу (id)
#             except:
#                 return Response({"error": f"Объект с данной id={pk} не существует"})
#         else:
#             return Response({"error": "Объект не определён"})
#             # новая запись    -  то что хотим изменить
#         serializer = AnimalSerializer(data=request.data, instance=instance)  # автомтически вызовет метод update()
#         serializer.is_valid(raise_exception=True)  # Для определения ошибки в API
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     # Метод для удаления данных  сущ поля под определённой id - Дать написать метод на ДЗ
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if pk:
#             try:
#                 instance = Animal.objects.get(pk=pk)
#                 instance.delete()
#             except:
#                 return Response({"error": f"Объект под id={pk} нет существует"})
#         else:
#             return Response({"error": f"Удаление не может быть выполнено"})
#
#         return Response({"post": f"Удалена запись под id={pk}"})

# ----------------------------------------------------------------------

# # Класс для получение и создания данных данный класс выполняет get и post запрос
# class AnimalAPIList(ListCreateAPIView):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer
#
#
# # Класс для внесения изменения Данных наследуясь от сущ класса
# class AnimalAPIUpdate(UpdateAPIView):
#     queryset = Animal.objects.all()  # возвращает только одну конкретную запись
#     serializer_class = AnimalSerializer
#
#
# # Класс для внесения изменения, удаления, добавления и получения данных
# class AnimalAPIDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Animal.objects.all()  # возвращает только одну конкретную запись
#     serializer_class = AnimalSerializer


# ----------------------------------------------------------------------

# Данный класс отвечает за get, post, put, delete Запрос один класс заменяет 3 класса
# class AnimalViewSet(ModelViewSet):
#     queryset = Animal.objects.all()  # возвращаем всё
#     serializer_class = AnimalSerializer


# class AnimalViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     # queryset = Animal.objects.all()  # возвращаем всё
#     serializer_class = AnimalSerializer
#
#     # Данный метод возвращает только первые 3 записи в таком случае queryset не нужен
#     # но нужно в urls
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:  # если нет pk то вернёт указ кол-во статей
#             return Animal.objects.all()[:3]
#
#         return Animal.objects.filter(pk=pk)  # в против случае вернёт конкретную запись по pk
#
#     # метод для получения списка категорий
#     @action(methods=['get'], detail=False)  # для чтения списков категорий если True то вернётся одна запись
#     def category(self, request):  # pk=None нужно указывать если мы будим брать конкретную категорию
#         cats = Category.objects.all()
#         return Response({'cats': [c.cat_name for c in cats]})  # получаем в словарь список категорий в маршрут
#
#     # метод для получения категории с указанием pk
#     @action(methods=['get'], detail=True)  # для чтения списков категорий если True то вернётся одна запись
#     def category_pk(self, request, pk=None):  # pk=None нужно указывать если мы будим брать конкретную категорию
#         cats = Category.objects.get(pk=pk)  # указываем id категории
#         return Response({'cats': cats.cat_name})


# ---------------------------------------------------------------------
# 3 класс Для прописания прав доступа

class AnimalAPIList(ListCreateAPIView):  # возвращает список статей
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalAPIUpdate(RetrieveUpdateAPIView):  # меняет определённую запись
    queryset = Animal.objects.all()  # возвращает только одну конкретную запись
    serializer_class = AnimalSerializer


class AnimalAPIDestroy(RetrieveDestroyAPIView):  # удаляет определённую запись
    queryset = Animal.objects.all()  # возвращает только одну конкретную запись
    serializer_class = AnimalSerializer
