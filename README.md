Flask-SQLAlchemy Project

This is a robust web application built with the Flask framework and SQLAlchemy ORM.
The project demonstrates database management, migrations using Flask-Migrate, and structured backend development.


Getting Started :
Prerequisites-
Ensure you have Python 3.8+ installed on your system.
Installation: Clone the repository: git clone https://github.com/LilianMuthoniMaina/Flask-SQLAlchemy-project.git on your terminal.
cd Flask-SQLAlchemy-project
Create a virtual environment: python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the dependencies: 
pip install -r requirements.txt

Tech Stack & Dependencies:
This project leverages the following libraries to ensure stability and scalability:
PackageVersionDescriptionFlask3.1.3
The core web framework.SQLAlchemy2.0.49
The Python SQL toolkit and Object Relational Mapper.
Flask-SQLAlchemy3.1.1Flask extension that simplifies SQLAlchemy integration.
Flask-Migrate4.1.0Handles SQLAlchemy database migrations via Alembic.
Alembic1.18.4Lightweight database migration tool.Jinja23.1.6
The template engine for rendering HTML.Werkzeug3.1.8
WSGI web application library used by Flask.
Other notable dependencies: click, blinker, itsdangerous, Mako, MarkupSafe, and typing_extensions.

Database Management:
This project uses Flask-Migrate to track changes to your database models.
Initialize the migration folder:
flask db init
Generate a migration script: flask db migrate -m "Description of changes made"
Apply changes to the database: flask db upgrade


Project StructurePlaintext.
├── migrations/          # Database migration files
├── app/                 # Main application logic
│   ├── models.py        # Database schemas
│   ├── routes.py        # API endpoints/View functions
│   └── __init__.py      # App factory
├── requirements.txt     # List of project dependencies
├── config.py            # Environment configurations
└── run.py               # Entry point to start the server
Author:
Lilian Muthoni Maina    GitHub: @LilianMuthoniMaina
