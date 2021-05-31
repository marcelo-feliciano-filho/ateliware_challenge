# Imports necessary tables and Github API class
from .models import TbLanguages, TbGitRepository
from github import Github
# PyGitHub documentation: https://pygithub.readthedocs.io/en/latest/index.html


class GitAPI:

    def __init__(self):
        """
        Initializes the class with local (self) variables
        """
        self.git_api = Github()
        self.tb_repo = TbGitRepository
        self.tb_lang = TbLanguages

    def cad_or_up_repo(self):
        """
        This method finds five repositories (one by language)
        """
        languages = self.tb_lang.objects.all()
        search_five = list()  # Creates a list to store five objects from Github API
        for lang in languages:

            # Searches by repositories and sorts by number of stars to get highlights ones
            repositories = self.git_api.search_repositories(lang.language, sort='stars')
            for repository in repositories:  # For each found repository

                # Creates a dictionary for repository main atributes except name
                dict_repo = {'id_fk_lang': lang.id,
                             'repo_url': repository.url,
                             'repo_stars': repository.stargazers_count,
                             'repo_commits': repository.get_commits().totalCount,
                             'repo_whatchers': repository.watchers_count,
                             'repo_branches': repository.get_branches().totalCount,
                             'repo_forks': repository.get_forks().totalCount,
                             'repo_issues': repository.open_issues_count,
                             'repo_up_at': repository.updated_at}

                # Verifies if current repository is registered on database and update or create
                obj, created = self.tb_repo.objects.update_or_create(repo_name=repository.name, defaults=dict_repo)

                if created:  # If it was created, otherwise it updates existent register
                    search_five.append(dict_repo)  # appends dict_repo to search list
                    break  # Breaks repository for loop and goes to next language

        # Returns all five new registered repositories main data
        return search_five

    def get_all_repo(self):
        """
        A method that returns all registered repositories
        Input: None
        Output: List
        """
        all_repositories = self.tb_repo.objects.all()

        return all_repositories
