import os
from urllib.parse import urlencode
from subprocess import call
import requests

GIT_BIN = '/usr/bin/git'
WORK_DIR = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'export'


def validate_token():
    if not os.environ['GITLAB_TOKEN']:
        print('missing gitlab token : did you export GITLAB_TOKEN variable?')
        exit(1)

    if not os.environ['GITLAB_URL']:
        print('missing gitlab url : did you export GITLAB_URL variable?')
        exit(1)


def build_gitlab_url(resource, params):
    query_string = urlencode(params)
    return "{}/{}?{}".format(os.environ['GITLAB_URL'], resource, query_string)


def get(resource, params):
    url = build_gitlab_url(resource, params)
    resp = requests.get(
        url, headers={'Private-Token': os.environ['GITLAB_TOKEN']})
    if resp.status_code != 200:
        print('Error when doing request', url)
        print(resp.text)

    return resp


def main():
    validate_token()
    resp = get('projects', {'simple': 'true', 'per_page': '500'})
    for project in resp.json():
        output_dir = WORK_DIR + os.sep + project['path_with_namespace']
        repo_url = project['ssh_url_to_repo']

        print('cloning ' + repo_url)
        code = call([GIT_BIN, 'clone', repo_url, output_dir])
        if code != 0:
            print('Git clone failed for', repo_url)
            continue


if __name__ == "__main__":
    main()
