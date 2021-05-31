# Imports necessary tables and Github API class
from .models import TbLanguages, TbGitRepository
from github import Github
# PyGitHub documentation: https://pygithub.readthedocs.io/en/latest/index.html


class GitAPI:

    def __init__(self, lang_list):
        """
        Initializes the class with local (self) variables
        Input:
            lang_list: list
                languages list input by user
        Outputs: class
            (Initialization)
        """
        self.git_api = Github()  # Object with Github API
        self.tb_repo = TbGitRepository  # TbGitRepository object
        self.tb_lang = TbLanguages  # TbLanguages object
        # Creates a list only with registered (allowed) languages
        self.allowed_lang = [lang[1] for lang in self.tb_lang.objects.all().values_list()]  # All allowed languages
        self.languages = [lang for lang in lang_list if lang in self.allowed_lang]  # Languages chosen by user

    def cad_or_up_repo(self):
        """
        This method finds five repositories (top three by language)
        """
        search_repos = list()  # Creates a list to store five objects from Github API
        for lang in self.languages:  # For each language in allowed languages list

            # Searches by repositories and sorts by number of stars to get highlights ones
            repositories = self.git_api.search_repositories(lang, sort='stars')
            index = 0  # Resets or initilizes the number of new repositories found by API
            while index < 3:  # While number of new repositories found is minor than 3
                for repository in repositories:  # For each found repository

                    # Creates a dictionary for repository main atributes except name
                    dict_repo = {'id_fk_lang': self.tb_lang.objects.filter(language=lang),
                                 'repo_url': repository.url,
                                 'repo_stars': repository.stargazers_count,
                                 'repo_commits': repository.get_commits().totalCount,
                                 'repo_watchers': repository.watchers_count,
                                 'repo_branches': repository.get_branches().totalCount,
                                 'repo_forks': repository.get_forks().totalCount,
                                 'repo_issues': repository.open_issues_count,
                                 'repo_up_at': repository.updated_at}

                    # Verifies if current repository is registered on database and update or create
                    obj, created = self.tb_repo.objects.update_or_create(repo_name=repository.name, defaults=dict_repo)

                    if created:  # If it was created, otherwise it updates existent register
                        search_repos.append(dict_repo)  # appends dict_repo to search list
                        index += 1  # adds one repository found by index status (3 by language)

        # Returns all five new registered repositories main data
        return search_repos

    def get_all_repo(self):
        """
        A method that returns all registered repositories
        Input: None
        Output: List
            list containing all repositories and their metadata
        """
        return [repo for repo in self.tb_repo.objects.all().values_list()]
