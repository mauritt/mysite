from django.shortcuts import render
from django.http import Http404
from .models import Video, Role, Company



# Create your views here.


def index(request):
    videos = Video.getVideos().order_by('priority')
    listSize = Video.getSmallerSize(3)
    context = {'videos': videos,'video_width': listSize[0], 'video_height' :listSize[1]}
    return render(request, 'videos/index.html', context)

def detail(request, slug):
    try:
        video = Video.objects.get(slug = slug)
    except Video.DoesNotExist:
        raise Http404()
    else:
        if video.hidden == True:
            pass
        detailSize = Video.getSmallerSize(1.5)
        context = {'video': video, 'company':video.company, 'video_width': detailSize[0], 'video_height' :detailSize[1]  }
        return render(request, 'videos/detail.html', context)