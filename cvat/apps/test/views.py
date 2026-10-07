# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from cvat.apps.engine.models import Task

from .serializers import AnnotationStatsSerializer
from .services import get_task_annotation_stats


class AnnotationStatsView(APIView):
    # TODO: replace with CVAT task permissions in step 4
    permission_classes = [permissions.AllowAny]

    def get(self, request, task_id: int):
        get_object_or_404(Task, pk=task_id)

        stats = get_task_annotation_stats(task_id)
        serializer = AnnotationStatsSerializer(instance=stats)
        return Response(serializer.data, status=status.HTTP_200_OK)
