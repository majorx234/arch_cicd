# Info
- WIP - nothing useful yet
- build system to build own Archlinux package

# References
- Idea taken from `abs_cd`
  - https://github.com/bionade24/abs_cd

# REST API
- WIP
- just testing
- list packages:
  - `curl -X 'GET' 'http://localhost:8000/rest-list/'`
    - `[{"name":"somepackage","repo_url":"https://github.com/majorx234/somepackage","makepkg_extra_args":"","clean_build":true,"build_status":"NOT_BUILT","build_date":"2025-08-22T00:00:00Z","build_output":"","repo_push":true,"repo_release_push":false,"last_version":""}]`
- get more info:
  - `curl -X 'GET' 'http://localhost:8000/rest-detail/somepackage/'`
- trigger some stuff: (does nothing yet)
  - `curl -X 'GET' 'http://127.0.0.1:8000/cd_manager/buildnow/somepackage/'`
  - `curl -X 'POST' 'http://127.0.0.1:8000/cd_manager/buildnow/somepackage/' -H 'Content-Type: application/json' -d '{"rebuild":"true"}'`
