from django.forms import ModelForm
from django import forms
from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
from import_export.forms import ImportExportFormBase
from import_export.forms import ImportForm

BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
STATUS_CHOICE = [
    ('ativa', 'ativa'),
    ('encerrada', 'encerrada')
]
FAVORITE_COLORS_CHOICES = [
    ("blue", "Blue"),
    ("green", "Green"),
    ("black", "Black"),
]


# class AlunoForm(ImportForm):
class AlunoForm(ModelForm):
    class Meta:
        model = models.Aluno
        fields = '__all__'


class AlunoSearch(ModelForm):
    # aluno_query = models.Funcionario.objects.values(status='ativo')
    class Meta:
        model = models.Aluno
        fields = ('nome', )
    # aluno_id = forms.(label="aluno_id", max_length=100)
    # class Meta:
    #     model = models.Aluno
    #     fields = '__all__'


class HorarioForm(ModelForm):
    class Meta:
        model = models.Horario
        fields = '__all__'


class HorarioUpdateForm(ModelForm):
    class Meta:
        # model = models.Horario.objects.get(pk)
        model = models.Horario
        fields = '__all__'

class FuncionarioForm(ModelForm):
    class Meta:
        # model = models.Horario.objects.get(pk)
        model = models.Funcionario
        fields = '__all__'


class TurmaForm2(ModelForm):
    class Meta:
        # model = models.Horario.objects.get(pk)
        model = models.Turma
        fields = '__all__'


class TurmaForm(forms.Form):
    #
    # FK HORARIO
    #
    # formating labels
    horario_query = models.Horario.objects.values(
        'dia_semana',
        'hora_inicio',
        'min_inicio',
        'hora_fim',
        'hora_fim',
        # 'duracao_min',
    )

    horario_list = []
    try:
        for i in horario_query:
            horario_list.append(
                ['dia_semana', f'{i["dia_semana"]} de '
                               f'{i["hora_inicio"].zfill(2)}:{i["min_inicio"].zfill(2)} até '
                               f'{i["hora_fim"].zfill(2)}:{i["hora_fim"].zfill(2)} '
                               f'({i["duracao_min"].zfill(2)} min) '
                 ]
            )
    except Exception as err:
        print(err)

    #
    # FK PROFESSOR
    #


    # professor_query = models.Funcionario.objects.all()
    professor_query = models.Funcionario.objects.values(
    # professor_query = models.Funcionario.objects.filter(
    #     funcao='professor'
        # 'id',
        # 'nome_completo',
        # 'status',
        # 'funcao',
    )

    professor_list = []
    try:
        for i in professor_query:
            if i["funcao"] == 'professor':
                prof = f'Professor: {i["nome_completo"]} - {i["status"]} - {i["funcao"]}'.upper()
                professor_list.append(
                    (i['id'], prof)
                )
    except Exception as err:
        print(err)

    # labels
    semestre = forms.IntegerField(min_value=1, max_value=2)
    numero_turma = forms.IntegerField()

    status = forms.MultipleChoiceField(
        required=False,
        widget=forms.Select,
        choices=STATUS_CHOICE
    )
    professor = forms.MultipleChoiceField(
        required=False,
        widget=forms.Select,
        choices=professor_list
    )
    horario = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=horario_list,
    )


    # senha3 = forms.CharField()
    # senha3 = forms.CharField(widget=forms.PasswordInput)


    # ModelMultipleChoiceField
