from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

# Create your views here.
def home_page(request):
    print("Home Page Function call")
    # return HttpResponse("This is your page is call")
    # data = {
    #     'first_name':"sachin",
    #     "Last_name":"Rao",
    #     "Roll_Number":115,
    # }
    data = ["sachin" , "yadav" , 51]  # Normal data ho that time we can surve the data directly 
    return JsonResponse(data , safe=False) # data send into the json format


