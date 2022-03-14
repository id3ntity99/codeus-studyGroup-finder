from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser
from .modules.auth import VerificationFactory


verification = openapi.Parameter(
    "idtoken",
    openapi.IN_FORM,
    description="ID token provided from client. ID token must be sent as form-data(multipart/form-data)",
    type=openapi.TYPE_STRING,
)


@api_view(["GET"])
def protected_resources(request):
    verification = VerificationFactory.get_verification_method(is_dummy=True)
    if request.method == "GET":
        cookie_val = request.COOKIES["study-login-cookie"]
        if cookie_val is None:
            return JsonResponse(
                {
                    "success": False,
                    "message": "study-login-cookie is null",
                }
            )
        else:
            user_info = verification.verify_token(cookie_val)
            # return HttpResponse(f"Welcome {user_info['name']}!")
            return Response(data=f"Welcom {user_info['name']}!")


@swagger_auto_schema(
    method="post",
    operation_description="Verify id token sent within a request header as a value of key 'idtoken'",
    manual_parameters=[verification],
)
@api_view(["POST"])
@parser_classes([MultiPartParser])
def verify(request):
    verification = VerificationFactory.get_verification_method(is_dummy=True)
    if request.method == "POST":
        id_token = request.POST["idtoken"]
        user_info = verification.verify_token(id_token)
        expires = user_info["exp"]
        res = JsonResponse(user_info)
        res.set_cookie(
            "study-login-cookie",
            id_token,
            expires=expires,
            httponly=True,
        )
        return res
    else:
        return Response({"success": False})
