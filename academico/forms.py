from django.forms import ModelForm
from django import forms
from django.contrib import admin
from . import models


class AlunoForm(ModelForm):
    class Meta:
        model = models.Aluno
        fields = '__all__'


class HorarioForm(ModelForm):
    class Meta:
        model = models.Horario
        fields = '__all__'


class HorarioUpdateForm(ModelForm):
    class Meta:
        # model = models.Horario.objects.get(pk)
        model = models.Horario
        fields = '__all__'


class TurmaForm(forms.Form):
    semestre = forms.IntegerField(min_value=1, max_value=2)
    horario_query = models.Horario.objects.values(
        'dia_semana',
        'hora_inicio',
        'min_inicio',
        'hora_fim',
        'hora_fim',
        'duracao_min',
    )

    horario_list = []

    for i in horario_query:
        horario_list.append(
            ['dia_semana', f'{i["dia_semana"]} de '
                           f'{i["hora_inicio"].zfill(2)}:{i["min_inicio"].zfill(2)} até '
                           f'{i["hora_fim"].zfill(2)}:{i["hora_fim"].zfill(2)} '
                           f'({i["duracao_min"].zfill(2)} min) '
             ]
        )

    horario = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=horario_list,
    )



    # ModelMultipleChoiceField
