from django.shortcuts import render
from django.http import JsonResponse  # Used to send data to ajax.done() method
from .ateliware_git_api import GitAPI
from django.views import View


# Creating our views here!
class ViewRepositories(View):

    def get(self, request):
        all_repos = GitAPI().get_all_repo()
        return render(request, 'templates/ateliware_repos.html', {'repositores': all_repos})


def update_repo_by_ajax(request):
    git_api_class = GitAPI()
    new_repos = git_api_class.cad_or_up_repo()
    all_repos = git_api_class.get_all_repo()
    return JsonResponse({'repositores': all_repos, 'best_found': new_repos})
