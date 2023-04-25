from django.db import models

# Create your models here.
class Aluno(models.Model):
    id = models.AutoField(primary_key=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100, blank=True, null=True, default='')
    sobrenome = models.CharField(max_length=100, blank=True, null=True, default='')
    last_name = models.CharField(max_length=100, blank=True, null=True, default='')
    status = models.CharField(max_length=100, blank=True, null=True, default='')
    dat_nasc = models.DateTimeField( blank=True, null=True, default='')
    mes_nascimento = models.IntegerField( blank=True, null=True, default='')
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
    inicio = models.DateTimeField( blank=True, null=True, default='')
    n_irmaos = models.IntegerField( blank=True, null=True, default='')
    retorno = models.DateTimeField( blank=True, null=True, default='')
    sexo = models.CharField(max_length=100, blank=True, null=True, default='')
    responsavel_financeiro = models.CharField(max_length=100, blank=True, null=True, default='')
    responsavel_p_filhos = models.CharField(max_length=100, blank=True, null=True, default='')
    bairro_de_ida = models.CharField(max_length=100, blank=True, null=True, default='')
    bairro_de_vola = models.CharField(max_length=100, blank=True, null=True, default='')
    enviar_boleto = models.IntegerField( blank=True, null=True, default='')
    gerar_taxa = models.IntegerField( blank=True, null=True, default='')
    bolsista = models.IntegerField( blank=True, null=True, default='')

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

    def __str__(self):
        return f'{self.id}: {self.nome} {self.last_name}'.upper()


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True,)
    created_at  = models.DateTimeField(auto_now_add=True)

    nome = models.CharField(max_length=100, blank=True, null=True, default='')
    status = models.CharField(max_length=100, blank=True, null=True, default='')
    funcao_choices = (
        ('gerente', 'gerente'),
        ('recepção', 'recepção'),
        ('professor', 'professor'),
    )
    funcao = models.CharField(max_length=30 , blank=True, null=True, default='', choices=funcao_choices)  # [1=gerente, 2=recep, 3=professor]
    senha = models.CharField(max_length=100, blank=True, null=True, default='')
    # senha = models.CharField(max_length=100, blank=True, null=True, default='')
    telefone1 = models.CharField(max_length=20, blank=True, null=True, default='')
    telefone2 = models.CharField(max_length=20, blank=True, null=True, default='')
    dat_nasc = models.DateTimeField( blank=True, null=True, default='')
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

    def __str__(self):
        return f'{self.id}: {self.nome} - {self.funcao} - {self.status}'.upper()


class Horario(models.Model):
    id = models.AutoField(primary_key=True,)
    dia_semana_choice = (
        ('segunda-feira','segunda-feira'),
        ('terça-feira','terça-feira'),
        ('quarta-feira','quartada-feira'),
        ('quinta-feira','quintaa-feira'),
        ('sexta-feira','sextaa-feira'),
        ('sábado-feira','sábadoda-feira'),
        ('domingo-feira','domingoa-feira'),
    )
    dia_semana = models.CharField(max_length=30, blank=True, null=True, default='', choices=dia_semana_choice)
    hora_inicio = models.CharField(max_length=2, blank=True, null=True, default='',)
    min_inicio = models.CharField(max_length=2, blank=True, null=True, default='')
    hora_fim = models.CharField(max_length=2, blank=True, null=True, default='')
    min_fim = models.CharField(max_length=2, blank=True, null=True, default='')
    duracao_min = models.CharField(max_length=2, blank=True, null=True, default='')

    def __str__(self):
        return f'{self.dia_semana} - {self.hora_inicio}:{self.min_inicio}/' \
           f'{self.hora_fim}:{self.min_fim}'.upper()


class Turma(models.Model):
    id = models.AutoField(primary_key=True,)
    created_at = models.DateTimeField(auto_now_add=True)

    horario = models.ForeignKey(Horario, null=True, on_delete=models.RESTRICT, related_name='horario') # FK horario
    professor = models.ForeignKey(Funcionario, null=True, on_delete=models.RESTRICT, related_name='professor') # FK professor
    coordenador = models.ForeignKey(Funcionario, null=True, on_delete=models.RESTRICT, related_name='coordenador') # FK coordenador
    aluno = models.ManyToManyField(Aluno, null=True, related_name='aluno') # FK coordenador

    status = models.CharField(max_length=100, blank=True, null=True, default='')
    escola = models.CharField(max_length=100, blank=True, null=True, default='')
    nome = models.CharField(max_length=100, blank=True, null=True, default='')
    observacao = models.CharField(max_length=100, blank=True, null=True, default='')
    desc = models.CharField(max_length=100, blank=True, null=True, default='') #list ([op beginer I, op beginer II]  )
    nivel = models.CharField(max_length=100, blank=True, null=True, default='') #list ([op beginer I, op beginer II]  )
    inicio = models.DateTimeField(blank=True, null=True, default='')
    fim = models.DateTimeField(blank=True, null=True, default='')
    map = models.CharField(max_length=100, blank=True, null=True, default='') #list ([op beginer I, op beginer II]  )
    idioma = models.CharField(max_length=100, blank=True, null=True, default='') #list ([op beginer I, op beginer II]  )


    def __str__(self):
        return f'{self.created_at.year}-{self.created_at.month}: {self.horario}'

class HistoricoAluno(models.Model):
    id = models.AutoField(primary_key=True,)
    created_at = models.DateTimeField(auto_now_add=True)

    aluno = models.ForeignKey(Aluno, null=True, on_delete=models.RESTRICT)  # FK aluno
    turma = models.ForeignKey(Turma, null=True, on_delete=models.RESTRICT)  # FK turma
    # id_aluno = models.IntegerField(blank=True, null=True, default='')
    # id_turma = models.IntegerField(blank=True, null=True, default='')
    n_aulas = models.IntegerField(blank=True, null=True, default='')
    n_faltas = models.IntegerField(blank=True, null=True, default='')
    frequencia = models.FloatField(blank=True, null=True, default='')
    # notas
    research = models.IntegerField(blank=True, null=True, default='')
    organization = models.IntegerField(blank=True, null=True, default='')
    interest = models.IntegerField(blank=True, null=True, default='')
    group_activity = models.IntegerField(blank=True, null=True, default='')
    speaking = models.IntegerField(blank=True, null=True, default='')
    frequencia_of = models.IntegerField(blank=True, null=True, default='')
    listening = models.IntegerField(blank=True, null=True, default='')
    readind_inter = models.IntegerField(blank=True, null=True, default='')
    writing_process = models.IntegerField(blank=True, null=True, default='')
    media = models.FloatField(blank=True, null=True, default='')

    coment1 = models.CharField(max_length=100, blank=True, null=True, default='')
    coment2 = models.TextField(blank=True, null=True, default='')
    coment3 = models.BinaryField(blank=True, null=True,)

    # inicio = models.DateTimeField(blank=True, null=True, default='')
    # def get_aluno(self):
    #     aluno = Aluno.objects.get(id=self.id)
    #     return aluno