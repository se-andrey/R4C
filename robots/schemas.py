from datetime import datetime
from django.http import JsonResponse


def valid_add_robot_json(data):
    version = data.get('version')
    model = data.get('model')
    created = data.get('created')
    if len(version) not in (1, 2) or len(model) not in (1, 2) or len(data) != 3:
        return JsonResponse({'error': 'Invalid data'}, status=400)
    try:
        datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
    except Exception:
        return JsonResponse({'error': 'Invalid data'}, status=400)
