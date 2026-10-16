from django.shortcuts import render

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return render(request, 'empmngt/technical_issue.html', status=404)
        return response
       
    def process_exception(self,request,Exception):
        return render(request, 'empmngt/technical_issue.html')