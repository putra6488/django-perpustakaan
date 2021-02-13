from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def buku(request):
    judul = [
        "belajar django",
        "belajar python",
        "belajar matplotlib"
    ]
    penulis = "Putra Prasetyo"

    konteks = {
        'title' : judul,
        "penulis" : penulis
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')