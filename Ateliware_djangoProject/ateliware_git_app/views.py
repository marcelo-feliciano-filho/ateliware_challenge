from django.shortcuts import render
from django.http import JsonResponse  # Used to send data to ajax.done() method
from .ateliware_git_api import GitAPI
from django.views import View


# Creating our views here!
class ViewRepositories(View):
    """
    This class creates the view to application
    """

    def get(self, request):
        git_api_class = GitAPI()  # Initializes GitAPI class
        all_repos = git_api_class.get_all_repo()  # Get all previous foung apps
        fields = git_api_class.tb_repo._meta.get_fields()  # Receives all fields from TbGitRepository
        # Creates and formats the table head by list comprehension
        head = [str(h).split('_')[-1].split('.')[-1] if not('up_at' in str(h)) else 'Last Update' for h in fields]
        head.remove('url')  # Removes url from header, once it´s a link over repo´s name

        return render(request, 'ateliware_repos.html', {'repositores': all_repos, 'header': head})


def update_repo_by_ajax(request):
    """
    Such function aims to return a JsonResponse to ajax.done() method in order to update
    datatables on html.
    """
    git_api_class = GitAPI()
    new_repos = git_api_class.cad_or_up_repo()
    all_repos = git_api_class.get_all_repo()
    return JsonResponse({'repositores': all_repos, 'best_found': new_repos})
