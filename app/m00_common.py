
from datetime import datetime

# Declaring django modules
from django.core.paginator import Paginator

# Declaring Global Variables

DATE_SHORT_LOCAL_WITH_DASH: str = '%Y-%m-%d'

def pagination(page: int, nbr_pag: int, liste_obj):
    paginator = Paginator(liste_obj, nbr_pag)
    obj = paginator.get_page(page)
    return obj