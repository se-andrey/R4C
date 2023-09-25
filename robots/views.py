import json
from django.http import JsonResponse
from robots.models import Robot
from django.middleware.csrf import get_token
from robots.schemas import valid_add_robot_json


def add_robot(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        validation_result = valid_add_robot_json(data)
        if validation_result:
            return validation_result
        try:

            model = data['model']
            version = data['version']
            created = data['created']
            serial = f'{model}-{version}'

            try:
                robot = Robot(
                    serial=serial,
                    model=model,
                    version=version,
                    created=created
                )
                robot.save()
                return JsonResponse({"message": "Robot successfully added."}, status=201)
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
