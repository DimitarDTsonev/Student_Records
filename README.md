# Student Records

## Live Demo (1‑click)

[![Open the site](https://img.shields.io/badge/Open%20site-Click%20to%20launch-blue)](https://DimitarDTsonev.github.io/Student_Records/)

[Open in GitHub Codespaces](https://codespaces.new/DimitarDTsonev/Student_Records)

## Run locally

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
# по подразбиране ползва SQLite файл students.db
python app.py
# или:
export FLASK_APP=app.py FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=5000
flask run
```

To use MySQL instead of SQLite, set env var `DATABASE_URL`, e.g.:
```
DATABASE_URL=mysql+pymysql://user:pass@host:3306/students
```
