from spravochnik.models import Category


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
    while len(childs) > 0:
        fo.write( "<ul>\n")
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