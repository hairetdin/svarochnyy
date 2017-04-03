from spravochnik.models import Contragent

def contragent(request):

    #отображаю только производителей
    proizvoditel = Contragent.objects.filter(type='P')
    
    return {
        'PROIZVODITEL': proizvoditel,
    }