# its take request as a argument
from .models import Category


#it fetch all the categories from database and return a list of them for
def menu_links(request):
    links = Category.objects.all()
    return dict(links = links)
