from django.forms import ModelForm, DateField
from cd_manager.models import Package
from bootstrap_datepicker_plus.widgets import DatePickerInput


class PackageForm(ModelForm):
    # not needed just for testing
    build_date = DateField(input_formats=["%Y-%m-%d"], label="build_date",
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
        fields = (
            'name',
            'repo_url',
            'makepkg_extra_args',
            'clean_build',
            'build_status',
            'build_date',
            'build_output',
            'repo_push',
            'repo_release_push',
        )

    def print_package(self):
        print("print_package(): here")
        pass
