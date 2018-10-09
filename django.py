from fabric.api import *

env.user = 'root'
env.hosts = ['xx.xx.xx.xx']

@task
def install_django():
    run('pip install django==1.11')
    run('exit')

@task
def create_project(project_name):
    run('django-admin startproject %s' % project_name)
    with cd(project_name):
        run('django-admin startapp webapps')

@task
def runserver(project_name):
    with cd(project_name):
        run('python manage.py runserver 0.0.0.0:8000')

@task
def one_stop_service():
    install_django()
    create_project('test_django')
    runserver()
