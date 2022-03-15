from django.urls import path
from django.views.generic.base import TemplateView

app_name = "dashboard"

urlpatterns = [
    path(
        "index",
        TemplateView.as_view(template_name="dashboard/index.html"),
        name="index",
    ),
    path(
        "gallery",
        TemplateView.as_view(template_name="dashboard/pages/gallery.html"),
        name="gallery",
    ),
    path(
        "widgets",
        TemplateView.as_view(template_name="dashboard/pages/widgets.html"),
        name="widgets",
    ),
    path(
        "profile",
        TemplateView.as_view(template_name="dashboard/pages/profile.html"),
        name="profile",
    ),
    path(
        "buttons",
        TemplateView.as_view(template_name="dashboard/pages/buttons.html"),
        name="buttons",
    ),
    path(
        "timeline",
        TemplateView.as_view(template_name="dashboard/pages/timeline.html"),
        name="timeline",
    ),
    path(
        "ribbons",
        TemplateView.as_view(template_name="dashboard/pages/ribbons.html"),
        name="ribbons",
    ),
    path(
        "general",
        TemplateView.as_view(template_name="dashboard/pages/general.html"),
        name="general",
    ),
    path(
        "tables",
        TemplateView.as_view(template_name="dashboard/pages/tables.html"),
        name="tables",
    ),
    path(
        "contacts",
        TemplateView.as_view(template_name="dashboard/pages/contacts.html"),
        name="contacts",
    ),
]
