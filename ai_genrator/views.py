import csv
import io

from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return render(request, 'home.html')





@api_view(['POST'])
def generate_single_product_details(request):
    data=request.data
    
    required_filds=['product_name','material','color','audience']
    for field in required_filds:
        if field not in data:
            return Response(
                {"error": f"'{field}' is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    # print user entered data
    print("User Entered Data:")
    for key, value in data.items():
        print(f"{key}: {value}")
    # Dummy response
    return Response(
        {
            "message": "Product details generated successfully",
            "product_name": data.get("product_name"),
            "material": data.get("material"),
            "color": data.get("color"),
            "audience": data.get("audience"),
            "description": "This is a dummy description generated for the product."
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
