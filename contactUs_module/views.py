from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.utils.translation import gettext_lazy as _
from contactUs_module.serializers import ContactUsSerializer
from site_settings.models import SiteSetting


class ContactUsView(GenericAPIView):
    """validated form data with serializer instead of model form"""
    serializer_class = ContactUsSerializer
    queryset = SiteSetting.objects.filter(is_active=True).first()

    def get(self, request, *args, **kwargs):
        return render(request, './contact-us/contactUs.html', {'settings': self.queryset})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, './contact-us/contactUs.html',
                          {'success_message': _('Your message has been successfully sent ')})

        field_errors = {}
        for field_name, field_error in serializer.errors.items():
            field_errors[field_name] = field_error[0]
        return render(request, './contact-us/contactUs.html', {"field_errors": field_errors})
