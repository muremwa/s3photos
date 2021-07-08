from django.views.generic import ListView, FormView
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Post
from .forms import PostForm
from .serializers import PostSerializer


class AllPosts(ListView):
    model = Post
    template_name = 'photos/post_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        query = self.request.GET.get('post-query', '')
        context = super().get_context_data()

        if query and 'object_list' in context:
            context['object_list'] = context['object_list'].filter(uploaded_by__icontains=query)

        context.update({
            'liked': self.request.session.setdefault('liked', []),
            'post_query': query
        })

        return context


class UploadImage(FormView):
    template_name = 'photos/upload.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('photos:index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def like_or_unlike(request, post_pk):
    liked_posts = list(request.session.setdefault('liked', []))

    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_pk)
        liked = False

        if post_pk in liked_posts:
            post.likes -= 1
            liked_posts.remove(post_pk)
        else:
            post.likes += 1
            liked_posts.append(post_pk)
            liked = True

        post.save()
        request.session['liked'] = liked_posts

        return JsonResponse({
            'liked': liked,
            'likes': post.likes
        })

    else:
        raise Http404


def all_posts_api(request):
    posts = Post.objects.all()

    query = request.GET.get('post-query', None)

    if query:
        posts = posts.filter(uploaded_by__icontains=query)

    return JsonResponse(
        data={
            'posts': PostSerializer(posts, many=True).data,
            'liked': request.session.setdefault('liked', [])
        },
        safe=False
    )


def upload_image_api(request):
    if request.method == 'GET':
        form = PostForm()
        fields = {field: form.fields[field].help_text for field in form.fields}
        return JsonResponse({
            'fields': fields
        })

    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save()
            response = {
                'success': True,
                'post': PostSerializer(post).data
            }

        else:
            response = {
                'success': False,
                'errors': form.errors
            }

        return JsonResponse(response)
