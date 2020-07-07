from .model.client import Client
from .model.address import Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Client
        fields = '__all__'

    

class ClientSerializer(serializers.ModelSerializer):
    address_info  = serializers.SerializerMethodField(required=False)

    def get_address_info(self, obj):
        try:

            if obj.Address:
                return({"Postcode": obj.Address.Postcode,
                        "City": obj.Address.City,
                        "State": obj.Address.State})
                        
        except (AttributeError, KeyError, TypeError) as e:
            return e
            
    class Meta:
        model  = Client
        fields = '__all__'

