from django.urls import path
# from django.conf.urls import urls

from .views import MainView, PackageCreateView, \
                   PackageListView, PackageDetailView, \
                   PackageRestDetailView, PackageRestListView \


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('create/', PackageCreateView.as_view(), name='create'),
    path('detail/<pk>/', PackageDetailView.as_view(), name='detail'),
    path('rest-detail/<pk>/', PackageRestDetailView.as_view(), name='rest-detail'),
    path('list/', PackageListView.as_view(), name='list'),
    path('rest-list/', PackageRestListView.as_view(), name='rest-list'),
]
