
        
for key, value in menu.items():
    print key,':',value
    

def get_parents(model_name):
    parents = []
    for object in model_name.objects.all():
        if object.parent is None:
            parents.append(object.name)
    return parents


def get_childs(parent):
    try:
        parent_item = Category.objects.get(name=parent)
        child_items = parent_item.category_set.all()
        childs = []
        for item in child_items:
            childs.append(item.name)
    except:
        childs = []
    return childs
    



menu = {}
for item in category:
    if item.parent == None:
        menu[item.name]= {}

for key in menu:
    submenu = get_set(key)
    if submenu:
        for item in submenu:
            menu[key][item.name]={}



for parent in get_parents(Category):
    
    childs = get_childs(parent)
    i=1
    print parent
    while len(childs) > 0:
        i+=1
        for child in childs:
            print ' '*i, child
            
            childs = get_childs(child)
            print i





def __unicode__(name):
    return u'%s'% (name)


fo = open("menu.html", "wb")
fo.write( "Content-Type: text/html; charset=utf-8\n")
fo.write( "<html><body>\n")
fo.write( "<ul>\n")

for parent in get_parents(Category):
    
    fo.write( "<li>\n")
    print parent
    fo.write(parent.encode('utf-8'))
    fo.write( "\n")
    
    childs = get_childs(parent)
    fo.write( "<ul>\n")
    while len(childs) > 0:
        fo.write( "<li>\n")
        for child in childs:
            fo.write( "<li>\n")
            print child
            fo.write(child.encode('utf-8'))
            fo.write( "\n")
            fo.write( "</li>\n")
            childs = get_childs(child)
        fo.write( "</li>\n")
    fo.write( "</ul>\n")
    fo.write( "</li>\n")

fo.write( "<ul>\n")
fo.write( "</html></body>\n")
fo.close()


def get_ancestors(item):
 ancestors = []
 parent = item.parent
 while parent is not None:
  ancestors.append(parent.name)
  parent = parent.parent
 return ancestors

for item in category:
 get_ancestors(item)