Annotation Analytics — Implementation Plan

Goal:
Add an Annotation Analytics feature to CVAT that provides an API for counting annotations by class for a task and a web interface that visualises those numbers as a graph.



implementation order + Allocated time:
1) Understand the existing CVAT architechture and Data model (~45 mins)
    a. trace relationship between Tasks, Jobs, annotations, labels
    b. check how to obtain the label name for annotations for a task
    c. identify the existing authentication, authorization, API routes, frontend patterns that should be reused
2) Create Django test app (~30 mins)
    a. integrate it with CVAT's existing backend structure and routing
3) Implement annotation-count API (~1.5 - 2 hrs)
    a. add an endpoint that accepts task ID
    b. query the database to get annotations of a task
    c. group those annotations by class/label and count them
    d. verify the result against COCO task
    e. once the endpoint is hitting in postman and returning correct JSON, move forward
4) Add authentication and task-access authorization (~45 mins)
    a. Use CVAT's existing auth system (they must have created middlewares before hand and i would just have to find and use them)
    b. Reject unauthenticated requests.
    c. Reject authenticated users who do not have access to the requested task.
    d. verify both cases in Postman
5) bulid frontend page (~1-1.5 hrs mins)
    a. add analytics page/view to CVAT (with dummy text like 'GRAPH')
    b. call backend analytics endpoint for selected task
    c. display the returned annotation counts as graph
6) handle required UI states (~20 mins)
    a. state when task contains no annotations
    b. state when API failed
    c. page should remain usable in both cases and must not hang
7) Define and measure one performance objective (~45 mins)
    a. Choose a measurable response-time target for the analytics endpoint.
    b. Measure it five times using the same task and environment.
    c. Report the raw measurements, median, spread, machine details, and CVAT commit SHA.



Either skip or Move ahead if time permits (if no time left: test the feature, create PR, update docs and record Loom video)
8) Add one filter or grouping (~45 mins)
    a. Add filtering the graph by label OR by number of annotations (display where annotations > 10).
    b. Document why the selected filter/grouping is useful.
9) Add live WebSocket updates if time permits (~1-2 hrs)
    a. Update the analytics graph when annotations change without requiring a manual page refresh.
    b. If implemented, handle WebSocket disconnection and reconnection.
    c. This work will only begin after requirements 1–4 are stable.
10) Test, clean up, document, and prepare the submission (~50 mins)
    a. Verify all completed requirements against the Definition of Done.
    b. Remove dead code, commented-out code, debug code, and stray files.
    c. Review the Git history and commit messages.
    d. Complete the Objectives and Definition of Done documents.
    e. Record the required Loom demonstration and technical explanation.
    f. Create the final pull request from dev-test01 into the main branch of my own fork.



Initial Scope Decision:

The first priority is requirements 1–4: the database-backed API, frontend page, graph, and required empty/error handling. These will be completed and verified before starting WebSocket work.

WebSocket live updates and reconnection are intentionally deferred until the required foundation is working. If time runs short, I will stop at the last stable requirement, document what remains unfinished, and submit the working implementation rather than rushing an unreliable feature.

If I reach requirement 10, I will add a short decision record below describing the approach taken, the approach rejected, and the cost of rejecting it.