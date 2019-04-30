from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer

@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer2(task_lists, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskListSerializer2(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def task_list_num(request, num):
    try:
        task_list = TaskList.objects.get(id=num)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    if request.method == 'GET':
        serializer = TaskListSerializer(task_list)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = TaskListSerializer(instance=task_list, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


def task_list_tasks(request,num):
    try:
        tasks = TaskList.objects.get(id=num)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    tasks_list = tasks.task_set.all()
    serializer = TaskSerializer(tasks_list, many=True)
    return JsonResponse(serializer.data, safe=False)

