Definition of Done

Core requirements
1) API endpoint returns the number of annotations per class for a specified CVAT task.
    Evidence:
2) Counts are read from database and verified against a task
    Evidence:
3) A page/section in the CVAT web interface calls the annotation analytics API for the selected task
    Evidence:
4) The annotation counts returned by the API are displayed as a graph
    Evidence:
5) The page displays a clear state when the selected task contains no annotations
    Evidence:
6) The page displays a clear error state when the analytics API request fails
    Evidence:


Authentication and Authorization
7) The analytics endpoint uses CVAT's existing authentication system
    Evidence:
8) An unauthenticated request is rejected
    Evidence:
9) A logged-in user without access to the requested task is rejected
    Evidence:
10) A user with access to the task can retrieve its analytics
    Evidence:
11) The analytics endpoint uses CVAT's existing authentication system
    Evidence:


Performance
12) The selected endpoint performance objective is measured using 5 runs + Raw measurement output is preserved + Median and spread are reported + CPU, RAM, operating system, and CVAT commit SHA are documented.
    Evidence:
13) The measured result is compared against the target defined in Objectives.md. If the target is missed, the reason is documented honestly.
    Evidence:


Additional Requirement (Filter or grouping)
14) At least one filter or grouping beyond the plain annotation count is implemented.
The reason for choosing it is documented.
    Evidence:


Advanced Requirements (WebSocket)

15) The graph updates when annotations change without requiring a manual page refresh.
    Evidence:

16) The page recovers when the WebSocket connection drops and subsequently reconnects.
    Evidence:


Documentation and Delivery
17) Plan.md was committed before implementation code.
    Evidence: <git commit SHA>
18) docs/Objectives.md contains measurable objectives and the final measurements
    Evidence:
19) Work is committed progressively on dev-test01. Commit messages describe what changed and why.
    Evidence: <git log>
18) docs/Objectives.md contains measurable objectives and the final measurements
    Evidence: