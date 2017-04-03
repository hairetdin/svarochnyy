from spravochnik.models import Category
from django.shortcuts import render_to_response

def menu_category(request):
    
    menu_category = Category.objects.all()
    
    
    return render_to_response('menu_category.html',
           {"menu_category": menu_category,
#            "user" : r_user,
#            "typedoc" : type_document,
#            "categorydoc" : category_document,
            },
            )



menu = {}
for item in category:
 if item.parent == None:
  menu['parent']=item.name
 else:
  menu[item.parent.name] = item.name

for key, value in menu.items():
 print key,':',value
 
newmenu = []
if menu.has_key('parent'):
 parent = menu.get('parent')
 newmenu.append(parent)
 newitem = menu.get(newmenu[-1])
 newmenu.append(newitem)
 
def get_set(cat):
    try:
        spisok = cat.category_set.all()
    except:
        spisok = []
    return spisok