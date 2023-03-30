from rest_framework import routers

# Создание своего класс Router
class MyCustomerRouter(routers.SimpleRouter):
    routers = [
        routers.Route(url=r'^{prefix}$',  # шаблон маршрута
                      mapping={'get': 'list'},  # связывает тип запроса с соответствующим методом вьюсета
                      name='{basename}-list',  # определяет название маршрута
                      detail=False,  # список или отдельная запись
                      initkwargs={'suffix': 'list'}), # доп аргументы, для коллекции keyworks которые передаются конкретному определению при сробатывании маршрута
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-details',
                      detail=True,
                      initkwargs={'suffix': 'Detail'})
    ]










