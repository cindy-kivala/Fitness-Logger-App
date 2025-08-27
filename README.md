# Fitness Logger CLI

- A command-line interface (CLI) application for managing users, exercises, and workout sessions. 
- Built with Python and SQLite for data persistence.


## Features

- **User Management**
  - Add, view, update, and delete users.

- **Exercise Management**
  - Add, view, update, and delete exercises.

- **Workout Session Management**
  - Add, view, update, and delete workout sessions.

- **Session Exercise Management**
  - Add, view, update, and delete exercises within a workout session.

## Project Structure

Fitness-Logger-App/
├── lib/
│   ├── __init__.py
│   ├── cli.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── database.py
│   └── helpers.py
├── Pipfile
|__ migrations
|__ venv
|__ app.py
|__ fitness.db
|__ alembic.ini
├── Pipfile.lock
└── README.md

## CLI Guide
=== FITNESS LOGGER ===
1. Add User
2. View Users
3. Update User
4. Delete User
5. Add Exercise
6. View Exercises
7. Update Exercise
8. Delete Exercise
9. Add Workout Session
10. View Workout Sessions
11. Update Workout
12. Delete Workout
13. Add Exercise to Session
14. View Session Exercise
15. Update Session Exercise
16. Delete Session Exercise
17. Exit

## Overview

- FIT4U is a Python CLI app that lets you:

1. Create and manage Users.

2. Define reusable Exercises.

3. Log Workout Sessions for a user.

4. Attach one or more Exercises to a workout session with sets, reps, and weight via an association table.

5. The app uses SQLAlchemy ORM for data persistence and relationships, and exposes a simple interactive menu to perform CRUD operations.

## Key Features

1. CRUD for Users, Exercises, Workout Sessions, and Session‑Exercises.

2. One‑to‑many: User → WorkoutSession.

3. Many‑to‑many (with extra fields): WorkoutSession ↔ Exercise via WorkoutSessionExercise, including sets, reps, and weight.

4. Persistent storage via SQLite (default) using SQLAlchemy.

## Architecture

- Entry point: app.py – prints the menu and routes choices to handlers.

- ORM models: lib/db/models.py – defines User, Exercise, WorkoutSession, WorkoutSessionExercise with relationships and convenience class methods.

- CLI handlers: lib/helpers.py – input handling and calls to SQLAlchemy sessions/queries.

- DB utilities: lib/db/__init__.py, lib/db/sessions.py, lib/db/setup.py (provide engine, SessionLocal, connection helpers). These are referenced by the codebase.

## Data Model

# Entities and Relationships

- User (1) ───< WorkoutSession (N)

- WorkoutSession (1) ───< WorkoutSessionExercise (N) >─── (1) Exercise

## Tables

# users

- id INTEGER PK

- name TEXT NOT NULL

- age INTEGER

- weight REAL

# exercises

- id INTEGER PK

- name TEXT NOT NULL

- muscle_group TEXT

- equipment TEXT

- description TEXT

# workout_sessions

- id INTEGER PK

- user_id INTEGER FK → users.id NOT NULL

- date DATETIME (defaults to current timestamp)

- duration INTEGER (minutes)

-activity TEXT

- calories INTEGER

# workout_session_exercises (association table with payload)

- id INTEGER PK

- session_id INTEGER FK → workout_sessions.id NOT NULL

- exercise_id INTEGER FK → exercises.id NOT NULL

- sets INTEGER

- reps INTEGER

- weight REAL

# SQLAlchemy Relationships

- User.workout_sessions ↔ WorkoutSession.user (one‑to‑many)

- WorkoutSession.exercises ↔ WorkoutSessionExercise.workout_session

- Exercise.workout_sessions ↔ WorkoutSessionExercise.exercise

## ORM Requirements

- Database is created and modified via SQLAlchemy ORM (Base.metadata.create_all(engine) and class methods).

- Data model includes 4 model classes: User, Exercise, WorkoutSession, WorkoutSessionExercise.

- One‑to‑many relationship: User → WorkoutSession.

- Property/relationship methods add constraints (e.g., nullable=False, cascade behavior, and typed columns).

- Each model includes ORM helpers: create, all, find_by_id (for WorkoutSession), and update/delete utilities are provided via handlers and class methods.

## CLI Requirements

- Interactive menu presented in app.py with loop until Exit.

- Options exist to create, delete, display all, and update objects for each class; related objects are viewed via listings (e.g., view sessions, view session exercises, and add exercises to sessions).

- Handlers check existence before update/delete and print informative messages.

- Code follows OOP/ORM organization with imports scoped to usage.

- Dependencies are confined to SQLAlchemy (and optional Alembic), declared in Pipfile and requirements.

- This README documents the application and usage.

## Troubleshooting

- Module import errors: Verify the project structure and that lib/ is a package (contains __init__.py files). Ensure PYTHONPATH is correct if running from outside the project root.

- SQLite database location: Confirm the database URL in your engine (e.g., sqlite:///fitness.db) and that the process has write permissions.

- Migrations: If using Alembic, set the correct sqlalchemy.url and metadata target.

- Date parsing: Use YYYY-MM-DD. Invalid formats will raise ValueError.

## Future Enhancements

- Add workout statistics and progress tracking.

- Implement export options (CSV, JSON).

- Include search and filter functionality.

## License 
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)

