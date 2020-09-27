from django.views.generic import ListView, FormView
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, reverse

from .models import Post
from .forms import PostForm


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
