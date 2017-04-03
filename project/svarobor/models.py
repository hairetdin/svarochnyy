from django.db import models
from django.contrib.auth.models import User

U_CHOICES = (
    ('2', '220'),
    ('3', '380'),

)

YESNO_CHOICES = (
    ('Y', u'Да'),
    ('N', u'Нет'),

)

class TechHarakteristiki(models.Model):
    tovar = models.OneToOneField('spravochnik.Nomenklatura')
    tok_min = models.IntegerField(blank=True, null=True)
    tok_max = models.IntegerField(blank=True, null=True)
    period_nagruzki = models.IntegerField(blank=True, null=True)
    mind_elektroda = models.DecimalField(max_digits=2, decimal_places=1,blank=True,null=True, help_text=u'Минимальный диаметр электрода, мм')
    maxd_elektroda = models.IntegerField(blank=True, null=True, help_text=u'Максимальный диаметр электрода, мм')
    max_mochnost = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
    u = models.CharField(max_length=1, choices=U_CHOICES, default='2', help_text=u'Напряжение, В')
    u_dugi = models.IntegerField(blank=True, null=True, help_text=u'Напряжение дуги')
    delta_u = models.CharField(max_length=20, blank=True, help_text=u'Допустимое отклонение напряжения')
    chastota_seti = models.CharField(max_length=10, blank=True)
    kpd = models.DecimalField(max_digits=2, decimal_places=0,blank=True,null=True)
#    kolichestvo_postov
    gabarity = models.CharField(max_length=20, blank=True)
    ves = models.DecimalField(max_digits=2, decimal_places=1,blank=True,null=True)
    ves_brutto  = models.DecimalField(max_digits=2, decimal_places=1,blank=True,null=True)
    trehfaznoe_u = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text=u'Трехфазное питание, В')
    anti_stick = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text=u'Антиприлипание')
    hot_start = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text=u'Поджиг дуги')
    arc_force = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text=u'Регулировка силы дуги')
    zachita_napryajeniya = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text=u'Защита от перепадов напряжения')
    zachita_razbyzgiv = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text=u'Защита от разбрызгивания')
    vozdushnoe_ohlagdenie = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text=u'Воздушное охлаждение')
    klas_zaschity = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return u'%s' % (self.tovar)
        


class DopInfo(models.Model):
    strana_proiz = models.ForeignKey('spravochnik.Strana', blank=True, help_text=u'В какой стране изготовлено')
    cena = models.DecimalField(max_digits=11, decimal_places=2,blank=True,null=True)
    cena_opt = models.DecimalField(max_digits=11, decimal_places=2,blank=True,null=True)

    def __unicode__(self):
        return u'%s' % (self.cena)
        

class DopKomplekt(models.Model):
    sumka = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text = u'Наличие кейса')
    maska = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text = u'Маска сварщика')
    schetka = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text=u'Щетка')
    zazhim_zemli = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text=u'Зажим заземления')
    derzhatel_elektr = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', help_text=u'Держатель электродов')

    def __unicode__(self):
        return u'%s' % (self.maska)
        
class Prodaja(models.Model):
    author = models.ForeignKey(User)
    prodavec = models.ForeignKey('spravochnik.Contragent')
    nomenklatura = models.ForeignKey('spravochnik.Nomenklatura')
    dop_info = models.OneToOneField(DopInfo)
    dop_komplekt = models.OneToOneField(DopKomplekt, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % (self.prodavec)