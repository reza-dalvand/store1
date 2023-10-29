from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from contactUs_module.serializers import ContactUsSerializer
from site_settings.models import SiteSetting


class ContactUsView(GenericAPIView):
    serializer_class = ContactUsSerializer
    queryset = SiteSetting.objects.filter(is_active=True).first()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'contact us': 'successful register message'}, status=status.HTTP_201_CREATED)
        return Response({'contact us': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
