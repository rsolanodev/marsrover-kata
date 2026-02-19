---
name: pr
description: Create pull requests interactively with proper title, description, and branch selection
license: MIT
compatibility: opencode
metadata:
  workflow: git
  audience: developers
---

## What I do

- Analyze current git status and branch information
- Help craft clear, descriptive PR titles and descriptions
- Identify source and target branches automatically when possible
- Support GitHub, GitLab, Bitbucket, and Azure DevOps
- Create the pull request using the appropriate git provider
- Confirm PR creation and provide the PR URL

## When to use me

Use this skill when you want to create a pull request. I'll guide you through the process by:

1. Checking your current branch and recent commits
2. Suggesting a PR title based on commit messages or branch name
3. Helping you write a clear description
4. Confirming the target branch (usually main/master/develop)
5. Creating the PR on your git provider

## How I work

I will:
- Use `mcp_gitkraken_git_status` to check your current branch and changes
- Use `mcp_gitkraken_git_log_or_diff` to review recent commits for context
- Ask you for any missing information (title, description, target branch)
- Use `mcp_gitkraken_pull_request_create` to create the PR
- Confirm successful creation with the PR link

## Best practices I follow

- Clear, descriptive PR titles that summarize the changes
- Structured descriptions explaining what, why, and how
- Verification that all changes are committed before creating the PR
- Confirmation of the correct target branch
- Option to create draft PRs for work-in-progress

## What I need from you

Just ask me to create a PR! You can:
- Simply say "create a pr" or use `/pr`
- Provide specific details: "create a pr to merge feature-x into develop"
- Let me guide you through the process interactively

I'll handle the rest, asking only for information I can't determine automatically.
