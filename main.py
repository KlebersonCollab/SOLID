from github.client import GithubClient

from repo.parser import RepoParser
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator
from repo.reports_generator import ReportsGenerator
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator

from models.member import Member
from models.owner import Owner

if __name__ == '__main__':
    username = 'KlebersonCollab'
    response = GithubClient.get_repos_by_user(username)
    
    if response['status_code'] == 200:
        repos = RepoParser.parse(response['body'])
        markdown_reports = ReportsGenerator.build(MarkdownGenerator, repos)
        html_reports = ReportsGenerator.build(HTMLGenerator, repos)
        print(html_reports)
        print(markdown_reports)
    else:
        print(response['body'])
        
    member = Member('KlebersonCollab', 'klebersondsromero@gmail.com')
    owner = Owner('AmandaCollab', 'Amanda@gmail.com')
    
print(member.member())
print(owner.member())