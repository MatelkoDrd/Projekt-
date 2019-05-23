def my_cp(request):
    ctx = {
        'zalogowany': request.user.is_authenticated,
        'Nazwa użytkownika': request.user.email if request.user.is_authenticated else "Niezalogowany",
        'niezarejestrowany': request.user.is_anonymous
    }
    return ctx