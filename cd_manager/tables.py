from django_tables2 import Table, Column
from django.utils.html import format_html

from cd_manager.models import Package


class PackageTable(Table):
    id = Column(visible=False)
    #name = Column(visible=False)

    def render_name(self, record, value):
        url = Package.objects.get(pk=record.name).get_absolute_url()
        print(url)
        html = format_html('<a href="{}">{}</a>', url, value)
        return html

    class Meta:
        model = Package
        per_page = 20
        order_by = ('name',)
        attrs = {"class": "table table-striped",
                 "thead": {
                     "class": "thead-light"
                    }
                 }
