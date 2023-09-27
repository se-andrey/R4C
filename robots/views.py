import json

from django.http import JsonResponse, HttpResponse

from robots.models import Robot
from robots.schemas import valid_add_robot_json
from robots.excel_export import summary_excel


def add_robot(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        validation_result = valid_add_robot_json(data)
        if validation_result:
            return validation_result

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
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


def download_robot_summary(request):

    workbook = summary_excel()

    # Буфер в памяти для отчета
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=robot_summary.xlsx'
    workbook.save(response)

    return response
