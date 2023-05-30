import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
#
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View
import csv

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)
#
from . import models
from . import forms

TEXT_LOGIN = 'faça login'

def not_auth(request):
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
        alunos = models.Aluno.objects.all()[:100]
        # alunos = models.Aluno.objects.all().filter(nome__icontains='JOAO')
        now = datetime.datetime.now()
        result = {
            'alunos': alunos,
            'now': f'{now.year}-{str(now.month).zfill(2)}'
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

from django.shortcuts import get_object_or_404

def aluno_id(request, id):
    aluno = models.Aluno.objects.get(id=id)
    # aluno = get_object_or_404(models.Aluno, pk=id)
    alunos_ativos = models.Aluno.objects.all()
    turmas_ativa = models.Turma.objects.filter(aluno=id, status='ativa')
    turmas_encerradas = models.Turma.objects.all().filter(aluno=id).exclude(status='ativa')

    # form = forms.AlunoSearch()

    result = {
        'alunos_ativos': alunos_ativos,
        'aluno': aluno,
        'turmas_ativa': turmas_ativa, #aluno pode estar em duas turmas ativas? se sim... fazer loop no template
        'turmas_encerradas': turmas_encerradas, #aluno pode estar em duas turmas ativas? se sim... fazer loop no template
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

    def search(self, request):

        nome = request.GET.get("nome")
        bday = request.GET.get("bday")
        pdf = request.GET.get("pdf")


        if nome is not None:
            alunos = models.Aluno.objects.all().filter(nome__icontains=nome)
        elif pdf == 'PDF':
            alunos = models.Aluno.objects.all().filter(
                dat_nasc__year=bday[:4],
                dat_nasc__month=bday[5:],
            )
            result = {
                'alunos': alunos,
            }

            # esse RENDER é do gerador de PDF e não do Django
            response = Render.render(
                path='aniversariantes_pdf.html',
                params=result,
                filename=f'aniversariantes_{bday[:4]}_{bday[:2]}'
            )
            return response
        elif bday is not None:
            alunos = models.Aluno.objects.all().filter(
                dat_nasc__year=bday[:4],
                dat_nasc__month=bday[5:],
            )
        else:
            alunos = models.Aluno.objects.all()[:10]

        now = datetime.datetime.now()
        result = {
            'alunos': alunos,
            'now': f'{now.year}-{str(now.month).zfill(2)}'
        }

        response = render(
            request=request,
            template_name='alunos.html',
            context=result,
        )

        return response


    def pdf_aluno_detalhe(self, request, id):

        aluno = models.Aluno.objects.get(id=id)
        turmas_ativa = models.Turma.objects.filter(aluno=id, status='ativa')
        turmas_encerradas = models.Turma.objects.all().filter(aluno=id).exclude(status='ativa')

        result = {
            'aluno': aluno,
            'turmas_ativa': turmas_ativa,
            'turmas_encerradas': turmas_encerradas,
        }

        # esse RENDER é do gerador de PDF e não do Django
        response = Render.render(
            path='aluno_pdf.html',
            params=result,
            filename='relatorio_aluno'
        )
        return response
    def pdf_aniversariantes(self, request, bday):

        alunos = models.Aluno.objects.all().filter(
            dat_nasc__year=bday[:4],
            dat_nasc__month=bday[5:],
        )
        result = {
            'alunos': alunos,
        }

        # esse RENDER é do gerador de PDF e não do Django
        response = Render.render(
            path='aniversariantes.html',
            params=result,
            filename=f'aniversariantes_{bday[:4]}_{bday[:2]}'
        )
        return response

    def update(self, request, id):

        post = models.Aluno.objects.get(id=id)
        form = forms.AlunoForm(request.POST or None, instance=post)

        result = {
            'aluno': post,
            'form': form,
        }

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('alunos')
        else:
            return render(request, 'aluno_update_form.html', result )


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
                template_name='aluno_form.html',
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

    def update(self, request, id):

        post = models.Horario.objects.get(id=id)
        form = forms.HorarioForm(request.POST or None, instance=post)

        data = {
            'horario': post,
            'form': form,
        }

        if request.method == "POST":
            if form.is_valid():
                # post = form.save(commit=False)
                # post.save()
                form.save()
                return redirect('horarios')
        else:
            return render(request, 'horario_update_form.html', data )

    def create(self, request):
        form = forms.HorarioForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('horario-form')

    def list(elf, request):
        if not request.user.is_authenticated:
            response = not_auth(request)
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
        now = datetime.datetime.now()

        if not request.user.is_authenticated:
            response = not_auth(request)
            return response
           # return redirect(to='home')
        else:
            if request.method == "POST":
                print(request)
                year = now.year if request.POST['ano'] == '' else request.POST['ano']
                status = request.POST['status']

                if (year is not None) and (status is not None):

                    if status == 'todas':
                        turmas = models.Turma.objects.all().filter(
                            created_at__year=year,
                         )
                    else:
                        turmas = models.Turma.objects.all().filter(
                            created_at__year=year,
                            status=status
                        )

                elif (year is None) and (status is not None):
                    turmas = models.Turma.objects.all().filter(
                        status=status
                    )
                else:
                    turmas = models.Turma.objects.all().filter(
                        status=status
                    )[:10]

            else:
                turmas = models.Turma.objects.all()

            result = {
                'turmas': turmas,
                'now': f'{now.year}'
            }

            response = render(
                request=request,
                template_name='turmas.html',
                context=result,
            )

            return response

    def form(self, request):
        if not request.user.is_authenticated:
            response = not_auth(request)
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
        form = forms.TurmaForm2(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('turmas')

    def detail(self, request, id):

        if request.method == "POST":
            print(request)
            # request.POST['id']
            pass
        # else:
        # result_query = get_notas(models.Turma, pk=id)
        # if len(result_query) <= 0:
        result_query = get_object_or_404(models.Turma, pk=id)

        from django import forms
        HistoricoAlunoFormset = forms.modelformset_factory(
            models.HistoricoAluno,
            # models.HistoricoAluno.objects.all().filter(
            #         id=id
            #     ),
            fields=("turma", "aluno", 'numero_aulas'),
            # extra=0, can_delete=True
        )

        formset = HistoricoAlunoFormset(
            initial=[
                {
                    'title': 'Django is now open source',
                }
            ]
        )

        data = {
            'turma': result_query,
            'formset': formset
        }

        response = render(
            request=request,
            template_name='turma_detalhe.html',
            context=data,
        )

        return response

    def update(self, request, id):

        post = models.Turma.objects.get(id=id)
        form = forms.TurmaForm2(request.POST or None, instance=post)

        data = {
            'turma': post,
            'form': form,
        }

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('turmas')
        else:
            return render(request, 'turma_update_form.html', data )

    def search(self, request):

        year = request.GET.get("ano")
        status = request.GET.get("status")
        # pdf = request.GET.get("pdf")


        if (year is not None) and (status is not None):
            turmas = models.Turma.objects.all().filter(
                created_at__year=year,
                status=status
            )

        elif (year is None) and (status is not None):
            turmas = models.Turma.objects.all().filter(
                status=status
            )
        else:
            turmas = models.Turma.objects.all().filter(
                status=status
            )[:10]

        now = datetime.datetime.now()
        result = {
            'turmas': turmas,
            'now': f'{now.year}'
        }

        response = render(
            request=request,
            template_name='turmas.html',
            context=result,
        )

        return response

    def nota(self, request):

        print(request)
        print(request.POST)
        print(request.POST['id'])
        print(request.POST['turma'])
        # print(request.POST.turma)

        id = request.POST["id"]
        research_01 = request.POST["research_01"]
        turma = request.POST["turma"]
        organization_01 = request.POST["organization_01"]

        # result_query = get_object_or_404(models.Turma, pk=id)
        turma = models.Turma.objects.get(id=turma)
        historico = models.HistoricoAluno.objects.all().filter(
            aluno__id=id,
        )

        data = {
            'turma': turma,
            'research_01': research_01
        }

        response = render(
            request=request,
            template_name='turma_detalhe.html',
            context=data,
        )

        return response


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
            form = forms.FuncionarioForm()

            result = {
                'form': form
            }

            response = render(
                request=request,
                template_name='funcionario_form.html',
                context=result,
            )

            return response

    def create(self, request):
        form = forms.FuncionarioForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('funcionarios')

    def update(self, request, id):

        post = models.Funcionario.objects.get(id=id)
        form = forms.FuncionarioForm(request.POST or None, instance=post)

        data = {
            'funcionario': post,
            'form': form,
        }

        if request.method == "POST":
            if form.is_valid():
                # post = form.save(commit=False)
                # post.save()
                form.save()
                return redirect('funcionarios')
        else:
            return render(request, 'funcionario_update_form.html', data )



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


######




class Pdf(View):

    def get(self, request):
        veiculos = Aluno.objects.all()
        params = {
            'alunos': veiculos,
            'request': request,
        }
        return Render.render('relatorio_alunos_turma.html', params, 'relatorio_alunos_turma')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        veiculos = Aluno.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'placa', 'Proprietario', 'Cor'])

        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario,
                 veiculo.cor
                 ])

        return response