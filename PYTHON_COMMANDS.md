# Gmail AI Assistant - Development Commands

This document contains all commonly used terminal commands for developing and running the Gmail AI Assistant.

---

# 1. Create Virtual Environment

## Python 3.12

```bash
python3.12 -m venv venv
```

---

# 2. Activate Virtual Environment

macOS / Linux

```bash
source venv/bin/activate
```

Deactivate

```bash
deactivate
```

---

# 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# 4. Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

# 5. Install Google OAuth Libraries

```bash
pip install google-auth google-auth-oauthlib google-api-python-client
```

---

# 6. Install Additional Package

Example:

```bash
pip install package_name
```

Example

```bash
pip install beautifulsoup4
```

---

# 7. Save Dependencies

```bash
pip freeze > requirements.txt
```

---

# 8. Show Installed Packages

```bash
pip list
```

---

# 9. Package Information

```bash
pip show fastapi
```

Example

```bash
pip show google-auth-oauthlib
```

---

# 10. Uninstall Package

```bash
pip uninstall psycopg2-binary
```

---

# 11. Run FastAPI

```bash
uvicorn app.main:app --reload
```

Run on custom port

```bash
uvicorn app.main:app --reload --port 8080
```

---

# 12. Stop FastAPI

```text
CTRL + C
```

---

# 13. Verify Python

```bash
python --version
```

---

# 14. Verify Pip

```bash
pip --version
```

---

# 15. Current Python Executable

```bash
which python
```

---

# 16. Current Pip

```bash
which pip
```

---

# 17. Verify Virtual Environment

```bash
echo $VIRTUAL_ENV
```

---

# 18. Run Configuration Test

```bash
python test_config.py
```

---

# 19. Project Tree

Install tree

```bash
brew install tree
```

Show project

```bash
tree
```

Only app folder

```bash
tree app
```

---

# 20. Find Python Files

```bash
find app -name "*.py"
```

---

# 21. Find **init**.py Files

```bash
find app -name "__init__.py"
```

---

# 22. Verify Credentials Folder

```bash
ls credentials
```

---

# 23. Verify Gmail Folder

```bash
ls app/gmail
```

---

# 24. Verify API Routes

```bash
ls app/api/routes
```

---

# 25. Check Running Uvicorn Process

```bash
ps aux | grep uvicorn
```

---

# 26. Kill Uvicorn

```bash
kill -9 <PID>
```

Example

```bash
kill -9 98765
```

---

# 27. Clean Python Cache

macOS/Linux

```bash
find . -name "__pycache__" -exec rm -rf {} +
```

Delete .pyc

```bash
find . -name "*.pyc" -delete
```

---

# 28. Run Swagger

```
http://localhost:8000/docs
```

---

# 29. Open Health API

```
http://localhost:8000/api/v1/health
```

---

# 30. Login

```
http://localhost:8000/api/v1/auth/login
```

---

# 31. Gmail APIs

Latest Emails

```
GET /api/v1/gmail/messages
```

Single Email

```
GET /api/v1/gmail/message/{id}
```

Search

```
GET /api/v1/gmail/search?q=amazon
```

Labels

```
GET /api/v1/gmail/labels
```

---

# 32. Git Commands

Status

```bash
git status
```

Stage

```bash
git add .
```

Commit

```bash
git commit -m "message"
```

Push

```bash
git push
```

Pull

```bash
git pull
```

---

# 33. Recommended Development Workflow

Activate environment

```bash
source venv/bin/activate
```

Run project

```bash
uvicorn app.main:app --reload
```

Open Swagger

```
http://localhost:8000/docs
```

Test APIs

Make changes

Save

Hot Reload

Commit changes

---

# 34. Project URLs

Swagger

```
http://localhost:8000/docs
```

Health

```
http://localhost:8000/api/v1/health
```

Google Login

```
http://localhost:8000/api/v1/auth/login
```

Google Callback

```
http://localhost:8000/api/v1/auth/callback
```
