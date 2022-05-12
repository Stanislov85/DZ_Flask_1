from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement



class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()


