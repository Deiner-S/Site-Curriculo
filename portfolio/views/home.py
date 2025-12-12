from django.shortcuts import render
from theme.templates.paths import Paths as path

def home(request):
    positions = [
        {'top': 845, 'left': 732},
        {'top': 170, 'left': 1466},
        {'top': 46, 'left': 1763},
        {'top': 100, 'left': 146},
        {'top': 566, 'left': 888},
        {'top': 609, 'left': 1300},
        {'top': 774, 'left': 1666},
        {'top': 211, 'left': 1197},
        {'top': 1086, 'left': 1421},
        {'top': 817, 'left': 173},
    ]
    positions2 = [
        {'top': 434, 'left': 234},
        {'top': 363, 'left': 751},
        {'top': 440, 'left': 1563},
        {'top': 691, 'left': 438},
        {'top': 38, 'left': 859},
        {'top': 1083, 'left': 478},
        {'top': 1153, 'left': 999},
        {'top': 1070, 'left': 763},
        {'top': 820, 'left': 1115},
        {'top': 183, 'left': 513},
    ]
    return render(request, path.HOME,{'positions': positions, "positions2":positions2})