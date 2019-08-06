# CrawlGitlab

Clone all repositories from a GitLab server

## Expectations

This script expects the following :

- GitLab is accessed using SSH key
- Python 3.x installed
- Working Git installation in /usr/bin/git

You will also need a a GitLab personal access token to authenticate against the GitLab API.

## Configuration

Export parameters as environment variables:

- GitLab API URL
- GitLab personal access token

```bash
export GITLAB_URL=https://gitlabserver/api/v4
export GITLAB_TOKEN=...
```

## Usage

```bash
python crawl.py
```

Cloned repositories will be outputted in an `export` subdirectory.
