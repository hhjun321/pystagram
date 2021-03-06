# coding: utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Photo
from photo.forms import PhotoEditForm
# Create your views here.

def single_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    print(photo.image_file.url)
    response_text = '<p>{photo_id}번 ... {photo_id}번 사진출력</p>'
    response_text += '<p>{photo_url}</p>'
    response_text += '<p><img src="{photo_url}" width=200 height=200/></p>'
    return HttpResponse(response_text.format(
                                            photo_id=photo_id,
                                            photo_url=photo.image_file.url))
    
def new_photo(request):
    if request.method == "GET":        
        edit_form = PhotoEditForm()
    elif request.method == "POST":
        edit_form = PhotoEditForm(request.POST, request.FILES)
        
        if edit_form.is_valid():
            new_photo = edit_form.save()
            
            return redirect(new_photo.get_absolute_url())
    
    return render(request, 'new_photo.html', {
                                                'form':edit_form,})
    
    