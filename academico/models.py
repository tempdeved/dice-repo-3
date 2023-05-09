import datetime
from django.db import models
from django.contrib import admin
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


# Create your models here.
class Aluno(models.Model):
    id = models.AutoField(primary_key=True,)
    created_at = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=100, blank=True, null=True, default='')
    nome_do_meio = models.CharField(max_length=100, blank=True, null=True, default='')
    ultimo_nome = models.CharField(max_length=100, blank=True, null=True, default='')
    status_choice = (
        ('ativo', 'ativo'),
        ('encerrado', 'encerrado'),
        ('trancado', 'trancado'),
        ('jubilado', 'jubilado'),
        ('cancelado', 'cancelado'),
    )
    status = models.CharField(max_length=100, blank=True, null=True, default='', choices=status_choice)

    dat_nasc = models.DateField( blank=True, null=True, default='')
    mes_nasc_choice = (
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )
    # mes_nascimento = models.IntegerField( blank=True, null=True, default='', choices=mes_nasc_choice )
    cidade_nascimento = models.CharField(max_length=100, blank=True, null=True, default='')
    endereco = models.CharField(max_length=200, blank=True, null=True, default='')
    numero = models.IntegerField( blank=True, null=True, default='')
    complemento = models.CharField(max_length=100, blank=True, null=True, default='')
    bairro = models.CharField(max_length=100, blank=True, null=True, default='')
    cidade = models.CharField(max_length=100, blank=True, null=True, default='')
    uf = models.CharField(max_length=5, blank=True, null=True, default='')
    cep = models.CharField(max_length=100, blank=True, null=True, default='')
    telefone1 = models.CharField(max_length=20, blank=True, null=True, default='')
    moradia = models.CharField(max_length=100, blank=True, null=True, default='')
    inicio = models.DateField( blank=True, null=True, default='')
    n_irmaos = models.IntegerField( blank=True, null=True, default='')
    retorno = models.DateField( blank=True, null=True, default='')
    sexo_choice = (
        ('M', 'M'),
        ('F', 'F'),
    )
    sexo = models.CharField(max_length=100, blank=True, null=True, default='', choices=sexo_choice)
    responsavel_financeiro = models.CharField(max_length=100, blank=True, null=True, default='')
    tel_responsavel_financeiro = models.CharField(max_length=20, blank=True, null=True, default='')
    responsavel_p_filhos = models.CharField(max_length=100, blank=True, null=True, default='')
    bairro_de_ida = models.CharField(max_length=100, blank=True, null=True, default='')
    bairro_de_volta = models.CharField(max_length=100, blank=True, null=True, default='')
    enviar_boleto = models.BooleanField( blank=True, null=True, default=False)
    gerar_taxa = models.BooleanField( blank=True, null=True, default=False)
    bolsista = models.BooleanField( blank=True, null=True, default=False)

    nome_pai = models.CharField(max_length=100, blank=True, null=True, default='')
    email_pai = models.EmailField(blank=True, null=True, default='')
    celular_pai = models.CharField(max_length=20, blank=True, null=True, default='')
    tel_trabalho_pai = models.CharField(max_length=20, blank=True, null=True, default='')
    cpf_pai = models.CharField(max_length=100, blank=True, null=True, default='')
    profissao_pai = models.CharField(max_length=100, blank=True, null=True, default='')

    nome_mae = models.CharField(max_length=100, blank=True, null=True, default='')
    email_mae = models.EmailField(blank=True, null=True, default='')
    celular_mae = models.CharField(max_length=20, blank=True, null=True, default='')
    tel_trabalho_mae = models.CharField(max_length=20, blank=True, null=True, default='')
    cpf_mae = models.CharField(max_length=100, blank=True, null=True, default='')
    profissao_mae = models.CharField(max_length=100, blank=True, null=True, default='')

    senha = models.CharField(max_length=100, blank=True, null=True, default='')
    foto = models.ImageField(upload_to='images', blank=True, null=True,)

    @admin.display(description='Nome Completo')
    def full_name(self):
        return f'{self.nome} {self.nome_do_meio} {self.ultimo_nome}'

    @admin.display(description='Mês Nasc')
    def mes_nascimento(self):
        try:
            return f'{self.dat_nasc.month}'
        except:
            return f'Não Cadastrado'

    def get_absolute_url(self):
        """Retorna o URL para acessar uma instância específica do modelo."""
        return reverse('aluno-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.nome} {self.ultimo_nome}'.upper()


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True,)
    created_at  = models.DateField(auto_now_add=True)

    nome_completo = models.CharField(max_length=100, blank=True, null=True, default='')
    status_choices = (
        ('contratado', 'contratado'),
        ('contrato encerrado', 'contrato encerrado'),
    )
    status = models.CharField(max_length=100, blank=True, null=True, default='', choices=status_choices)
    funcao_choices = (
        ('gerente', 'gerente'),
        ('recepção', 'recepção'),
        ('professor', 'professor'),
    )
    funcao = models.CharField(max_length=30 , blank=True, null=True, default='', choices=funcao_choices)  # [1=gerente, 2=recep, 3=professor]
    senha = models.CharField(max_length=100, blank=True, null=True, default='')
    telefone1 = models.CharField(max_length=20, blank=True, null=True, default='')
    telefone2 = models.CharField(max_length=20, blank=True, null=True, default='')
    dat_nasc = models.DateField( blank=True, null=True, default='')
    cc = models.CharField(max_length=100, blank=True, null=True, default='')
    cart_profis = models.CharField(max_length=100, blank=True, null=True, default='')
    rg = models.CharField(max_length=100, blank=True, null=True, default='')
    endereco = models.CharField(max_length=200, blank=True, null=True, default='')
    numero = models.IntegerField( blank=True, null=True, default='')
    complemento = models.CharField(max_length=100, blank=True, null=True, default='')
    bairro = models.CharField(max_length=100, blank=True, null=True, default='')
    cidade = models.CharField(max_length=100, blank=True, null=True, default='')
    uf = models.CharField(max_length=5, blank=True, null=True, default='')
    cep = models.CharField(max_length=100, blank=True, null=True, default='')
    email = models.EmailField(blank=True, null=True, default='')
    foto = models.ImageField(upload_to='images', blank=True, null=True,)

    def _str_(self):
        return f'{self.id}: {self.nome_completo} - {self.funcao} - {self.status}'.upper()

    def __str__(self):
        return f'{self.nome_completo} - {self.funcao}'


