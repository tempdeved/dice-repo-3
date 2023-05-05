from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from . import models
from . import forms

TEXT_LOGIN = 'faça login'


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        result = {
            'hello': TEXT_LOGIN,
            'div_teste': '',
        }

        response = render(
            request=request,
            # template_name='registration/login.html',
            template_name='index.html',
            context=result,
        )

        return response
    else:
        result = {
            'hello': f'Olá, {request.user}',
            'div_teste': '',
        }

        response = render(
            request=request,
            # template_name='registration/login.html',
            template_name='index.html',
            context=result,
        )

        return response


def alunos(request):
    if not request.user.is_authenticated:
        result = {
            'hello': TEXT_LOGIN,
            'div_teste': '',
        }

        response = render(
            request=request,
            # template_name='registration/login.html',
            template_name='index.html',
            context=result,
        )

        return response
    else:
        alunos = models.Aluno.objects.all()

        result = {
            'alunos': alunos,
        }

        response = render(
            request=request,
            template_name='alunos.html',
            context=result,
        )

        return response


def aluno_novo(request):
    form = forms.AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('alunos')




def aluno(request):
    result = {
        'hello': 'ola mundo, home',
        'div_teste': 'teste-div',
    }

    response = render(
        request=request,
        # template_name='registration/login.html',
        template_name='aluno.html',
        context=result,
    )
    return response


# def aluno_id(request, id):
#     request = f'ola, ID: {id}'
#     response = HttpResponse(request)

from django.views import generic
from django.shortcuts import get_object_or_404

def aluno_id(request, id):
    aluno = get_object_or_404(models.Aluno, pk=id)
    form = forms.AlunoSearch()

    result = {
        'form_search': form,
        'aluno': aluno
    }

    response = render(
        request=request,
        template_name='aluno_detalhe.html',
        context=result,
    )

    return response
    # return render(request, 'aluno_detalhe.html', context={'aluno': aluno})


class Aluno():

    def __init__(self):
        pass

    def form(self):
        pass

    def update_form(self):
        pass

    def update(self):
        pass

    def create(self, request):
        if not request.user.is_authenticated:
            result = {
                'hello': TEXT_LOGIN,
                'div_teste': '',
            }

            response = render(
                request=request,
                # template_name='registration/login.html',
                template_name='index.html',
                context=result,
            )

            return response
        else:
            form = forms.AlunoForm()

            result = {
                'form': form
            }

            response = render(
                request=request,
                template_name='aluno_create.html',
                context=result,
            )

            return response


    def list(self):
        pass


class Horario():

    def __init__(self):
        pass

    def form(self, request):
        if not request.user.is_authenticated:
            result = {
                'hello': TEXT_LOGIN,
                'div_teste': '',
            }

            response = render(
                request=request,
                # template_name='registration/login.html',
                template_name='index.html',
                context=result,
            )

            return response
        else:
            form = forms.HorarioForm()

            result = {
                'form': form
            }

            response = render(
                request=request,
                template_name='horario_form.html',
                context=result,
            )

            return response

    def update_form(self, request, pk):
        # form = forms.HorarioUpdateForm(pk)

        post = models.Horario.objects.get(id=pk)
        if request.method == "POST":
            form = forms.HorarioUpdateForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('home:detalhes', pk=post.hr_turma)
        else:
            form = forms.HorarioUpdateForm(instance=post)
        return render(request, 'horario_update_form.html', {'form': form})

    def update(self, request):
        form = forms.HorarioForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('home')

    def create(self, request):
        form = forms.HorarioForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('home')

    def list(elf, request):
        if not request.user.is_authenticated:
            result = {
                'hello': TEXT_LOGIN,
                'div_teste': '',
            }

            response = render(
                request=request,
                # template_name='registration/login.html',
                template_name='index.html',
                context=result,
            )

            return response
        else:
            horario = models.Horario.objects.all()

            result = {
                'horarios': horario,
            }

            response = render(
                request=request,
                template_name='horarios.html',
                context=result,
            )

            return response


class Turmas():
    def __init__(self):
        pass

    # @login_required()
    def list(rself, request):
        if not request.user.is_authenticated:
            result = {
                'hello': TEXT_LOGIN,
                'div_teste': '',
            }

            response = render(
                request=request,
                # template_name='registration/login.html',
                template_name='index.html',
                context=result,
            )

            return response
           # return redirect(to='home')
        else:
            turmas = models.Turma.objects.all()

            result = {
                'turmas': turmas
            }

            response = render(
                request=request,
                template_name='turmas.html',
                context=result,
            )

            return response

    def form(self, request):
        if not request.user.is_authenticated:
            result = {
                'hello': TEXT_LOGIN,
                'div_teste': '',
            }

            response = render(
                request=request,
                # template_name='registration/login.html',
                template_name='index.html',
                context=result,
            )

            return response
        else:
            # form = forms.TurmaForm()
            form = forms.TurmaForm2()

            result = {
                'form': form
            }

            response = render(
                request=request,
                template_name='turma_form.html',
                context=result,
            )

            return response

    def create(self, request):
        form = forms.HorarioForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('home')


class Funcionario():

    def __init__(self):
        pass

    def auth(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            ...
        pass

    def log_out(self, request):
        logout(request)
        pass


def funcionarios(request):
    if not request.user.is_authenticated:
        result = {
            'hello': TEXT_LOGIN,
            'div_teste': '',
        }

        response = render(
            request=request,
            # template_name='registration/login.html',
            template_name='index.html',
            context=result,
        )

        return response
    else:
        funcionarios = models.Funcionario.objects.all()

        result = {
            'funcionarios': funcionarios
        }

        for i in funcionarios:
            print(f'kkkkk - {i}')

        response = render(
            request=request,
            template_name='funcionarios.html',
            context=result,
        )

        return response
