import csv
import io

from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes,permission_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductDetialsSerializer
from .models import ProductDetials
from .utils import generate_ai_description


from rest_framework.permissions import IsAuthenticated


def home(request):
    return render(request, 'home.html')




@api_view(['POST'])
@permission_classes([IsAuthenticated])

def generate_single_product_details(request):
    data = request.data

    required_fields = ['product_name', 'material', 'color', 'audience']
    for field in required_fields:
        if field not in data:
            return Response(
                {"error": f"'{field}' is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

    max_words = int(data.get("max_words", 50))  # default 50 words

    try:
        raw_description = generate_ai_description(
    data['product_name'],
    data['material'],
    data['color'],
    data['audience'],
    max_words
)

# ✅ Split AI response into 3 parts
        parts = [part.strip() for part in raw_description.split("\n\n") if part.strip()]

        descriptions = {
            "description_1": parts[0] if len(parts) > 0 else "",
            "description_2": parts[1] if len(parts) > 1 else "",
            "description_3": parts[2] if len(parts) > 2 else "",
        }

    except Exception as e:
        return Response(
            {"error": "AI generation failed", "details": str(e)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )

    product = ProductDetials.objects.create(
        product_name=data['product_name'],
        material=data['material'],
        color=data['color'],
        audience=data['audience'],
        description=descriptions
    )

    serializer = ProductDetialsSerializer(product)

    return Response(
        {
            "message": "Product details generated successfully",
            "data": serializer.data
        },
        status=status.HTTP_200_OK
    )

  















@api_view(['POST'])
@parser_classes([MultiPartParser])
def bulk_Create_ProductDetails(request):

    file = request.FILES.get('file')

    if not file:
        return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        decodeFile = file.read().decode("utf-8")
    except UnicodeDecodeError:
        return Response(
            {"error": "File decoding error. Please upload a valid CSV file."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        reader = csv.reader(io.StringIO(decodeFile))
        headers = next(reader)
        rows=[]
        for i, row in enumerate(reader):
            if i>=5:
                break
            rows.append(row)
            
    except Exception as e:
        return Response(
            {"error": "Error reading CSV file: " + str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response(
        {
            "message": "File processed successfully",
            "file_type": "Text/CSV",
            "headers": headers,
            "num_rows": rows,
            
        },
        status=status.HTTP_200_OK
    )
