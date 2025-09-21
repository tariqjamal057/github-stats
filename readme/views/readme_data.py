from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from django.http import HttpResponse

from readme.forms.readme_data import CreateReadmeFileForm
from readme.models.readme_column import Component, Section
from readme.models.readme_data import ReadmeData


class CreateReadmeFile(CreateView):
    form_class = CreateReadmeFileForm
    template_name = "readme/file/create_file.html"

    def get_success_url(self):
        return reverse_lazy("readme:create_readme_data", kwargs={"id": self.object.pk})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UpdateReadmeFile(View):
    def post(self, request, *args, **kwargs):
        filename = request.POST.get("file_name")
        readme_data = ReadmeData.objects.get(id=kwargs.get("id"))
        readme_data.file_name = filename
        readme_data.save()
        return HttpResponse(status=200)


class ReadmeDataView(View):
    template_name = "readme/file_content/create_readme.html"
    success_url = reverse_lazy("readme:home")
    component_column = Component
    section_column_model = Section

    def get(self, request, *args, **kwargs):
        context = {
            "compoments": self.component_column.objects.all(),
            "sections": self.section_column_model.objects.all(),
            "readme_data": ReadmeData.objects.get(id=kwargs.get("id")),
        }
        return render(request, self.template_name, context)
