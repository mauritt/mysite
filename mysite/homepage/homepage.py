from django.conf.urls import url
from django.shortcuts import render
# from videos.models import Video


def index(request):    
    # videos = Video.getVideos().order_by('priority')
    # listSize = Video.getSmallerSize(3)
    # context = {'videos': videos,'video_width': listSize[0], 'video_height' :listSize[1]}
    context = {}
    return render(request, 'homepage/index.html', context)


urlpatterns = [
    url(r'^$', index, name='index'),
]