from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProfileScan
from .serializers import ProfileScanSerializer
from .services import analyze_profile

class ScanProfileView(APIView):

    def post(self, request):
        username = request.data.get("username")

        result = analyze_profile(username)

        scan = ProfileScan.objects.create(
            user=request.user,
            username=username,
            risk_score=result["risk_score"],
            is_fake=result["is_fake"]
        )

        serializer = ProfileScanSerializer(scan)

        return Response(serializer.data, status=status.HTTP_201_CREATED)