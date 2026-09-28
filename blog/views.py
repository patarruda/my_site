from django.http import Http404
from django.shortcuts import render
from django.utils import lorem_ipsum
from django.utils.text import slugify

# Create your views here.

lorem_text = lorem_ipsum.paragraphs(3)

image1_url = "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
image2_url = "https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
image3_url = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
image4_url = "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1170&q=80"
image5_url = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
image6_url = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"

posts_list = [
    {'id': 1, 'title': 'Hiking Adventures', 'content': lorem_text, 'updated_at': '2025-10-01 10:00:00', 'image_url': image1_url},
    {'id': 2, 'title': 'Programming Tips', 'content': lorem_text, 'updated_at': '2024-12-01 11:00:00', 'image_url': image2_url},
    {'id': 3, 'title': 'Healthy Living', 'content': lorem_text, 'updated_at': '2025-03-01 12:00:00', 'image_url': image3_url},
    {'id': 4, 'title': 'Artificial Intelligence', 'content': lorem_text, 'updated_at': '2026-05-01 13:00:00', 'image_url': image4_url},
    {'id': 5, 'title': 'Exploring the Cosmos', 'content': lorem_text, 'updated_at': '2024-06-01 14:00:00', 'image_url': image5_url},
    {'id': 6, 'title': 'Hopeful Beginnings', 'content': lorem_text, 'updated_at': '2026-07-01 15:00:00', 'image_url': image6_url},
]   

blog_owner = "Max"
presentation = "Welcome to my blog! Here, I share my thoughts, experiences, and insights on various topics. From hiking adventures to programming tips, healthy living, and the wonders of artificial intelligence, I aim to provide valuable content for my readers. Join me on this journey as we explore the cosmos of knowledge together!"

def home(request):
    # 3 ultimos posts
    latest_posts = sorted(posts_list, key=lambda x: x['updated_at'], reverse=True)
    latest_posts = latest_posts[:3]  # Pega os 3 primeiros posts mais recentes
    return render(request, 'blog/home.html', {'latest_posts': latest_posts, 'blog_owner': blog_owner, 'presentation': presentation})

def posts(request):
    return render(request, 'blog/posts.html', {'posts': posts_list, 'blog_owner': blog_owner})

def post_detail(request, post_slug):
    post = next((post for post in posts_list if slugify(post['title']) == post_slug), None)
    
    if post is None:
        # Se o post não for encontrado, você pode redirecionar para uma página de erro ou retornar 404
        return Http404("Post not found")
    
    return render(request, 'blog/post_detail.html', {'post': post, 'blog_owner': blog_owner})
    