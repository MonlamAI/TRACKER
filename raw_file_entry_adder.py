from pathlib import Path

PARENT_PATH = Path('./mt/mt-extracted-text-pairs')
def add_raw_file_entry(list_of_repos):
    
    for repo_name in list_of_repos:
        (PARENT_PATH / repo_name).write_text('')

if __name__ == "__main__":
    list_of_repos = Path('./repo_list.txt').read_text().split('\n')
    add_raw_file_entry(list_of_repos)