from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from readme.models import Component, Section


class ReadmeColumnList(ListView):
    model = Component
    template_name = "build_readme.html"
    section_column_model = Section
    context_object_name = "columns"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["columns"] = self.model.objects.filter()
        context["groups"] = self.section_column_model.objects.all()
        return context


class ManageReadmeContentView(View):
    # def get(self, request):
    #     return render(request, 'partials/element_form.html')
    def get(self, request, *args, **kwargs):
        column = Component.objects.get(id=kwargs['id'])
        return render(request, 'partials/element_form.html', {'column': column})


class AddElementView(View):
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        element_html = f"""
        <div class="selected-element shadow p-2 rounded mb-2 transition-all duration-300">
            <h3 class="font-semibold">{title}</h3>
            <p>{content}</p>
        </div>
        """
        
        readme_content = f"""
        <div class="p-4">
            <h1 class="text-2xl font-bold">{title}</h1>
            <div class="mt-4">
                {content}
            </div>
        </div>
        """
        
        return HttpResponse(element_html + f"""
            <div hx-swap-oob="innerHTML:#readme-data">
                {readme_content}
            </div>
        """)