from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import HttpResponse, JsonResponse
from dotenv import load_dotenv
import os



dotenv_path = os.path.abspath("../.env")
load_dotenv(dotenv_path)

DUMMY_ID = "407408718192.apps.googleusercontent.com"
CLIENT_ID = os.getenv("CLIENT_ID")


def verify_token(token):
    try:
        user_info = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        return user_info
    except ValueError as e:
        return e


def protected_resources(request):
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
            user_info = verify_token(cookie_val)
            return HttpResponse(f"Welcome {user_info['name']}!")


def verify(request):
    if request.method == "POST":
        id_token = request.POST["idtoken"]
        user_info = verify_token(id_token)
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
        return JsonResponse({"success": False})
