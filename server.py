# server.py

'''
This module contains a FastAPI application that uses Uvicorn (ASGI)
to send JSON data.
'''


import canvas_assignment_api
import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/assignments')
def get_upcoming_assignments():
    '''
    Gets assignments from Canvas, filters into upcoming, and returns
    the assignments as a list of dictionaries.
    '''

    canvas_api = canvas_assignment_api.CanvasApiAssignments('TOKEN')

    assignments = canvas_api.get_all_assignments()

    if not assignments:
        return

    filtered_assignments = canvas_api.filter_assignments_due(assignments)

    return filtered_assignments


if __name__ == '__main__':
    uvicorn.run("server:app", port = 8080, log_level = "info")

