from django.shortcuts import render
from django.http import HttpResponse
from . import StukasMaster as stk
# Create your views here.

def index(request):
    return render(request, "index.html",{
        "namaHotel":stk.namaHotel,
        "menginap":stk.menginap,
        "tanggalCheckin":stk.tanggalCheckIn.date(),
        "tanggalCheckout":stk.tanggalCheckOut.date(),
        "charge": len(stk.chargeTerpilih),
        "chargeTerpilih":stk.chargeTerpilih,
        "biayaCharge":stk.tagihanCharge,
        "subTotalCharge":sum(stk.tagihanCharge),
        "subTotalKamar":stk.totalBiayaKamar,
        "grandTotal":stk.grandTotal,
        "listcharge" : stk.listCharge
        
    })