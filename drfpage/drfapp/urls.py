from django.urls import path, include
from .views import *

from rest_framework import routers
from .routers import MyCustomerRouter
# router = routers.SimpleRouter()  # Создали объект класса
# router.register(r'animal', AnimalViewSet)


# router = routers.DefaultRouter()  # Создали объект класса
# router.register(r'animal', AnimalViewSet, basename='animal')  # basename= префикс для указания имени маршрута
# print(router.urls)

# router = MyCustomerRouter()  # Создали объект класса
# router.register(r'animal', AnimalViewSet, basename='animal')  # basename= префикс для указания имени маршрута
# print(router.urls)

urlpatterns = [
    # path('api/v1/animal_list', AnimalAPIView.as_view()),
    # path('api/v1/animal_list/', AnimalAPIView.as_view()),
    # path('api/v1/animal_list/<int:pk>/', AnimalAPIView.as_view()),  # Путь для изменения данных

    # path('api/v1/animal_list/', AnimalAPIList.as_view()),  # для просмотра всех данных
    # path('api/v1/animal_list/<int:pk>/', AnimalAPIList.as_view()),  # для просмотра данных с указанием id
    # path('api/v1/animal_list_update/<int:pk>/', AnimalAPIUpdate.as_view()),  # для изменения данных по id
    # path('api/v1/animal_detail/<int:pk>/', AnimalAPIDetailView.as_view()),  # для внесения изменения, удаления, добавления и получения данных по id

    #  Пути для класса AnimalViewSet работа с ViewSet
    # path('api/v1/animal_list/', AnimalViewSet.as_view({'get': 'list'})),  # для просмотра всех данных
    # path('api/v1/animal_list/<int:pk>/', AnimalViewSet.as_view({'post': 'update'}))

#   в данном пути можно выпонить get и post запрос и изменить конкретную статью указав id
    # path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/animal/

    # Пути на классы и установления прав доступа
    path('api/v1/animal/', AnimalAPIList.as_view()),
    path('api/v1/animal_update/<int:pk>/', AnimalAPIUpdate.as_view()),
    path('api/v1/animal_delete/<int:pk>/', AnimalAPIDestroy.as_view())

]