class Horario(models.Model):
    id = models.AutoField(primary_key=True,)
    dia_semana_choice = (
        ('segunda-feira', 'segunda-feira'),
        ('terça-feira', 'terça-feira'),
        ('quarta-feira', 'quartada-feira'),
        ('quinta-feira', 'quintaa-feira'),
        ('sexta-feira', 'sextaa-feira'),
        ('sábado-feira', 'sábadoda-feira'),
        ('domingo-feira', 'domingoa-feira'),
    )
    dia_semana = models.CharField(max_length=30, blank=True, null=True, default='', choices=dia_semana_choice)
    hora_ini_choice = (
        (f'{x}', f'{x}')
        for x in range(0, 24)
    )
    hora_fim_choice = (
        (f'{x}', f'{x}')
        for x in range(0, 24)
    )
    min_ini_choice = (
        (f'{x}', f'{x}')
        for x in range(0, 60)
    )
    min_fim_choice = (
        (f'{x}', f'{x}')
        for x in range(0, 60)
    )
    hora_inicio = models.CharField(max_length=2, blank=True, null=True, default='', choices=hora_ini_choice)
    min_inicio = models.CharField(max_length=2, blank=True, null=True, default='', choices=min_ini_choice)
    hora_fim = models.CharField(max_length=2, blank=True, null=True, default='', choices=hora_fim_choice)
    min_fim = models.CharField(max_length=2, blank=True, null=True, default='', choices=min_fim_choice)
    # duracao_min = models.CharField(max_length=2, blank=True, null=True, default='')
    # time_travel = models.TimeField('tempo', null=True, blank=True)
    # duration_travel = models.DurationField('duração', null=True, blank=True)

    def hr_turma(self):
        return f'{self.hora_inicio}:{self.min_inicio} - ' \
               f'{self.hora_fim}:{self.min_fim}'.upper()

    def view_duracao_min(self):
        # ini = datetime.time(int(self.hora_inicio), int(self.min_inicio), 00)
        # fim = datetime.time(int(self.hora_fim.zfill(2)), int(self.min_fim.zfill(2)), 00)

        ini = datetime.datetime(
            datetime.datetime.now().year,
            datetime.datetime.now().month,
            datetime.datetime.now().day,
            00 if self.hora_inicio == None else int(self.hora_inicio.zfill(2)),
            00 if self.min_inicio == None else int(self.min_inicio.zfill(2)),
            00
        )
        fim = datetime.datetime(
            datetime.datetime.now().year,
            datetime.datetime.now().month,
            datetime.datetime.now().day,
            00 if self.hora_fim == None else int(self.hora_fim.zfill(2)),
            00 if self.min_fim == None else int(self.min_fim.zfill(2)),
            00
        )

        delta = int((fim - ini).total_seconds() / 60)

        return delta

    def __str__(self):
        # return f'{self.dia_semana}'.upper()
        return f'{self.dia_semana} | {self.hora_inicio.zfill(2)}:{self.min_inicio.zfill(2)}-' \
           f'{self.hora_fim.zfill(2)}:{self.min_fim.zfill(2)}'.upper()


