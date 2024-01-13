from django.views.generic import ListView, DetailView
from .models import Post
from django.http import Http404
from django.shortcuts import render



class PostsList(ListView):

    queryset = Post.objects.order_by('-datetime_post')
    template_name = 'posts.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'news'
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            
            return render(request, 'no_post.html', status=404)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)