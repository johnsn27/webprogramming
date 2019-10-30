from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

def get(request):
    allPosts = Post.objects.order_by('-averageRating')[:5]
    context = {
        'allPosts': allPosts,
    }
    return render(request, 'polls/index.html', context)

def create_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        print('request')
        name = request.POST.get('name')
        summary = request.POST.get('summary')
        averagerating = request.POST.get('averagerating')

        response_data['name'] = name
        response_data['summary'] = summary
        response_data['averageRating'] = averagerating

        posts.create(
            name = name,
            summary = summary,
            averageRating = averagerating,
            )
        return JsonResponse(response_data)

    return render(request, 'polls/postForm.html', {'posts':posts})