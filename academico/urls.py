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

                  path('alunos/', views.alunos, name='alunos'),
                  path('turmas/', views.Turmas().list, name='turmas'),
                  path('funcionarios/', views.funcionarios, name='funcionarios'),
                  path('horarios', views.Horario().list, name='horarios'),

                  path('turma/form', views.Turmas().form, name='turma-form'),
                  path('funcionario/form', views.Funcionario().form, name='funcionario-form'),
                  path('horario/form', views.Horario().form, name='horario-form'),
                  path('aluno/create', views.Aluno().create, name='aluno-create'),

                  path('aluno-novo/', views.aluno_novo, name='aluno-novo'),
                  path('turma-novo/', views.Turmas().create, name='turma-novo'),
                  path('funcionario-novo', views.Funcionario().create, name='funcionario-novo'),
                  path('horario-novo/', views.Horario().create, name='horario-novo'),

                  path('aluno/<int:id>', views.aluno_id, name='aluno-detail'),
                  path('turma/<int:id>', views.Turmas().detail, name='turma-detail'),

                  path('aluno-update/<int:id>', views.Aluno().update, name='aluno-update'),
                  path('funcionario-update/<int:id>', views.Funcionario().update, name='funcionario-update'),
                  path('horario-update/<int:id>', views.Horario().update, name='horario-update'),
                  path('turma-update/<int:id>', views.Turmas().update, name='turma-update'),

                  path('horario-update-form/<int:pk>', views.Horario().update_form, name='horario-update-form'),
                  # path('horario-update/', views.Horario().update, name='horario-update'),

                  path('aluno-search-name/', views.Aluno().search_name, name='aluno-search-name'),

                  path('aluno-pdf/<int:id>', views.Aluno().pdf, name='aluno-pdf'),


              ] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

