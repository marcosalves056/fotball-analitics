from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RunDetectionView(APIView):
    def get(self, request):
        filename = request.query_params.get("file")
        if not filename:
            return Response({"error": "Missing 'file' parameter"}, status=status.HTTP_400_BAD_REQUEST)

        # Simulação de processamento
        result = {"message": f"Processed file {filename}", "detections": []}
        return Response(result)
