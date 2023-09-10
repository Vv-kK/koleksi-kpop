from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama': 'Veronica Kylie',
        'kelas': 'PBP D',
    }

    return render(request, "main.html", context)