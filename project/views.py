from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from spravochnik.models import Contragent, Category, Nomenklatura
from django.template import RequestContext
from localform import ContactForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def home(request):
    #отображаем только производителей
    proizvoditel = Contragent.objects.filter(type='P')
    category_list = Category.objects.all()
    tovar = Nomenklatura.objects.all().order_by('-pub_date')[:8]
    
    return render_to_response('home.html', {
                        'proizvoditel': proizvoditel,
                        'category_list': category_list,
                        'tovar': tovar,
                        },
            context_instance=RequestContext(request))
            
def search(request):
    tovar_list = []
    q=''
    error=len(q)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if len(q) > 50:
            error = 'Количeство символов в строке Поиск не может быть больше 50 символов'
        else:
            tovar_list = Nomenklatura.objects.filter(name__icontains=q)
            #tovar_list = Category.objects.filter(name__icontains=q)
    else:
        tovar_list=[]
    
    paginator = Paginator(tovar_list, 25)

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        tovars = paginator.page(page)
    except (EmptyPage, InvalidPage):
        tovars = paginator.page(paginator.num_pages)
        
    return render_to_response("search.html", {
                        'search_list': tovars, 
                        'query': q,
                        'error': error ,
                        })

def about(request):
    return render_to_response('about.html')
    
def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        contactform = ContactForm(request.POST) # A form bound to the POST data
        c = {'form':contactform}
        c.update(csrf(request))
        
        if contactform.is_valid():
            subject = contactform.cleaned_data['subject']
            message = contactform.cleaned_data['message']
            sender = contactform.cleaned_data['sender']
            #cc_myself = contactform.cleaned_data['cc_myself']
            
            recipients = ['mail@svarochnyy.ru']
            #if cc_myself:
            #    recipients.append(sender)

            from django.core.mail import send_mail
            from settings import DEFAULT_FROM_EMAIL
            content = u'Сообщение от:' + sender + u' Текст сообщения: ' + message
            send_mail('svarochnyy_ru' + subject, content, DEFAULT_FROM_EMAIL, recipients)
            return render_to_response('thanks.html')
    else:
        contactform = ContactForm()
        c = {'form':contactform}
        c.update(csrf(request))

    return render_to_response('contact_form.html', c)

