from datetime import datetime
import math
from collections import defaultdict
from constants import parkir, riwayat, TARIF
from utils.waktu import hitung_durasi_menit, hitung_biaya

# ================= KONFIG DEMO =================
# Paksa semua input hari ini ke tanggal 15 Januari 2026
TANGGAL_TETAP = datetime(2026, 1, 15)
# Tanggal khusus untuk laporan bulan & tahun
TANGGAL_LAPORAN = datetime(2025, 12, 16)

# ================= INIT RIWAYAT =================
def init_riwayat():
    for r in riwayat:
        if r.get("menit") is None or r.get("biaya") is None:
            menit = hitung_durasi_menit(r["masuk"], r["keluar"])
            biaya = hitung_biaya(r["jenis"], menit)

            r["menit"] = menit
            r["biaya"] = biaya


# ================= LAPORAN =================
def buat_struktur_kosong():
    return {
        "mobil": {"jml": 0, "biaya": 0},
        "motor": {"jml": 0, "biaya": 0},
        "total_jml": 0,
        "total_biaya": 0
    }

def proses_analisis(format_waktu):
    init_riwayat()
    hasil = defaultdict(buat_struktur_kosong)

    for r in riwayat:
        dt = datetime.strptime(r["keluar"], "%Y-%m-%d %H:%M:%S")
        key = dt.strftime(format_waktu)

        jenis = r["jenis"].lower()
        biaya = r["biaya"]

        if jenis == "mobil":
            hasil[key]["mobil"]["jml"] += 1
            hasil[key]["mobil"]["biaya"] += biaya
        elif jenis == "motor":
            hasil[key]["motor"]["jml"] += 1
            hasil[key]["motor"]["biaya"] += biaya

        hasil[key]["total_jml"] += 1
        hasil[key]["total_biaya"] += biaya

    return hasil


# ================= MENU ANALISIS =================
def laporan_harian():
    return proses_analisis("%d-%m-%Y")

def laporan_mingguan():
    # Mingguan = tanggal data (bukan minggu ke-...)
    return proses_analisis("%d-%m-%Y")

def laporan_bulanan():
    # Pakai tanggal 16 Desember 2025
    return proses_analisis(TANGGAL_LAPORAN.strftime("%d %B %Y"))

def laporan_tahunan():
    # Pakai tanggal 16 Desember 2025
    return proses_analisis(TANGGAL_LAPORAN.strftime("%d %B %Y"))



def total_laporan():
    init_riwayat()
    mobil = sum(1 for r in riwayat if r["jenis"] == "mobil")
    motor = sum(1 for r in riwayat if r["jenis"] == "motor")
    total_biaya = sum(r["biaya"] for r in riwayat)

    return len(riwayat), total_biaya, mobil, motor


# ================= PARKIR =================
def kendaraan_masuk(plat, jenis, merk):
    # ... (cek plat)
    parkir.append({
        "plat": plat,
        "jenis": jenis.lower(),
        "merk": merk,
        "masuk": datetime.now().strftime("%Y-%m-%d %H:%M:%S") # MENGGUNAKAN WAKTU SEKARANG
    })
    return True

def kendaraan_keluar(plat):
    for i, k in enumerate(parkir):
        if k["plat"] == plat:
            keluar = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # MENGGUNAKAN WAKTU SEKARANG
            # ... (proses hitung durasi & biaya tetap sama)

            durasi_menit = hitung_durasi_menit(k["masuk"], keluar)
            biaya = hitung_biaya(k["jenis"], durasi_menit)

            data = {
                "plat": k["plat"],
                "jenis": k["jenis"],
                "merk": k["merk"],
                "masuk": k["masuk"],
                "keluar": keluar,
                "menit": durasi_menit,
                "biaya": biaya
            }

            parkir.pop(i)
            riwayat.append(data)
            return data

    return None


def daftar_parkir():
    return parkir


def reset_data():
    parkir.clear()
    riwayat.clear()