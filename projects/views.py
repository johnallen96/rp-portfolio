from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.object.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Projects.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
