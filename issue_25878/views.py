from django.shortcuts import render
from django.http import HttpResponse

def error_response(message):
    def view_func(request):
        return HttpResponse(message)
    return view_func

err_400 = error_response('400\n')
err_403 = error_response('403\n')
err_404 = error_response('404\n')
err_500 = error_response('500\n')

# Just for understanding
custom_view_func = error_response

feature = custom_view_func("Feature URL response\n")
