from django.db import models
from django.utils import timezone

class HangHoa(models.Model):
    ten_hang_hoa = models.CharField(max_length=255, unique=True)
    don_vi_hang_hoa = models.CharField(max_length=50)
    don_vi_nguyen_lieu = models.CharField(max_length=50)
    dinh_luong = models.FloatField()

    def __str__(self):
        return self.ten_hang_hoa

class NhapHangHoa(models.Model):
    hang_hoa = models.ForeignKey(HangHoa, on_delete=models.CASCADE)
    ngay_nhap = models.DateField()
    so_luong = models.FloatField()
    don_vi_hang_hoa = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.hang_hoa} - {self.ngay_nhap}"

class KyTonKho(models.Model):
    ten_ky = models.CharField(max_length=255)
    ngay_bat_dau = models.DateField()
    ngay_ket_thuc = models.DateField()

    def __str__(self):
        return self.ten_ky

class TonKhoHangHoa(models.Model):
    hang_hoa = models.ForeignKey('HangHoa', on_delete=models.CASCADE)
    ngay_ton = models.DateField()
    ton_dau_ngay = models.FloatField(default=0)  # Tồn đầu ngày
    ton_cuoi_ngay = models.FloatField(default=0)  # Tồn cuối ngày
    don_vi_hang_hoa = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.hang_hoa.ten_hang_hoa} - {self.ngay_ton}"

class CongThucMon(models.Model):
    ten_mon = models.CharField(max_length=255)
    def __str__(self):
        return self.ten_mon  # Sửa lại vì không còn trường ngay_xuat

class ChiTietCongThucMon(models.Model):
    cong_thuc_mon = models.ForeignKey(CongThucMon, on_delete=models.CASCADE, related_name='chi_tiet')
    hang_hoa = models.ForeignKey(HangHoa, on_delete=models.CASCADE)
    dinh_luong = models.FloatField()

    def __str__(self):
        return f"{self.cong_thuc_mon.ten_mon} - {self.hang_hoa.ten_hang_hoa}"

    @property
    def don_vi_nguyen_lieu(self):
        return self.hang_hoa.don_vi_nguyen_lieu  # Lấy tự động từ HangHoa

class XuatMonTheoFabi(models.Model):
    ngay_xuat = models.DateField()
    ten_mon = models.ForeignKey(CongThucMon, on_delete=models.CASCADE)
    nhom_mon = models.CharField(max_length=100)
    loai_mon = models.CharField(max_length=100)
    don_vi_tinh = models.CharField(max_length=50)
    so_luong = models.FloatField()

    def __str__(self):
        return f"{self.ten_mon.ten_mon} - {self.ngay_xuat}"

class TongHopXuatNguyenLieu(models.Model):
    cong_thuc_mon = models.ForeignKey(CongThucMon, on_delete=models.CASCADE)
    hang_hoa = models.ForeignKey(HangHoa, on_delete=models.CASCADE)
    dinh_luong = models.FloatField()
    so_mon_xuat = models.FloatField(default=0)
    nguyen_lieu_da_xuat = models.FloatField(default=0)
    ngay_xuat = models.DateField(default=timezone.now)  # Thêm trường này

    def __str__(self):
        return f"{self.cong_thuc_mon.ten_mon} - {self.hang_hoa.ten_hang_hoa}"