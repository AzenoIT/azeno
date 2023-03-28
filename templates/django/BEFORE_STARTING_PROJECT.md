# Before starting a project

> **DO NOT COPY THIS FILE INTO YOUR PROJECT**

## Set project name in following files

> ### backend/pyproject.toml

Line 2 `name = "{{project_name}}"` should be changed to:

```python
# e.g.

name="quiz" or name="flashcards"
```

Line 4 `description = "virtual environment for {{project_name}} application"` should be changed to:

```python
# e.g.

description = "virtual environment for quiz application" or
description = "virtual environment for flashcards application"
```

> ### backend/docs/conf.py

Line 25 `project = "{{project_name}}"` should be changed to:

```python
# e.q.

project = "quiz" or project = "flashcards"
```
