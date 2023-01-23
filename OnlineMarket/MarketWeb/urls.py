from django.urls import path
from MarketWeb import views

urlpatterns = [
    path('', views.home_pg, name="home_pg"),
    path('about_pg/', views.about_pg, name="about_pg"),
    path('about_d/<int:dataid>', views.about_d, name="about_d"),
    path('contact_pg/', views.contact_pg, name="contact_pg"),
    path('products_pg/', views.products_pg, name="products_pg"),
    path('dispCateg/<itemCateg>', views.dispCateg, name="dispCateg"),
    path('displayProd/<int:dataid>/', views.displayProd, name="displayProd"),
    path('login/',views.login,name='login'),
    path('loginsave/',views.loginsave,name='loginsave'),
    path('customerlogin/',views.customerlogin,name='customerlogin'),
    path('logout/',views.logout,name='logout')

]