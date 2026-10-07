# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.db.models import Count, Q

from cvat.apps.engine.models import (
    LabeledImage,
    LabeledInterval,
    LabeledShape,
    LabeledTrack,
)


def get_task_annotation_stats(task_id: int) -> dict:
    # Annotation rows are spread over four tables; every row carries
    # job_id and label_id, so a task-scoped count is a plain ORM
    # aggregation filtered through job__segment__task.
    # - Shapes/tracks are filtered with parent__isnull=True so that
    #   skeleton child elements (which repeat their parent's label)
    #   are not double-counted.
    # - TrackedShape keyframes are counted via their parent
    #   LabeledTrack (TrackedShape has no label/job FK of its own).
    tables = (
        (LabeledShape, Q(parent__isnull=True)),
        (LabeledImage, Q()),
        (LabeledTrack, Q(parent__isnull=True)),
        (LabeledInterval, Q()),
    )

    merged: dict[str, int] = {}
    for model, extra_filter in tables:
        rows = (
            model.objects.filter(job__segment__task_id=task_id)
            .filter(extra_filter)
            .values("label__name")
            .annotate(c=Count("id"))
        )
        for row in rows:
            label_name = row["label__name"]
            merged[label_name] = merged.get(label_name, 0) + row["c"]

    counts = [
        {"label": label_name, "count": count}
        for label_name, count in sorted(merged.items(), key=lambda item: (-item[1], item[0]))
    ]

    return {"task_id": task_id, "counts": counts}
