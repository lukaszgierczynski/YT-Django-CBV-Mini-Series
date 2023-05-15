from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.shortcuts import get_object_or_404
from django.db.models import F


class Ex2View(TemplateView):

    """TemplateResponseMixin
    Provides a mechanism to construct a TemplateResponse, given a suitable context.
    Attributes:
    """
    template_name = "ex2.html"
    #template_engine = The Name of a template engine to use for loading the template.
    #response_class = Custom template loading or custom context objext instantiation
    #content_type = Default Django uses 'text/html'

    """ get_context_data(**kwargs) is a method inherited from ContextMixin """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=1)
        context['data'] = "Context Data for Ex2"
        return context


class PostPreLoadTaskView(RedirectView):

    # url = 'http://youtube.com/veryacademy'
    pattern_name = 'cbv:singlepost'
    # permanent = HTTP status code returned (True = 301, False = 302, Default = False)

    def get_redirect_url(self, *args, **kwargs):
        # post = get_object_or_404(Post, pk=kwargs['pk'])
        # post.count = F('count') + 1
        # post.save()

        post = Post.objects.filter(pk=kwargs['pk'])
        post.update(count=F('count') + 1)

        return super().get_redirect_url(*args, **kwargs)


class SinglePostView(TemplateView):

    template_name = "ex4.html"  # single.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return context
