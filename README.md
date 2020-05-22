# RFranco Technologies git hooks

This repo contains git hooks that can be installed with [pre-commit](https://pre-commit.com/)

List of available hooks:

- commit-msg hook: ensure jira issue is present in commit message.

## Usage: Ensure jira issue is present in commit message Hook

There is two options of usage:

**1st option: Use in single repo**

Create a file .commit-msg-config.yaml in the repo you want to use:

```
repos:
-   repo: git@bitbucket.org:mediatechsolutions/rf-git-hooks.git
    rev: v1.0.0
    hooks:
    -   id: ensure-jira-issue
        args:
          - .git/COMMIT_EDITMSG
          - DVOP ## <JIRA_PROJECT_KEY>: In the example DVOP. You can use more than one issuekey (ISSUEKEY1|ISSUEKEY2)
```
Execute next command

```
pre-commit install -c .commit-msg-config.yaml -t commit-msg
```


**2nd option: Configure hook as a template for all git repos**

Create a file .commit-msg-config.yaml wherever you want:

```
repos:
-   repo: git@bitbucket.org:mediatechsolutions/rf-git-hooks.git
    rev: v1.0.0
    hooks:
    -   id: ensure-jira-issue
        args:
          - .git/COMMIT_EDITMSG
          - DVOP ##<JIRA_PROJECT_KEY>: In the example DVOP. You can use more than one issuekey (ISSUEKEY1|ISSUEKEY2)
```
Use init-templatedir config of Git:

```
git config --global init.templateDir ~/.git-template

pre-commit init-templatedir ~/.git-template -c .commit-msg-config.yaml -t commit-msg
```
Now when you create or clone a new git repo, it will have configured this commit-msg hook.

On previously created repos you have to execute *git init* to configure it.
