from django.views.generic import CreateView, DetailView, \
                                 UpdateView, ListView
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from rest_framework import generics

from cd_manager.models import Package
from cd_manager.forms import PackageForm
from cd_manager.tables import PackageTable
from cd_manager.filters import PackageFilter
from cd_manager.serializers import PackageSerializer


class PackageCreateView(CreateView):
    # permission_required = 'cd_manager.add_package'
    model = Package
    template_name = 'create.html'
    form_class = PackageForm
    # success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['METHOD'] = 'create'
        return context


class PackageCreateRestView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class PackageDetailView(DetailView):
    # permission_required = 'cd_manager.view_packages'
    model = Package
    template_name = 'detail.html'


class PackageRestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class PackageListView(SingleTableMixin, FilterView):
    # permission_required = 'cd_manager.view_packages'
    template_name = 'list.html'
    model = Package
    filterset_class = PackageFilter
    table_class = PackageTable


class PackageRestListView(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class MainView(SingleTableMixin, FilterView):
    filterset_class = PackageFilter
    template_name = 'cicd_overview.html'
    model = Package
    table_class = PackageTable
