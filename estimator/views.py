from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from .utils import getDurationDays, impactEstimator, severeImactEstimator


class EstimatorViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    

    def create(self, request, *args, **kwargs):
        '''collates all data for estimate functions'''

        estimate = {
            'data': request.data,
            'impact': impactEstimator(request.data),
            'severeImpact': severeImactEstimator(request.data)
        }

        return Response({'estimate': estimate}, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['POST'], url_path='xml')
    def xml_output(self, request, format=None):
        '''returns an xml output of the create method'''
        estimate = {
            'data': request.data,
            'impact': impactEstimator(request.data),
            'severeImpact': severeImactEstimator(request.data)
        }

        return Response({'estimate': estimate}, status=status.HTTP_200_OK)