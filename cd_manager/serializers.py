from rest_framework import serializers

from cd_manager.models import Package


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ('name',
                  'repo_url',
                  'makepkg_extra_args',
                  'clean_build',
                  'build_status',
                  'build_date',
                  'build_output',
                  'repo_push',
                  'repo_release_push')
