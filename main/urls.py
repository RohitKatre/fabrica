from django.conf.urls import url
from . views import HomePage, send_email, AboutUs, GalleryListView, \
    CertificationView, ContactView, ClientView, ProductView



urlpatterns = [
    url(r'^$', HomePage.as_view(), name="home_page"),
    url('^email/$', send_email, name='email'),
    url('^about/$', AboutUs.as_view(), name='about'),
    url('^products/$', ProductView.as_view(), name='products'),
    url('^gallery/$', GalleryListView.as_view(), name='gallery'),
    url('^certificates/$', CertificationView.as_view(), name='certificates'),
    url('^clients/$', ClientView.as_view(), name='client'),
    url('^contact/$', ContactView.as_view(), name='contact'),
]
