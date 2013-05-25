source /home/workspace-django/virtualenvs/ironika-calosso/bin/activate
cd /home/workspace-django/projects/ironika-calosso/calosso/
fab live prepare_deploy
fab live deploy
deactivate
