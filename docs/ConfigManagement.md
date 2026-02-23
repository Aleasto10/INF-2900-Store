# Configuration Management

This document describes the methodology around the configuration management we will follow.

## Branching Methodology

The branching methodology for this project will be as follows:

- **main**: This branch will be used for stable and feature ready versions of the project.

- **develop**: This branch will be used to develop the project, all finished tasks will be merged into develop after they have been reviewed by another team member.

### Support branches

Each task will have its own branch that will be named after the task it is associated with.

After the task is finished a pull request to develop is created and, after approval, merged into develop.

### Bugfixes

If unexpected bugs get found after merging then a bugfix task will be created and a branch will be made.

If the bug is on develop then the branch will be named **bugfix/descriptive-name-of-the-bug** after the bug is fixed a pull request is created and merged after approval.

If the bug is on main the branch will be named **hotfix/descriptive-name-of-the-bug** after the bug is fixed a pull request is created to main and merged after approval.