class Turma(models.Model):
    id = models.AutoField(primary_key=True,)
    created_at = models.DateField(auto_now_add=True)

    # horario = models.ForeignKey(Horario, null=True, on_delete=models.RESTRICT, related_name='horario') # FK horario
    professor = models.ForeignKey(Funcionario, null=True, on_delete=models.RESTRICT, related_name='professor') # FK professor
    coordenador = models.ForeignKey(Funcionario, null=True, on_delete=models.RESTRICT, related_name='coordenador') # FK coordenador
    # cod_turma = models.CharField(max_length=4, blank=True, null=True,)

    semestre_choice = (
        (1, 1),
        (2, 2),
    )
    semestre = models.IntegerField(blank=True, null=True, default=0, choices=semestre_choice)
    # nu_turma = models.IntegerField(blank=True, null=True, default=0)
    numero_turma = models.IntegerField(blank=True, null=True, default=0)
    status_choice = (
        ('ativa', 'ativa'),
        ('encerrada', 'encerrada'),
    )
    status = models.CharField(max_length=100, blank=True, null=True, default='', choices=status_choice)
    escola_choice = (
        ('Dice - Lagoa', 'Dice - Lagoa'),
    )
    escola = models.CharField(max_length=100, blank=True, null=True, default=escola_choice[0], choices=escola_choice)
    # nome = models.CharField(max_length=100, blank=True, null=True, default='')
    observacao = models.CharField(max_length=100, blank=True, null=True, default='')
    # desc = models.CharField(max_length=100, blank=True, null=True, default='') #list ([op beginer I, op beginer II]  )
    descricao = models.CharField(max_length=100, blank=True, null=True, default='') #list ([op beginer I, op beginer II]  )
    nivel_choice = (
        ('op beginer I', 'op beginer I'),
        ('op beginer II', 'op beginer II'),
        ('op beginer III', 'op beginer III'),
        ('op intermediate I', 'op intermediate I'),
        ('op intermediate II', 'op intermediate II'),
        ('op advanced I', 'op advanced I'),
        ('op advanced II', 'op advanced II'),
        ('op advanced III', 'op advanced III'),
        ('op advanced IV', 'op advanced IV'),
        ('simbolico', 'simbolico'),
        ('simbolico intuitivo I', 'simbolico intuitivo I'),
        ('sensório motor II', 'sensório motor II'),

    )
    nivel = models.CharField(max_length=100, blank=True, null=True, default='', choices=nivel_choice) #list ([op beginer I, op beginer II]  )
    inicio = models.DateField(blank=True, null=True, default='')
    fim = models.DateField(blank=True, null=True, default='')
    map = models.CharField(max_length=100, blank=True, null=True, default='') #list ([op beginer I, op beginer II]  )
    idioma = models.CharField(max_length=100, blank=True, null=True, default='') #list ([op beginer I, op beginer II]  )

    hr_turma = models.ManyToManyField(Horario, related_name='horario')  # FK horario)
    aluno = models.ManyToManyField(Aluno,  blank=True, related_name='aluno')  # FK coordenador

    def _horario(self):
        return "\n".join([f'{p}' for p in self.hr_turma.all()])

    def __str__(self):
        return f'{self.created_at.year}-{self.numero_turma}'
               # f'{self.hr_turma.hora_inicio.zfill(2)}:{self.hr_turma.min_inicio.zfill(2)} - ' \
               # f'{self.hr_turma.hora_fim.zfill(2)}:{self.hr_turma.min_fim.zfill(2)}'


