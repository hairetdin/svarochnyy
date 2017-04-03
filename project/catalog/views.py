from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from spravochnik.models import Contragent, Category, Nomenklatura
from django.template import RequestContext



def proizvoditel(request, proizvoditel):
    proizvoditel_id = get_object_or_404(Contragent, slug=proizvoditel)
    tovar_list = proizvoditel_id.nomenklatura_set.all()
    category_list = Category.objects.filter(nomenklatura__proizvoditel = proizvoditel_id).distinct()
    return render_to_response('proizvoditel.html', {
            'proizvoditel':proizvoditel_id,
            'tovar_list': tovar_list,
            'category_list':category_list,
                },
            context_instance=RequestContext(request))

def prozvoditel_category(request, proizvoditel, category):
    proizvoditel_id = get_object_or_404(Contragent, slug=proizvoditel)
    category_id = get_object_or_404(Category, slug=category)
    tovar_list = proizvoditel_id.nomenklatura_set.filter(category = category_id)
    category_list = Category.objects.filter(nomenklatura__proizvoditel = proizvoditel_id).distinct()
    return render_to_response('prozvoditel_category.html', {
            'proizvoditel' : proizvoditel_id,
            'category' : category_id,
            'tovar_list': tovar_list,
            'category_list':category_list,
                },
            context_instance=RequestContext(request))
            


def category(request, category):
    category_id = get_object_or_404(Category, slug=category)
    tovar_list = category_id.nomenklatura_set.all()
    proizvoditel_list = Contragent.objects.filter(nomenklatura__category = category_id).distinct()
    return render_to_response('category.html', {
            'category':category_id,
            'tovar_list' : tovar_list,
            'proizvoditel_list': proizvoditel_list,
                },
            context_instance=RequestContext(request))


def category_proizvoditel(request, category, proizvoditel):
    category_id = get_object_or_404(Category, slug=category)
    proizvoditel_id = get_object_or_404(Contragent, slug=proizvoditel)
    tovar_list = proizvoditel_id.nomenklatura_set.filter(category = category_id)
    proizvoditel_list = Contragent.objects.filter(nomenklatura__category = category_id).distinct()
    return render_to_response('category_proizvoditel.html', {
            'proizvoditel' : proizvoditel_id,
            'category' : category_id,
            'tovar_list' : tovar_list,
            'proizvoditel_list':proizvoditel_list,
                },
            context_instance=RequestContext(request))
            
def tovar_detail(request, tovar):

    tovar_id = get_object_or_404(Nomenklatura, slug=tovar)

    c = {'tovar':tovar_id,}
    c.update(csrf(request))
    return render_to_response('tovar_detail.html', c,
                            context_instance=RequestContext(request)
                            )
