from django.contrib import admin

from .models import Pelanggan, Produk, Pesanan, DetailPesanan


admin.site.register(Pelanggan)
admin.site.register(Produk)
admin.site.register(Pesanan)
admin.site.register(DetailPesanan)