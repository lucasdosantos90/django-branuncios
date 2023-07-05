from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from PIL import Image

# Create your models here.
#--------------------class Imovel-------------------------------------#
class Tipo_Imovel(models.Model):
    tipo_imovel = models.CharField(max_length=30,default='casa, apartamento etc')

    def __str__(self):
        return self.tipo_imovel

class Imovel(models.Model):
    titulo_anuncio = models.CharField(default='Imovel...',max_length=30,null=True, blank=True)
    valor_a_vista = models.CharField(default='250.000', max_length=10,null=True, blank=True)
    valor_aluguel = models.CharField(default='1600,00', max_length=10,null=True, blank=True)
    condominio = models.CharField(default='400,00',max_length=10,null=True, blank=True)
    iptu = models.CharField(default='900,00',max_length=10,null=True, blank=True)
    contato_anunciante = models.CharField(default='(19) 99348-0987', max_length=15,null=True, blank=True)
    cidade = models.CharField(default='Americana', max_length=50,null=True, blank=True)
    estado = models.CharField(default='São Paulo', max_length=50,null=True, blank=True)
    tipo_imovel = models.ManyToManyField(Tipo_Imovel,default='casa, apartamento etc', null=True, blank=True)
    metros_quadrados = models.IntegerField(default=25,max_length=1500,null=True, blank=True)
    quartos = models.IntegerField(default=2,max_length=5,null=True, blank=True)
    vagas = models.IntegerField(default=2,max_length=5,null=True, blank=True)
    banheiros = models.IntegerField(default=1,max_length=4,null=True, blank=True)
    portaria = models.BooleanField(default=True)
    informacoes_gerais = models.TextField(default='Informações aqui...',null=True, blank=True)
    foto1 = models.ImageField(default='default.jpg', upload_to='media',null=True,blank=True)
    foto2 = models.ImageField(default='default.jpg', upload_to='media',null=True,blank=True)
    foto3 = models.ImageField(default='default.jpg', upload_to='media',null=True,blank=True)
    foto4 = models.ImageField(default='default.jpg', upload_to='media',null=True,blank=True)
    foto5 = models.ImageField(default='default.jpg', upload_to='media',null=True,blank=True)
    descricao_texto = models.TextField(default='Descrição...',null=True, blank=True)
    login = models.ForeignKey(User,on_delete=models.CASCADE,default=User.username,null=False,blank=False)
    viram_anuncio = models.IntegerField(default=0)
    vezes_na_lista = models.IntegerField(default=0)
    data_anuncio = models.DateTimeField(default=timezone.now)

    #Prevent to show extra 'S' on the names
    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.titulo_anuncio
    
#--------------------class Carro-------------------------------------#

class Cambio(models.Model):
    cambio = models.CharField(max_length=20)

    def __str__(self):
        return self.cambio

class Carroceria(models.Model):
    carroceria = models.CharField(max_length=20)

    def __str__(self):
        return self.carroceria

class Combustivel(models.Model):
    combustivel = models.CharField(default='Automático',max_length=20)

    def __str__(self):
        return self.combustivel

class Cor(models.Model):
    cor = models.CharField(max_length=20)

    def __str__(self):
        return self.cor

class Itens_veiculo(models.Model):
    itens_veiculo = models.CharField(max_length=20)

    def __str__(self):
        return self.itens_veiculo
    
class Carro(models.Model):
    nome = models.CharField(default='Carro',max_length=30,null=True, blank=True)
    valor = models.CharField(default='70.000,00',max_length=15,null=True, blank=True)
    versao_carro = models.CharField(default='Versão Nova',max_length=25,null=True, blank=True)
    marca = models.CharField(default='Sem Marca',max_length=25,null=True, blank=True)
    cidade = models.CharField(default='Americana', max_length=50,null=True, blank=True)
    estado = models.CharField(default='São Paulo', max_length=50,null=True, blank=True)
    ano = models.CharField(default='2024',max_length=4,null=True, blank=True)
    km = models.CharField(default='0',max_length=6,null=True, blank=True)
    cambio = models.ManyToManyField(Cambio,default='Automático',null=True, blank=True)
    carroceria = models.ManyToManyField(Carroceria,null=True, blank=True)
    combustivel = models.ManyToManyField(Combustivel,default='Flex',null=True, blank=True)
    cor = models.ManyToManyField(Cor,default='Cinza',null=True, blank=True)
    aceita_troca = models.BooleanField(default=True)
    licenciado = models.BooleanField(default=True)
    foto1 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    foto2 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    foto3 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    foto4 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    foto5 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    itens_veiculo = models.ManyToManyField(Itens_veiculo)
    contato = models.CharField(max_length=30)
    login = models.ForeignKey(User, on_delete=models.CASCADE, default=User.username, null=False, blank=False)
    status_anuncio = models.BooleanField(default=True)
    data_criado = models.DateTimeField(default=timezone.now)
    viram_anuncio = models.IntegerField(default=0)
    vezes_na_lista = models.IntegerField(default=0) 

    #Prevent to show extra 'S' on the names
    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.nome  

#--------------------class Moto-------------------------------------#    
class Tipo_Motor(models.Model):
    tipo_motor = models.CharField(default='Monocilindro')

    def __str__(self):
        return self.tipo_motor

class Refrigeracao(models.Model):
    refrigeracao = models.CharField(default='Líquido')

    def __str__(self):
        return self.refrigeracao

class Estilo(models.Model):
    estilo = models.CharField(default='Custom')

    def __str__(self):
        return self.estilo

