from django_filters import FilterSet, DateFilter
from bootstrap_datepicker_plus.widgets import DatePickerInput
from cd_manager.models import Package


class PackageFilter(FilterSet):
    build_date__gte = DateFilter(
        field_name='build_date',
        lookup_expr='gte',
        input_formats=["%Y-%m-%d"],
        label='build date...',
        widget=DatePickerInput(
                    options={
                        "format": "YYYY-MM-DD",
                        "showClose": True,
                        "showClear": True,
                        "showTodayButton": True,
                    }
                            ))
    build_date__lte = DateFilter(
        field_name='build_date',
        lookup_expr='lte',
        input_formats=["%Y-%m-%d"],
        label='...end Datum',
        widget=DatePickerInput(
                    options={
                        "format": "YYYY-MM-DD",
                        "showClose": True,
                        "showClear": True,
                        "showTodayButton": True,
                    }
                              ))

    class Meta:
        model = Package
        fields = {
            'name': ['icontains', ],
            'build_status': ['exact', ],
            'repo_url': ['icontains', ],
        }
