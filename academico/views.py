from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms

# Create your views here.
def home(request):

    result = {
        'hello': 'ola mundo, home',
        'div_teste': 'teste-div',
    }

    response = render(
        request=request,
        # template_name='registration/login.html',
        template_name='index.html',
        context=result,
    )

    return response


def aluno_create(request):

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


class Horario():

    def __init__(self):
        pass

    def form(self, request):
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


def alunos(request):

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


class Turmas():
    def __init__(self):
        pass

    def list(rself, request):

        turmas = models.Turma.objects.all()

        result = {
            'turmas': turmas
        }

        for i in turmas:
            print(f'kkkkk - {i.semestre}')

        response = render(
            request=request,
            template_name='turmas.html',
            context=result,
        )

        return response

    def form(self, request):
        form = forms.TurmaForm()

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

def funcionarios(request):

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


def aluno_id(request, id):
    request = f'ola, ID: {id}'
    response = HttpResponse(request)
    return response
