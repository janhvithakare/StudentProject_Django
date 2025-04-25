# StudentProject Django + Docker CI/CD

## Overview
A multi-app Django project (app1 & app2) containerized with Docker and deployed via a Jenkins pipeline.

## Apps & URLs
- `/` → Homepage (app1)  
- `/sample1/` → App1 sample page  
- `/app2/sample2/` → App2 sample page  

## Local Run (without Docker)
```bash
python manage.py runserver
