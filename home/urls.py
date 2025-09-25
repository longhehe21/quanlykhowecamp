from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('so-sanh-ton-kho/<int:ky_id>/', views.so_sanh_ton_kho, name='so_sanh_ton_kho'),
    path('delete-ton-kho-hang-hoa/<int:ton_kho_id>/', views.delete_ton_kho_hang_hoa, name='delete_ton_kho_hang_hoa'),
    path('edit-ton-kho-hang-hoa/<int:ton_kho_id>/', views.edit_ton_kho_hang_hoa, name='edit_ton_kho_hang_hoa'),
    path('xuat-theo-mon/', views.xuat_theo_mon, name='xuat_theo_mon'),
    path('so-sanh-fabi/', views.so_sanh_fabi, name='so_sanh_fabi'),
    path('quan-ly-hang-hoa/', views.quan_ly_hang_hoa, name='quan_ly_hang_hoa'),
    path('export-tong-ton-kho-excel/', views.export_tong_ton_kho_excel, name='export_tong_ton_kho_excel'),
    path('export-so-sanh-fabi-excel/', views.export_so_sanh_fabi_excel, name='export_so_sanh_fabi_excel'),
    path('nhap-hang-hoa/delete/<int:id>/', views.delete_nhap_hang_hoa, name='delete_nhap_hang_hoa'),
    path('xuat-mon/delete/<int:id>/', views.delete_xuat_mon, name='delete_xuat_mon'),
    path('xuat-mon/delete-all/', views.delete_all_xuat_mon, name='delete_all_xuat_mon'),
    path('tong-hop/delete/<int:id>/', views.delete_tong_hop, name='delete_tong_hop'),
    path('tong-hop/delete-all/', views.delete_all_tong_hop, name='delete_all_tong_hop'),
    path('delete-all-nhap-hang/', views.delete_all_nhap_hang, name='delete_all_nhap_hang'),
    path('hang-hoa/edit/<int:id>/', views.edit_hang_hoa, name='edit_hang_hoa'),
    path('hang-hoa/delete/<int:id>/', views.delete_hang_hoa, name='delete_hang_hoa'),
    path('hang-hoa/delete-all/', views.delete_all_hang_hoa, name='delete_all_hang_hoa'),
    path('delete-cong-thuc/<int:id>/', views.delete_cong_thuc, name='delete_cong_thuc'),  # URL xóa từng công thức
    path('delete-all-cong-thuc/', views.delete_all_cong_thuc, name='delete_all_cong_thuc'),  # URL xóa tất cả công thức
    path('ton-kho-le-tan/edit/<int:ton_kho_id>/', views.edit_ton_kho_le_tan, name='edit_ton_kho_le_tan'),
    path('ton-kho-le-tan/delete/<int:ton_kho_id>/', views.delete_ton_kho_le_tan, name='delete_ton_kho_le_tan'),
    path('ton-kho-le-tan/delete-all/', views.delete_all_ton_kho_le_tan, name='delete_all_ton_kho_le_tan'),
    path('delete-ton-kho-by-date-range/', views.delete_ton_kho_by_date_range, name='delete_ton_kho_by_date_range'),
    # Các URL khác
    # THÊM 2 DÒNG NÀY
    path('api/get-ton-kho-data/', views.get_ton_kho_data, name='get_ton_kho_data'),
    path('api/get-hang-hoa-list/', views.get_hang_hoa_list, name='get_hang_hoa_list'),
    path('api/get-hang-hoa-detail/<int:id>/', views.get_hang_hoa_detail, name='get_hang_hoa_detail'),
    path('api/get-ton-kho-le-tan-data/', views.get_ton_kho_le_tan_data, name='get_ton_kho_le_tan_data'),
]