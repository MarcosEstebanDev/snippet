from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SnippetAdd, SnippetEdit, SnippetDelete, SnippetDetails, UserSnippets, SnippetsByLanguage, Index, PublicSnippetListView, SnippetDetailView, SnippetCreateView, Login, Logout
from . import views

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path(
        "language/<str:language>/",
        SnippetsByLanguage.as_view(),
        name="snippets_by_language",
    ),
    path(
        "user/<str:username>/",
        UserSnippets.as_view(),
        name="user_snippets",
    ),
    path("snippet/<int:id>/", views.snippet_detail, name="snippet_detail"),
    path("add/", SnippetAdd.as_view(), name="snippet_add"),
    path("edit/<int:pk>/", SnippetEdit.as_view(), name="snippet_edit"),  # Ensure 'pk' is used
    path("delete/<int:pk>/", SnippetDelete.as_view(), name="snippet_delete"),
    path("public/", PublicSnippetListView.as_view(), name="public_snippets"),
    path('create/', SnippetCreateView.as_view(), name='snippet_create'),
    path('snippet/<int:pk>/', SnippetDetailView.as_view(), name='snippet_detail'),  # Ensure the name matches
]
