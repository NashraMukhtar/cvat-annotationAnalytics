# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cvat.apps.engine.models import Task
from cvat.apps.engine.permissions import TaskPermission
from cvat.apps.iam.permissions import get_iam_context

from .serializers import AnnotationStatsSerializer
from .services import get_task_annotation_stats


class AnnotationStatsView(APIView):
    # IsAuthenticated relies on CVAT's default authentication classes
    # (Token/Session/AccessToken/Basic), so anonymous requests are rejected
    # with 401 before the view is dispatched.
    # The OPA-based PolicyEnforcer is not used here because it only works
    # with ViewSets (it relies on view.detail/view.action); instead the same
    # policy is enforced below via TaskPermission, like other CVAT code does.
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id: int):
        task = get_object_or_404(Task, pk=task_id)

        # Same authorization as GET /api/tasks/<id>/annotations:
        # CVAT's OPA policy decides whether this user may view the
        # annotations of this task (owner/assignee/admin/org member rules).
        permission = TaskPermission.create_base_perm(
            request,
            self,
            TaskPermission.Scopes.VIEW_ANNOTATIONS,
            get_iam_context(request, task),
            task,
        )
        result = permission.check_access()
        if not result.allow:
            raise PermissionDenied(
                ", ".join(result.reasons) or "You do not have permission to view this task"
            )

        stats = get_task_annotation_stats(task.id)
        serializer = AnnotationStatsSerializer(instance=stats)
        return Response(serializer.data, status=status.HTTP_200_OK)
