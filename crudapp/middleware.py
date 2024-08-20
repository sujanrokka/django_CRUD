from django.http import HttpResponseForbidden

class IPFilterMiddleware:
    # ALLOWED_IPS = ['127.0.0.1', '182.93.85.133']  #  allowed IPs
    ALLOWED_IPS = ['127.0.0.1', '182.93.85.133']  
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = self.get_client_ip(request)
        if ip not in self.ALLOWED_IPS:
            return HttpResponseForbidden("Forbidden: Your IP is not allowed.")

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip