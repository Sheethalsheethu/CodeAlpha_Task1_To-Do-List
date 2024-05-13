from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from todoApp.serializers import todoSerializer  # Adjusted serializer import
from todoApp.models import todo  # Adjusted model import
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Assuming you have an index.html template


@csrf_exempt
def todoApi(request, id=0):  # Adjusted function name to match the model name

    if request.method == 'GET':
        todos = todo.objects.all()  # Adjusted model name
        todo_serializer = todoSerializer(todos, many=True)  # Adjusted serializer name
        return JsonResponse(todo_serializer.data, safe=False)
    
    elif request.method == 'POST':
        todo_data = JSONParser().parse(request)
        todo_serializer = todoSerializer(data=todo_data)  # Adjusted serializer name
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(todo_serializer.errors, status=400)  # Return serializer errors with status
    
    elif request.method == 'PUT':
        todo_data = JSONParser().parse(request)
        todo_instance = todo.objects.get(id=id)  # Adjusted model name
        todo_serializer = todoSerializer(todo_instance, data=todo_data)  # Adjusted serializer name
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse(todo_serializer.errors, status=400)  # Return serializer errors with status
    
    elif request.method == 'DELETE':
        todo_instance = todo.objects.get(id=id)  # Adjusted model name
        todo_instance.delete()
        return JsonResponse("Deleted Successfully", safe=False)
