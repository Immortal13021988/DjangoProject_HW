from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.views import CategoryListinMenu
from .models import Blog
from .forms import BlogForm


class BlogListView(CategoryListinMenu, LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogDetailView(CategoryListinMenu, LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CategoryListinMenu, LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(CategoryListinMenu, LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(CategoryListinMenu, LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
