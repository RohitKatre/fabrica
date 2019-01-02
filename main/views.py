from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
# Create your views here.
from .models import Gallery, Client, Certificate
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse


class HomePage(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        gallery_imgs = Gallery.objects.order_by('-id')[:10]
        context["gallery_imgs"] = gallery_imgs
        if gallery_imgs and len(gallery_imgs) < 5:
            context["g_img_count"] = range(5 - len(gallery_imgs))
        elif len(gallery_imgs) == 0:
            context["g_img_count"] = range(5)
        else:
            context["g_img_count"] = []

        clients = Client.objects.order_by('-id')
        context['clients'] = clients
        return context

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            from_email = "info@turtlelabs.co.in"
            message = form.cleaned_data['message']
            message = name + "\n\n" + message
            try:
                send_mail(subject, message, from_email, ['rudra.katre@gmail.com'])
            except BadHeaderError as e:
                return JsonResponse({"error_message": 'Invalid header found.', "status_code": 500, "error": str(e)})
        return JsonResponse({'status_code': 200, "message":"Email has send sucessfully"})
    else:
        return JsonResponse({'status_code': 500, "error": "Invalid Usage Error"})

class AboutUs(TemplateView):
    template_name = "main/about_us.html"

class ProductView(TemplateView):
    template_name = "main/product.html"

class GalleryListView(ListView):
    model = Gallery
    template_name = "main/gallery.html"

class CertificationView(ListView):
    template_name = "main/certificates.html"
    model = Certificate

    def get_context_data(self, **kwargs):
        context = super(CertificationView, self).get_context_data(**kwargs)
        context["img_format"] = [".png", ".jpg", ".jpeg"]
        context["pdf_format"] = [".pdf", ".txt", ".doc", ".docx"]
        return context

class ContactView(TemplateView):
    template_name = "main/contact.html"

class ClientView(ListView):
    model = Client
    template_name = "main/client.html"