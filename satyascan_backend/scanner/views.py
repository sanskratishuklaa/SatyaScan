from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProfileScan
from .serializers import ProfileScanSerializer
from .services import analyze_profile
from django.contrib.auth import get_user_model

User = get_user_model()


class ScanProfileView(APIView):

    def post(self, request):

        username = request.data.get("username")

        if not username:
            return Response(
                {"error": "username is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔥 FIX: no login dependency (hackathon mode)
        user = User.objects.first()

        if not user:
            return Response(
                {"error": "No user found in database"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        result = analyze_profile(username)

        if not isinstance(result, dict):
            return Response(
                {"error": "Analysis failed"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        scan = ProfileScan.objects.create(
            user=user,
            username=username,
            risk_score=result["risk_score"],
            is_fake=result["is_fake"]
        )

        return Response({
            "username": username,
            "risk_score": result["risk_score"],
            "is_fake": result["is_fake"],
            "verdict": "Fake Profile" if result["is_fake"] else "Real Profile",
            "confidence": result.get("confidence", 0),
            "reasons": result.get("reasons", []),
            "recommendation": result.get("recommendation", "")
        }, status=status.HTTP_201_CREATED)


class ScanHistoryView(APIView):

    def get(self, request):

        # 🔥 FIX: no login required
        user = User.objects.first()

        scans = ProfileScan.objects.filter(user=user).order_by('-id')

        data = []
        for scan in scans:
            data.append({
                "username": scan.username,
                "risk_score": scan.risk_score,
                "is_fake": scan.is_fake
            })

        return Response(data)