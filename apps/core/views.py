from django.http import JsonResponse


def health_check(request):
    return JsonResponse(
        {
            "status": "healthy",
            "service": "prompt-editor",
            "version": "0.1.0",
        }
    )
