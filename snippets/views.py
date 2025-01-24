from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Snippet, Language
from .forms import SnippetForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

class SnippetAdd(CreateView):
    model = Snippet
    fields = ['name', 'description', 'snippet', 'language', 'public']
    template_name = 'snippets/snippet_form.html'
    success_url = reverse_lazy('index')

class SnippetEdit(UpdateView):
    model = Snippet
    fields = ['name', 'description', 'snippet', 'language', 'public']
    template_name = 'snippets/snippet_form.html'
    success_url = reverse_lazy('index')

class SnippetDelete(DeleteView):
    model = Snippet
    template_name = 'snippets/snippet_confirm_delete.html'
    success_url = reverse_lazy('index')
    
class PublicSnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/public_snippets.html'  # Cambiar a public_snippets.html
    context_object_name = 'snippets'

    def get_queryset(self):
        selected_language = self.request.GET.get('language', '')
        queryset = Snippet.objects.filter(public=True)
        if selected_language:
            queryset = queryset.filter(language__name=selected_language)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['languages'] = Language.objects.all()
        context['selected_language'] = self.request.GET.get('language', '')
        return context

class SnippetDetails(View):
    def get(self, request, *args, **kwargs):
        snippet_id = self.kwargs["id"]
        snippet = get_object_or_404(Snippet, id=snippet_id)
        language = snippet.language.name  # Obtener el nombre del lenguaje
        if '://' in language:
            language = language.split('/')[-1]  
            language = language  
        return render(
            request, 
            "snippets/snippet.html", 
            {
                "snippet": snippet,
                "edit_url": reverse_lazy('snippet_edit', kwargs={'pk': snippet_id}),
                "language": language
            }
        )


class UserSnippets(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        snippets = Snippet.objects.filter(user=request.user)
        return render(
            request,
            "snippets/user_snippets.html",
            {"snippets": snippets},
        )


class SnippetsByLanguage(View):
    def get(self, request, *args, **kwargs):
        language_slug = self.kwargs["language"]
        snippets = Snippet.objects.filter(language__slug=language_slug, public=True)
        return render(request, "snippets/snippets_by_language.html", {"snippets": snippets, "language": language_slug})

class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/snippet_detail.html'
    context_object_name = 'snippet'
    
class SnippetCreateView(CreateView):
    model = Snippet
    form_class = SnippetForm
    template_name = 'snippets/snippet_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Create Snippet'))
        return form

class Login(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Login'))
        return render(request, 'snippets/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            form.helper = FormHelper()
            form.helper.add_input(Submit('submit', 'Login'))
            return render(request, 'snippets/login.html', {'form': form})

class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')

class Index(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        snippets = Snippet.objects.filter(public=True).values('id', 'name', 'description', 'user__username', 'created')
        context = {"snippets": snippets}
        username = request.user.username if request.user.is_authenticated else None
        if username:
            context["user_snippets_url"] = reverse_lazy('user_snippets', kwargs={'username': username})
        else:
            context["user_snippets_url"] = None
        return render(request, "index.html", context)

def index(request):
    selected_language = request.GET.get('language', '')
    snippets = Snippet.objects.filter(public=True).select_related('user', 'language').values('id', 'name', 'description', 'user__username', 'created')
    if selected_language:
        snippets = snippets.filter(language__name=selected_language)
    languages = Language.objects.all()
    return render(request, 'index.html', {
        'snippets': snippets,
        'languages': languages,
        'selected_language': selected_language
    })

def snippet_detail(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    if '://' in snippet.language.slug:
        snippet.language.slug = snippet.language.slug.split('/')[-1]
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})
