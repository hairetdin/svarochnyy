from django.contrib import admin
from spravochnik.models import VidDeyatelnosty, Valuta, Strana, Gorod, Category, Contragent, Nomenklatura, AttachNomenkl


#class MembershipInline(admin.TabularInline):
#    model = Pdn.categoriya_pdn.through

#class Categoriya_pdnAdmin(admin.ModelAdmin):
#    inlines = [
#        MembershipInline,
#    ]

#class PdnAdmin(admin.ModelAdmin):
#    inlines = [
#        MembershipInline,
#    ]

#class DocumentAdmin(admin.ModelAdmin):
#    search_fields = ['name']

admin.site.register(VidDeyatelnosty)
admin.site.register(Valuta)
admin.site.register(Strana)
admin.site.register(Gorod)
admin.site.register(Category)
admin.site.register(Contragent)
admin.site.register(Nomenklatura)
admin.site.register(AttachNomenkl)
