from django.db import models
import trans
from tinymce import models as tinymce_models

TYPECONTRAGENT_CHOICES = (
    ('F', u'Физ лицо'),
    ('D', u'Дочернее общество'),
    ('Z', u'Зависимое общество'),
    ('O', u'Организация'),
    ('P', u'Производитель'),
)

class VidDeyatelnosty(models.Model):
    name = models.CharField(max_length=50,help_text=u'Производитель, поставщик, магазин, транспортная компания')
    slug = models.SlugField(default="1")
    
    def __unicode__(self):
        return u'%s'% (self.name)
    
    def save(self, *args, **kwargs):
        e = self.name.encode('trans/slug')[:100]
        if VidDeyatelnosty.objects.filter(slug=e):
            d=1
            while VidDeyatelnosty.objects.filter(slug=e):
                e = self.name.encode('trans/slug')[:100] + str(d)
                d=d+1
                self.slug = e
        else:
            self.slug = self.name.encode('trans/slug')[:100]
            
        super(VidDeyatelnosty, self).save(*args, **kwargs)

class Strana(models.Model):
    name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return u'%s'% (self.name)
        
class Gorod(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    
    def __unicode__(self):
        return u'%s, %s'% (self.name, self.region)

class Valuta(models.Model):
    name = models.CharField(max_length=50)
    kurs = models.IntegerField(blank=True, null=True)
    strana = models.ForeignKey(Strana, blank=True)
    
    def __unicode__(self):
        return u'%s'% (self.name)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text=u'Сварочные полуавтоматы (MIG-MAG), сварочный инвертор')
    parent = models.ForeignKey('self', null=True, blank=True, help_text=u'Родительская категория. Например: сварочное оборудование. Если не уверены - оставьте поле пустым')
    slug = models.SlugField(default="1")
    photo = models.ImageField(upload_to='photo/category/', blank=True)
    about = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        e = self.name.encode('trans/slug')[:50]
        if Category.objects.filter(slug=e):
            d=1
            while Category.objects.filter(slug=e):
                e = self.name.encode('trans/slug')[:50] + str(d)
                d=d+1
                self.slug = e
        else:
            self.slug = self.name.encode('trans/slug')[:50]
            
        super(Category, self).save(*args, **kwargs)

class Contragent(models.Model):
    name = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=TYPECONTRAGENT_CHOICES, default='O')
    gorod = models.ForeignKey(Gorod, blank=True, null=True)
    yuraddress = models.CharField(max_length=85, blank=True)
    postaddress = models.CharField(max_length=85, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    inn = models.IntegerField(blank=True, null=True)
    about = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="1")

    def __unicode__(self):
        if self.name:
            return u'%s'% (self.name)
        else:
            return self.full_name

    def save(self, *args, **kwargs):
        e = self.name.encode('trans/slug')[:100]
        if Contragent.objects.filter(slug=e):
            d=1
            while Contragent.objects.filter(slug=e):
                e = self.name.encode('trans/slug')[:100] + str(d)
                d=d+1
                self.slug = e
        else:
            self.slug = self.name.encode('trans/slug')[:50]
            
        super(Contragent, self).save(*args, **kwargs)

EDINICA_IZMERENIYA_CHOICES = (
    ('S', u'штук'),
    ('L', u'литр'),
    ('K', u'кг'),
    ('T', u'тонна'),
)

TYPE_NOMENKLATURA_CHOICES = (
    ('T', u'Товар'),
    ('U', u'Услуга'),
    ('P', u'Продукция'),
    ('M', u'Материал'),
    ('K', u'Товар на комиссии'),
    ('D', u'Посредническая услуга'),
    ('E', u'Услуга ЕНВД'),
)

class Nomenklatura(models.Model):
    name = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=255)
    edinica_izmereniya = models.CharField(max_length=1, choices=EDINICA_IZMERENIYA_CHOICES, default='S')
    type = models.CharField(max_length=1, choices=TYPE_NOMENKLATURA_CHOICES, default='T')
    vid_deyatelnosty = models.ManyToManyField(VidDeyatelnosty, blank=True)
    cena = models.DecimalField(max_digits=11, decimal_places=2,blank=True,null=True)
    valuta =  models.ForeignKey(Valuta, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('spravochnik.Category', blank=True, null=True)
    proizvoditel = models.ForeignKey('spravochnik.Contragent', blank=True, null=True)
    strana_brenda = models.ForeignKey('spravochnik.Strana', blank=True, null=True, help_text=u'Страна бренда')
    #about = models.TextField(max_length = 500, blank=True)
    about = tinymce_models.HTMLField(blank=True)

    upload_to = lambda inst, fn: 'nomenklatura/%s/%s' % (inst.slug, fn)
    photo = models.ImageField(upload_to=upload_to, blank = True, null=True)
    
    slug = models.SlugField(default="1")
    
    def __unicode__(self):
        if self.name:
            return u'%s'% (self.name)
        else:
            return self.full_name
            
    def save(self, *args, **kwargs):
        e = self.name.encode('trans/slug')[:100]
        if Nomenklatura.objects.filter(slug=e):
            d=1
            while Nomenklatura.objects.filter(slug=e):
                e = self.name.encode('trans/slug')[:100] + str(d)
                d=d+1
                self.slug = e
        else:
            self.slug = self.name.encode('trans/slug')[:50]
            
        super(Nomenklatura, self).save(*args, **kwargs)
        

class AttachNomenkl(models.Model):
    upload_to = lambda inst, fn: 'nomenklatura/%s/%s' % (inst.nomenklatura.slug, fn)
    tovar = models.ForeignKey(Nomenklatura)
    photo = models.ImageField(upload_to=upload_to, blank = True, null=True)
    attachment = models.FileField(upload_to=upload_to, blank = True, null=True)
    caption = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ('-tovar', 'id')

    def __unicode__(self):
        return u'%s: %s' % (self.tovar, self.caption)