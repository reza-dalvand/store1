from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.generics import GenericAPIView
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response

from contactUs_module.models import ContactUs
from contactUs_module.serializers import ContactUsSerializer


class ContactUsView(GenericAPIView):
    serializer_class = ContactUsSerializer

    def get(self, request, *args, **kwargs):
        print(request, args, kwargs, 'bbbbbbbbbbb')

        return render(request, './contact-us/contactUs.html', {})

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, './contact-us/contactUs.html',
                          {'success_message': _('Your message has been successfully sent ')})

        field_errors = {}
        for field_name, field_error in serializer.errors.items():
            field_errors[field_name] = field_error[0]

        # return Response({'login': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        return render(request, './contact-us/contactUs.html', {"field_errors": field_errors})
