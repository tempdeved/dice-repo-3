from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import models

# @admin.register(models.HistoricoAlunoPre)
# class HistoricoAlunoPre(admin.ModelAdmin):
#     fields = ('id', 'created_at') #campos para cadastrar
#     # list_display = ()
#     # grid de visualizações
#     # list_filter = ()
#     # search_fields = ()
#     # filter_horizontal = ('aluno',)
#     pass
# Register your models here.
@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'nome_completo',
        'funcao',
        'status',
        'telefone1',
        'telefone2',
        'email',
        'foto',
    ) # grid de visualizações
    # list_filter = ()
    # search_fields = ()
    # filter_horizontal = ('aluno',)
    pass


@admin.register(models.Aluno)
class AlunoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'id',
        'full_name',
        'status',
        'dat_nasc',
        'mes_nascimento',
        'bairro',
        'nome_mae',
        'nome_pai',
        'foto',
    ) # grid de visualizações
    # list_filter = ()
    search_fields = (
        'id',
        'nome',
        'status',
        'dat_nasc',
        'bairro',
        'nome_mae',
        'nome_pai',
    )
    # filter_horizontal = ('aluno',)
    pass


@admin.register(models.Horario)
class HorarioAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'dia_semana',
        'hr_turma',
    ) # grid de visualizações
    # list_filter = ()
    # search_fields = ()
    # filter_horizontal = ('aluno',)

    @admin.display(description='Hora')
    def v_hora(self, obj):
        return f'{obj.hora_inicio}:{obj.min_inicio}-' \
           f'{obj.hora_fim}:{obj.min_fim}'
    pass


@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'v_created_at',
        'numero_turma',
        'professor',
        'coordenador',
        'semestre',
        'numero_turma',
        # 'v_hr_turma',
        '_horario',
        'status',
    )

    # grid de visualizações
    # list_filter = (
    #     'created_at',
    #     'status',
    # )

    # search_fields = ()
    filter_horizontal = ('aluno', 'hr_turma')

    @admin.display(description='Ano')
    def v_created_at(self, obj):
        return f'{obj.created_at.year}'

    # @admin.display(description='Dia Semana')
    # def dia_semana(self, obj):
    #     return f'{obj.dia_semana}'

    @admin.display(description='Hora')
    def v_hr_turma(self, obj):
        try:
            # result = obj.hr_turma.select_related()
            result = obj.hr_turma.all()
            a = []
            for i in result:
                # a = f'{i.dia_semana} '
                a.append(
                        f'{i.dia_semana} de '
                        f'{i.hora_inicio.zfill(2)}:{i.min_inicio.zfill(2)} até '
                        f'{i.hora_fim.zfill(2)}:{i.hora_fim.zfill(2)} '
                        f'({i.duracao_min.zfill(2)} min) '
                )
            return str(a)
            # return f'{self.hr_turma.hora_inicio}:{self.min_inicio} - ' \
            #        f'{self.hora_fim}:{self.min_fim}'
        except:
            return f'Não Cadastrado'

    pass


@admin.register(models.HistoricoAluno)
class HistoricoAlunoAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'v_created_at',
        'v_week_at',
        'aluno',
        'research_01',
        'research_02',
        'organization_01',
        'organization_02',
        'interest_01',
        'interest_02',
        'group_activity_01',
        'group_activity_02',
        'speaking_01',
        'speaking_02',
        'frequencia_of_01',
        'frequencia_of_02',
        'listening_01',
        'listening_02',
        'readind_inter_01',
        'readind_inter_02',
        'writing_process_01',
        'writing_process_02',
        'frequencia_pct',
        'descricao',
        'media_final',
        # 'media_final',

    ) # grid de visualizações
    # list_filter = ()
    search_fields = (
        'v_created_at',
        'v_week_at',
        'aluno',
    )

    @admin.display(description='Turma')
    def v_created_at(self, obj):
        return f'{obj.turma.created_at.year}-{obj.turma.created_at.month}'

    @admin.display(description='Horário')
    def v_week_at(self, obj):
        return f'{obj.turma}'

    @admin.display(description='Média')
    def v_media(self, obj):
        return f'{obj.media_final}'

    # filter_horizontal = ('aluno',)
    pass