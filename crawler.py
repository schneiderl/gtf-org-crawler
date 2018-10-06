import os
import sys
from os.path import expanduser
from github import Github
from misspellings import misspelling_dict


g = Github(os.environ['GITHUB_OAUTH'])

owner_organization = g.get_user(sys.argv[1])
repos = owner_organization.get_repos()

print("Working :). Wait a few minutes.")

for repo in repos:
    try:
        readme = repo.get_readme().decoded_content
        text = readme.decode()
        #print(data)
        for line in text.split('\n'): 
            words = line.split(" ")
            for word in words: 
                if (word in misspelling_dict):
                    print ("Possible misspeling at " + repo.full_name + '. Word: ' + word + " Stars: " + str(repo.stargazers_count)) 
    except Exception as x:
        pass
    
print("Finished.")