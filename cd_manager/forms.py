from django.forms import ModelForm
from cd_manager.models import Package


class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = (
            'name',
            'repo_url',
            'makepkg_extra_args',
            'clean_build',
            'repo_push',
            'repo_release_push',
        )

    def print_package(self):
        print("print_package(): here")
        pass
