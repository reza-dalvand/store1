from rest_framework import serializers
from contactUs_module.models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['fullname', 'email', 'subject', 'message']

    def preparing_message(self):
        self.message = ContactUs(
            fullname=self.validated_data['fullname'],
            email=self.validated_data['email'],
            subject=self.validated_data['subject'],
            message=self.validated_data['message'])

    def save(self):
        self.preparing_message()
        self.message.save()
        return self.message
