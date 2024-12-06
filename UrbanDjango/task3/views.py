from django.shortcuts import render


def func(request):
    return render(request, 'first_page.html')


def shop(request):
    items = [
        {'name': 'Cheat Dota2'},
        {'name': 'Cheat CS2'},
        {'name': 'Cheat Rust'},
        {'name': 'Cheat DeadLock'}
    ]
    return render(request, 'shop.html', {'items': items})


def basket(request):
    return render(request, 'basket.html')
