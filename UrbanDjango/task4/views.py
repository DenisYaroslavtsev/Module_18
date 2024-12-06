from django.shortcuts import render


def func(request):
    return render(request, 'first_page.html')


def shop(request):
    context = {
        'cheats': [' Cheat Dota2', 'Cheat CS2', ' Cheat Rust', 'Cheat DeadLock']
    }

    return render(request, 'shop.html', {'context': context})


def basket(request):
    return render(request, 'basket.html')

