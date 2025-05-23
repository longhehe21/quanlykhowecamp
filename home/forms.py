from django import forms
from .models import HangHoa, NhapHangHoa, TonKhoHangHoa, CongThucMon, ChiTietCongThucMon, XuatMonTheoFabi

class HangHoaForm(forms.ModelForm):
    class Meta:
        model = HangHoa
        fields = ['ten_hang_hoa', 'don_vi_hang_hoa', 'don_vi_nguyen_lieu', 'dinh_luong']
        labels = {
            'ten_hang_hoa': 'Tên hàng hóa',
            'don_vi_hang_hoa': 'Đơn vị hàng hóa',
            'don_vi_nguyen_lieu': 'Đơn vị nguyên liệu',
            'dinh_luong': 'Định lượng',
        }
        widgets = {
            'ten_hang_hoa': forms.TextInput(attrs={'placeholder': 'Ví dụ: Gạo', 'class': 'form-control'}),
            'don_vi_hang_hoa': forms.TextInput(attrs={'placeholder': 'Ví dụ: kg', 'class': 'form-control'}),
            'don_vi_nguyen_lieu': forms.TextInput(attrs={'placeholder': 'Ví dụ: kg', 'class': 'form-control'}),
            'dinh_luong': forms.NumberInput(attrs={'placeholder': 'Ví dụ: 100', 'step': '0.01', 'class': 'form-control'}),
        }

class NhapHangHoaForm(forms.ModelForm):
    class Meta:
        model = NhapHangHoa
        fields = ['hang_hoa', 'ngay_nhap', 'so_luong']
        labels = {
            'hang_hoa': 'Tên hàng hóa',
            'ngay_nhap': 'Ngày nhập',
            'so_luong': 'Số lượng',
        }
        widgets = {
            'hang_hoa': forms.Select(attrs={'class': 'form-control'}),
            'ngay_nhap': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'so_luong': forms.NumberInput(attrs={'placeholder': 'Ví dụ: 50', 'step': '0.01', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hang_hoa'].widget.choices = [
            ('', '--- Chọn hàng hóa ---'),
        ] + [(hh.pk, hh.ten_hang_hoa) for hh in HangHoa.objects.all()]

class TonKhoHangHoaForm(forms.ModelForm):
    class Meta:
        model = TonKhoHangHoa
        fields = ['hang_hoa', 'ngay_ton', 'ton_dau_ngay', 'ton_cuoi_ngay']
        labels = {
            'hang_hoa': 'Tên hàng hóa',
            'ngay_ton': 'Ngày tồn',
            'ton_dau_ngay': 'Tồn đầu ngày',
            'ton_cuoi_ngay': 'Tồn cuối ngày',
        }
        widgets = {
            'hang_hoa': forms.Select(attrs={'class': 'form-control', 'id': 'id_hang_hoa'}),
            'ngay_ton': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ton_dau_ngay': forms.NumberInput(attrs={'placeholder': 'Tính tự động', 'step': '0.01', 'class': 'form-control', 'readonly': 'readonly'}),
            'ton_cuoi_ngay': forms.NumberInput(attrs={'placeholder': 'Ví dụ: 100', 'step': '0.01', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hang_hoa'].widget.choices = [
            ('', '--- Chọn hàng hóa ---'),
        ] + [(hh.pk, hh.ten_hang_hoa) for hh in HangHoa.objects.all()]
        self.fields['ton_dau_ngay'].disabled = True  # Vô hiệu hóa trường tồn đầu ngày

class TonKhoHangHoaImportForm(forms.Form):
    excel_file = forms.FileField(
        label='File Excel',
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.xlsx'}),
        help_text='File Excel phải có các cột: "Tên Hàng Hóa", "Ngày Tồn", "Tồn Cuối Ngày".'
    )

class TonKhoHangHoaFilterForm(forms.Form):
    ngay_bat_dau = forms.DateField(
        label='Từ ngày',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )
    ngay_ket_thuc = forms.DateField(
        label='Đến ngày',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )

class CongThucMonForm(forms.ModelForm):
    class Meta:
        model = CongThucMon
        fields = ['ten_mon']
        labels = {
            'ten_mon': 'Tên món',
        }
        widgets = {
            'ten_mon': forms.TextInput(attrs={'placeholder': 'Ví dụ: Phở bò', 'class': 'form-control'}),
        }

class ChiTietCongThucMonForm(forms.ModelForm):
    hang_hoa = forms.ModelChoiceField(
        queryset=HangHoa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Nguyên liệu'
    )

    class Meta:
        model = ChiTietCongThucMon
        fields = ['hang_hoa', 'dinh_luong']
        labels = {
            'dinh_luong': 'Định lượng',
        }
        widgets = {
            'dinh_luong': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control', 'placeholder': 'Ví dụ: 0.5'}),
        }

class XuatMonTheoFabiForm(forms.ModelForm):
    class Meta:
        model = XuatMonTheoFabi
        fields = ['ngay_xuat', 'ten_mon', 'nhom_mon', 'loai_mon', 'don_vi_tinh', 'so_luong']
        labels = {
            'ngay_xuat': 'Ngày xuất',
            'ten_mon': 'Tên món',
            'nhom_mon': 'Nhóm món',
            'loai_mon': 'Loại món',
            'don_vi_tinh': 'Đơn vị tính',
            'so_luong': 'Số lượng',
        }
        widgets = {
            'ngay_xuat': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ten_mon': forms.Select(attrs={'class': 'form-control'}),
            'nhom_mon': forms.TextInput(attrs={'placeholder': 'Ví dụ: Món chính', 'class': 'form-control'}),
            'loai_mon': forms.TextInput(attrs={'placeholder': 'Ví dụ: Món nước', 'class': 'form-control'}),
            'don_vi_tinh': forms.TextInput(attrs={'placeholder': 'Ví dụ: Suất', 'class': 'form-control'}),
            'so_luong': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }