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
        git_api_class = GitAPI([])  # Initializes GitAPI class
        all_repos = git_api_class.get_all_repo()  # Get all previous foung apps
        langs = git_api_class.allowed_lang  # List with all allowed languages
        head = ['Repositório', 'Linguagem', 'Estrelas', 'Commits', 'Observadores', 'Branches', 'forks', 'Dúvidas',
                'Última Atualização']  # Datatables header seen in pt-br by front-end

        return render(request, 'ateliware_repos.html', {'repositories': all_repos, 'header': head, 'languages': langs})


def update_repo_by_ajax(request):
    """
    Such function aims to return a JsonResponse to ajax.done() method in order to update
    datatables on html.
    """
    git_api_class = GitAPI(request.POST.get('list_lang'))  # Receives all selected langs by user and calls class
    new_repos = git_api_class.cad_or_up_repo()
    all_repos = git_api_class.get_all_repo()
    return JsonResponse({'repositories': all_repos, 'new_found': new_repos})


def list_languages(request):
    """
    This function returns a list with all allowed languages
    """
    return JsonResponse({'lang': GitAPI([]).allowed_lang})
