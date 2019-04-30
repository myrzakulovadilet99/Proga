from django.contrib.auth.models import User
from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



class Tasklist(generics.ListCreateAPIView):
    # queryset = TaskList.objects.all()

    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)

    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class Tasklist_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2


