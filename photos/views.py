from django.views.generic import ListView, FormView
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, reverse

from .models import Post
from .forms import PostForm


class AllPosts(ListView):
    model = Post
    template_name = 'photos/post_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        query = self.request.GET.get('post-query', None)
        context = super().get_context_data()
        try:
            liked = self.request.session['liked']
        except KeyError:
            self.request.session['liked'] = []
            liked = self.request.session['liked']
        context['liked'] = liked
        if query:
            context['object_list'] = context['object_list'].filter(uploaded_by__icontains=query)
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
    liked = list(request.session['liked'])

    if request.method == "POST":
        response = {}
        post = get_object_or_404(Post, pk=post_pk)

        if post_pk in liked:
            post.likes -= 1
            liked.remove(post_pk)
            response['state'] = 'unliked'
        else:
            post.likes += 1
            liked.append(post_pk)
            response['state'] = 'liked'
        post.save()
        response['likes'] = post.likes
        request.session['liked'] = liked
        return JsonResponse(response)

    else:
        raise Http404
