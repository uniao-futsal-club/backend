from django.db import models
from .fields import UpperCaseField

# Create your models here.


class Team(models.Model):

    asset = models.ForeignKey(
        "asset.Asset", verbose_name="Foto", on_delete=models.CASCADE)
    coach = models.ForeignKey(
        "accounts.Coach", verbose_name="Técnico", on_delete=models.CASCADE)
    name = UpperCaseField("Nome", max_length=45)
    initials = UpperCaseField("Sigla", max_length=3)
    start_year = models.PositiveIntegerField("Ano de Fundação", null=False)
    created_at = models.DateTimeField('Data de Entrada', auto_now_add=True)

    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"

    def __str__(self):
        return self.name


class Contract(models.Model):
    TYPE_CHOICES = (
        (1, 'goalkeeper_titular'),
        (2, 'fixed_titular'),
        (3, 'left_wing_titular'),
        (4, 'right_wing_titular'),
        (5, 'pivot_titular'),
        (6, 'selected'),
        (7, 'unselected'),
    )
    team = models.ForeignKey(
        "team.Team", verbose_name="Time", on_delete=models.CASCADE)
    player = models.ForeignKey(
        "accounts.Player", verbose_name="Jogador", on_delete=models.CASCADE)
    contract_type = models.PositiveIntegerField(
        "Tipo", choices=TYPE_CHOICES, null=False)
    created_at = models.DateTimeField('Data de Entrada', auto_now_add=True)

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"


class Training(models.Model):
    team = models.ForeignKey(
        "team.Team", verbose_name="Treino", on_delete=models.CASCADE)
    players = models.ManyToManyField(
        "accounts.Player", verbose_name="Jogadores")
    description = models.CharField("Descrção", max_length=255)
    date = models.DateField(
        "Data do Treino", auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField('Data de Entrada', auto_now_add=True)

    class Meta:
        verbose_name = "Treino"
        verbose_name_plural = "Treinos"
