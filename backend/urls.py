from django.urls import path
from backend import views

urlpatterns = [
    path('index_page',views.index_page, name="index_page"),
    path('add_legal_ent',views.add_legal_ent, name="add_legal_ent"),
    path('save_legal_ent/',views.save_legal_ent,name="save_legal_ent"),
    path('display_legal_ent/',views.display_legal_ent,name="display_legal_ent"),
    path('edit_legal/<int:legalid>/',views.edit_legal,name="edit_legal"),
    path('update_legal/<int:updateid>/',views.update_legal,name="update_legal"),
    path('de_l_legal/<int:delid>/',views.de_l_legal,name="de_l_legal"),
    path('admin_log_page/',views.admin_log_page,name="admin_log_page"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('add_comp_det/',views.add_comp_det,name="add_comp_det"),
    path('save_comp_det/',views.save_comp_det,name="save_comp_det"),
    path('disp_comp_det/',views.disp_comp_det,name="disp_comp_det"),
    path('edit_comp/<int:compid>/',views.edit_comp,name="edit_comp"),
    path('update_comp/<int:upid>/',views.update_comp,name="update_comp"),
    path('delete_comp/<int:cncid>/',views.delete_comp,name="delete_comp"),
    path('display_lawyer/',views.display_lawyer,name="display_lawyer"),
    path('edit_lawyer/<int:lawyerid>/',views.edit_lawyer,name="edit_lawyer"),
    path('update_lawyer/<int:updid>/',views.update_lawyer,name="update_lawyer"),
    path('remove_lawyer/<int:removeid>/', views.remove_lawyer, name="remove_lawyer")


]