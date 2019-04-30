from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TaskSerializer2
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

class Tasklist(APIView):
    def get(self, request):
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer2(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Tasklist_detail(APIView):
    def get_object(self, num):
        try:
            return TaskList.objects.get(id=num)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, num):
        task_list = self.get_object(num)
        serializer = TaskListSerializer2(task_list)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, num):
        task_list = self.get_object(num)
        serializer = TaskListSerializer2(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, num):
        task_list = self.get_object(num)
        task_list.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

class Task(APIView):
    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404
    def get(self, request, num):
        task_list = self.get_object(num)
        tasks = task_list.task_set.all()
        serializer = TaskSerializer2(tasks,many=True)
        return Response(serializer.data)
