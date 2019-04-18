from django.urls import path

from blog2 import views
#注意“/”，应该加上
urlpatterns = [
    path('index/',views.test)
    # path('index1/',views.test1),
    # path('index2/',views.test2)
]