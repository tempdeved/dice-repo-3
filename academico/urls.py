"""dice9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('aluno', views.aluno, name='aluno'),
    path('aluno/create', views.aluno_create, name='aluno-create'),
    path('aluno-novo/', views.aluno_novo, name='aluno-novo'), # path usado pelo 'alunos/' para cadastrar novo aluno


    path('alunos/', views.alunos, name='alunos'),

    path('turmas/', views.Turmas().list, name='turmas'),
    path('turma/form', views.Turmas().form, name='turma-form'),
    path('turma-novo/', views.Turmas().create, name='turma-create'),

    path('funcionarios/', views.funcionarios, name='funcionarios'),

    path('horarios', views.Horario().list, name='horarios'),
    path('horario/form', views.Horario().form, name='horario-form'),
    path('horario-novo/', views.Horario().create, name='horario-novo'),
    path('horario-update-form/<int:pk>', views.Horario().update_form, name='horario-update-form'),
    path('horario-update/', views.Horario().update, name='horario-update'),

] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

