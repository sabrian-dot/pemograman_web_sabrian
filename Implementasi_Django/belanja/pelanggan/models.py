from django.db import models


class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    alamat = models.TextField()

    def __str__(self):
        return self.nama


class Produk(models.Model):
    nama_produk = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=12, decimal_places=2)
    stok = models.IntegerField()

    def __str__(self):
        return self.nama_produk


class Pesanan(models.Model):
    pelanggan = models.ForeignKey(
        Pelanggan,
        on_delete=models.CASCADE
    )
    tanggal_pesanan = models.DateField()
    total_harga = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return f"Pesanan {self.id}"


class DetailPesanan(models.Model):
    pesanan = models.ForeignKey(
        Pesanan,
        on_delete=models.CASCADE
    )
    produk = models.ForeignKey(
        Produk,
        on_delete=models.CASCADE
    )
    jumlah = models.IntegerField()
    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return f"Detail {self.id}"