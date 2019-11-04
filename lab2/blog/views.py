from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Post


def get(request):
    posts = Post.objects.order_by('-id')[:5]
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def getmoreinfo(request, id):
    postid = get_object_or_404(Post, pk=id)
    return render(request, 'getmoreinfo.html', {'postid': postid})


def create_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        title = request.POST.get('title')
        description = request.POST.get('description')

        response_data['title'] = title
        response_data['description'] = description

        Post.objects.create(
            title=title,
            description=description,
        )
        return JsonResponse(response_data)

    return render(request, 'create_post.html', {'posts': posts})


@csrf_exempt
def deleteTest(request):
    posts = Post.objects.order_by('-id')[:5]
    context = {
        'posts': posts,
    }
    return render(request, 'delete.html', context)


@csrf_exempt
def delete(request, pk):
    if request.method == 'DELETE':
        Post.objects.get(pk=pk).delete()
        return HttpResponse("car with pk %s deleted" % pk, content_type='application/json')
    return HttpResponse("Not a delete request")

@csrf_exempt
def put1(request):
    posts = Post.objects.order_by('-id')[:5]
    context = {
        'posts': posts,
    }
    return render(request, 'putIndex.html', context)

def put2(request,pk):
    posts = Post.objects.order_by('-id')[:5]
    context = {
        'posts': posts,
    }
    return render(request, 'put.html', context)

@csrf_exempt
def put3(request, pk):
    if request.method != 'PUT':
        obj = Post.objects.get(pk=pk)
        obj.title = request.POST.get('title')
        obj.description = request.POST.get('description')
        obj.save()
        return HttpResponse("car with pk %s deleted" % pk, content_type='application/json')
    return HttpResponse("Not a delete request")
