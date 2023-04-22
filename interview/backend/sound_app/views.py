from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse

from .play import play_file
from .record import record


@csrf_exempt
def record_view(request):
    if request.method == 'POST':
        duration = int(request.POST.get('duration'))
        fs = int(request.POST.get('fs'))
        filename = request.POST.get('filename')
        threshold = int(request.POST.get('threshold'))

        record(duration, fs, filename, threshold)

        response_data = {'filename': filename}
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request method'})


def play_view(request, filename):
    try:
        play_file(filename)
        with open(filename, 'rb') as f:
            response = FileResponse(f, content_type='audio/wav')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    except:
        return JsonResponse({'error': 'File not found'})