class HistoricoAluno(models.Model):
    id = models.AutoField(primary_key=True,)
    created_at = models.DateField(auto_now_add=True)

    turma = models.ForeignKey(Turma, null=True, on_delete=models.RESTRICT)  # FK turma
    aluno = models.ForeignKey(Aluno, null=True, on_delete=models.RESTRICT)  # FK aluno

    numero_aulas = models.IntegerField(blank=True, null=True, default='')
    numero_faltas = models.IntegerField(blank=True, null=True, default='')

    research_01 = models.IntegerField(blank=True, null=True, default='')
    research_02= models.IntegerField(blank=True, null=True, default='')
    organization_01 = models.IntegerField(blank=True, null=True, default='')
    organization_02 = models.IntegerField(blank=True, null=True, default='')
    interest_01 = models.IntegerField(blank=True, null=True, default='')
    interest_02 = models.IntegerField(blank=True, null=True, default='')
    group_activity_01 = models.IntegerField(blank=True, null=True, default='')
    group_activity_02 = models.IntegerField(blank=True, null=True, default='')
    speaking_01 = models.IntegerField(blank=True, null=True, default='')
    speaking_02 = models.IntegerField(blank=True, null=True, default='')
    frequencia_of_01 = models.IntegerField(blank=True, null=True, default='')
    frequencia_of_02 = models.IntegerField(blank=True, null=True, default='')
    listening_01 = models.IntegerField(blank=True, null=True, default='')
    listening_02 = models.IntegerField(blank=True, null=True, default='')
    readind_inter_01 = models.IntegerField(blank=True, null=True, default='')
    readind_inter_02 = models.IntegerField(blank=True, null=True, default='')
    writing_process_01 = models.IntegerField(blank=True, null=True, default='')
    writing_process_02 = models.IntegerField(blank=True, null=True, default='')

    descricao = models.TextField(blank=True, null=True, default='')

    # inicio = models.DateField(blank=True, null=True, default='')
    # def get_aluno(self):
    #     aluno = Aluno.objects.get(id=self.id)
    #     return aluno

    def frequencia_pct(self):
        result = ((self.numero_faltas - self.numero_faltas) * 100) / self.numero_aulas /10
        self.frequencia = result
        return round(result, 2)
        # return f'{result:".0f"}'

    def media_final(self):

        list_of_values = [
            self.research_01,
            self.research_02,
            self.organization_01,
            self.organization_02,
            self.interest_01,
            self.interest_02,
            self.group_activity_01,
            self.group_activity_02,
            self.speaking_01,
            self.speaking_02,
            self.frequencia_of_01,
            self.frequencia_of_02,
            self.listening_01,
            self.listening_02,
            self.readind_inter_01,
            self.readind_inter_02,
            self.writing_process_01,
            self.writing_process_02,
        ]

        result = sum([i for i in list_of_values if i is not None]) / \
                 len([i for i in list_of_values if i is not None])

        return round(result, 2)

    def __str__(self):
        return f'{self.turma}: {self.aluno}'

# class HistoricoAlunoPre(models.Model):
#     id = models.AutoField(primary_key=True,)
#     created_at = models.DateField(auto_now_add=True)
#
#     turma = models.ForeignKey(Turma, null=True, on_delete=models.RESTRICT)  # FK turma
#     aluno = models.ForeignKey(Aluno, null=True, on_delete=models.RESTRICT)  # FK aluno
#
#     numero_aulas = models.IntegerField(blank=True, null=True, default='')
#     numero_faltas = models.IntegerField(blank=True, null=True, default='')
#
#     def __str__(self):
#         return self.id