class Freio_dianteiro_traseiro(models.Model):
    freio_dianteiro_traseiro = models.CharField(default='ABS')

    def __str__(self):
        return self.freio_dianteiro_traseiro

class Injecao(models.Model):
    injecao = models.CharField(default='Eletrînica')

    def __str__(self):
        return self.injecao

class Moto(models.Model):
    nome = models.CharField(default='Moto',max_length=30,null=True, blank=True)
    valor = models.CharField(default='20.000,00',max_length=15,null=True, blank=True)
    versao_moto = models.CharField(default='Versão Nova',max_length=25,null=True, blank=True)
    marca = models.CharField(default='Sem Marca',max_length=25,null=True, blank=True)
    cidade = models.CharField(default='Americana', max_length=50,null=True, blank=True)
    estado = models.CharField(default='São Paulo', max_length=50,null=True, blank=True)
    ano = models.CharField(default='2024',max_length=4,null=True, blank=True)
    km = models.CharField(default='0',max_length=6,null=True, blank=True)
    marchas = models.IntegerField(default=5,max_length=6)
    tipo_de_motor = models.ManyToManyField(Tipo_Motor,default='Monocilindro')
    cor = models.ManyToManyField(Cor,default='Cinza',null=True, blank=True)
    combustivel = models.ManyToManyField(Combustivel,default='Flex',null=True, blank=True)
    refrigeracao = models.ManyToManyField(Refrigeracao)
    estilo = models.ManyToManyField(Estilo)
    cilindrada = models.CharField(default='162,7 cc',max_length=15)
    partida = models.CharField(default='Elétrica',max_length=20)
    freio_dianteiro_traseiro = models.ManyToManyField(Freio_dianteiro_traseiro)
    injecao = models.ManyToManyField(Injecao,default='Eletrônica')
    contato = models.CharField(max_length=30)
    login = models.ForeignKey(User, on_delete=models.CASCADE, default=User.username, null=False, blank=False)
    status_anuncio = models.BooleanField(default=True)
    data_criado = models.DateTimeField(default=timezone.now)
    viram_anuncio = models.IntegerField(default=0)
    vezes_na_lista = models.IntegerField(default=0)

    #Prevent to show extra 'S' on the names
    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.nome

#--------------------class Empresas e Empregos-------------------------------------# 
class Empresa(models.Model):
    nome_empresa = models.CharField(default='Empresa',max_length=30,null=True, blank=True)
    detalhe_anuncio = models.TextField()
    cidade = models.CharField(default='Americana', max_length=50,null=True, blank=True)
    estado = models.CharField(default='São Paulo', max_length=50,null=True, blank=True)
    contato = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    login = models.ForeignKey(User, on_delete=models.CASCADE, default=User.username, null=False, blank=False)
    status_anuncio = models.BooleanField(default=True)
    data_criado = models.DateTimeField(default=timezone.now)
    viram_anuncio = models.IntegerField(default=0)
    vezes_na_lista = models.IntegerField(default=0)

    #Prevent to show extra 'S' on the names
    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.nome_empresa  

class Responsabilidades(models.Model):
    responsabilidades = models.CharField(max_length=25)

    def __str__(self):
        return self.responsabilidades

class Requisitos(models.Model):
    requisitos = models.CharField(max_length=25)

    def __str__(self):
        return self.requisitos

class Beneficio(models.Model):
    beneficios = models.CharField(max_length=25)

    def __str__(self):
        return self.beneficios
    
class Emprego(models.Model):
    nome_vaga = models.CharField(max_length=30,null=True,blank=True)
    salario = models.CharField(max_length=15,null=True,blank=True)
    empresa = models.ManyToManyField(Empresa)
    descricao = models.TextField(default='Descrição...')
    cidade = models.CharField(default='Americana', max_length=50,null=True, blank=True)
    estado = models.CharField(default='São Paulo', max_length=50,null=True, blank=True)
    responsabilidades = models.ManyToManyField(Responsabilidades)
    requisitos = models.ManyToManyField(Requisitos)
    beneficios = models.ManyToManyField(Beneficio)
    observacoes = models.TextField()
    contato = models.CharField(max_length=30)
    email_contato = models.CharField(max_length=30)
    login = models.ForeignKey(User, on_delete=models.CASCADE, default=User.username, null=False, blank=False)
    status_anuncio = models.BooleanField(default=True)
    data_criado = models.DateTimeField(default=timezone.now)
    viram_anuncio = models.IntegerField(default=0)
    vezes_na_lista = models.IntegerField(default=0)   

    #Prevent to show extra 'S' on the names
    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.nome_vaga

#--------------------class Servicos-------------------------------------#   
class Tipo_servico(models.Model):
    tipo_servico = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_servico

class Servico(models.Model):
    nome = models.CharField(default='Serviço',max_length=30,null=True, blank=True)
    tipo_servico = models.ManyToManyField(Tipo_servico)
    descricao = models.TextField()
    contato = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    preco = models.CharField(default='0',null=True,blank=True,max_length=10)
    cidade = models.CharField(default='Americana', max_length=50,null=True, blank=True)
    estado = models.CharField(default='São Paulo', max_length=50,null=True, blank=True)
    login = models.ForeignKey(User, on_delete=models.CASCADE, default=User.username, null=False, blank=False)
    status_anuncio = models.BooleanField(default=True)
    data_criado = models.DateTimeField(default=timezone.now)
    viram_anuncio = models.IntegerField(default=0)
    vezes_na_lista = models.IntegerField(default=0) 

    #Prevent to show extra 'S' on the names
    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.nome