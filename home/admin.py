from django.contrib import admin
from .models import HangHoa, KyTonKho, NhapHangHoa, TonKhoHangHoa, CongThucMon, ChiTietCongThucMon, XuatMonTheoFabi, TongHopXuatNguyenLieu

# Register your models here.
admin.site.register(HangHoa)
admin.site.register(KyTonKho)
admin.site.register(NhapHangHoa)
admin.site.register(TonKhoHangHoa)
admin.site.register(CongThucMon)
admin.site.register(ChiTietCongThucMon)
admin.site.register(XuatMonTheoFabi)
admin.site.register(TongHopXuatNguyenLieu)