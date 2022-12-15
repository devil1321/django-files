import os
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Track
from django.views.static import serve
from django.utils.encoding import smart_str
from django.conf import settings
# Create your views here.
import boto3
def addFile(request):
   
    if request.method == "POST":
        session = boto3.session.Session()
        client = session.client(
            's3',
            region_name='nyc3',
            endpoint_url='https://nyc3.digitaloceanspaces.com',
            aws_access_key_id='YOUR_ACCESS_KEY_ID',
            aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
        )
        with open('test.txt', 'rb') as file_contents:
            client.put_object(
                Bucket='media',
                Key=file,
                Body=file,
            )
        file = Track(file=request.POST.get('file'))
        file.save()
        return JsonResponse({'msg':'file added'})
    if request.method == "GET":
        files = Track.objects.all()
        print(files[0])
        return render(request,'add-file.page.html',{'files':files})
def getFile(request, filename):

    # Split the elements of the path
    response = HttpResponse(content_type='application/force-download') # mimetype is replaced by content_type for django 1.7
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
    response['X-Sendfile'] = smart_str(filename)
# It's usually a good idea to set the 'Content-Length' header too.
# You can also set any other required headers: Cache-Control, etc.
    return response
# It's usually a good idea to set the 'Content-Length' header too.
# You can also set any other required headers: Cache-Control, etc.