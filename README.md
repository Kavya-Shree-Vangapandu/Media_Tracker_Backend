**📄 [Media Tracker - Project Documentation]{.underline}**

**[Introduction:]{.underline}**\
\
Welcome to Media Tracker, a simple yet efficient application that helps
users track videos by adding them to History or Bookmarks. This project
consists of:

-   Django (Backend) -- Handles API requests and stores data.

-   Angular (Frontend) -- Provides a user-friendly interface.

This guide will walk you through how to set up and run the project on
your local machine.

**1. Getting Started**

Before you begin, ensure you have the following installed:

🔹 Prerequisites:

-   Python 3.10+ (for the backend)

-   Node.js 18+ & npm (for the frontend)

-   A code editor (VS Code recommended)

**2. Setting Up the Backend (Django API)**

The backend is built with Django REST Framework and serves API endpoints
for managing history and bookmarks.

🔹 Step 1: Navigate to Backend Directory

Open a terminal and run: cd media_tracker

🔹 Step 2: Create a Virtual Environment:

python -m venv venv

source venv/bin/activate \# On macOS/Linux

venv\\Scripts\\activate \# On Windows

🔹 Step 3: Install Dependencies: pip install -r requirements.txt

🔹 Step 4: Apply Database Migrations:

python manage.py makemigrations media_app

python manage.py migrate

🔹 Step 5: Run the Backend Server:\
python manage.py runserver

Your Django API is now running at: <http://127.0.0.1:8000/api/>

To test both History and Bookmarks:

<http://127.0.0.1:8000/api/history/>

<http://127.0.0.1:8000/api/bookmarks/>

**3. Setting Up the Frontend (Angular)**

The frontend is built using Angular 19 and provides a clean UI to
interact with the API.

🔹 Step 1: Navigate to Frontend Directory

Open a new terminal and run: cd media_tracker-frontend

🔹 Step 2: Install Dependencies: npm install\
🔹 Step 3: Start the Angular App: ng serve \--port 4200

Your Angular application is now running at: <http://127.0.0.1:4200/> or
<http://localhost:4200/>

**4. Features**

-   List videos in History & Bookmarks

-   Add new videos to History & Bookmarks

-   Delete entries from History & Bookmarks

-   Sort videos by Title, URL, or Date

**5. API Endpoints**

Your backend provides the following API routes:\
🔹 History API

  -------------------------------------------------------------------------
  **Method**               **Endpoint**             **Description**
  ------------------------ ------------------------ -----------------------
  **GET**                  **/api/history/**        **Get all history
                                                    items**

  **POST**                 **/api/history/**        **Add a video to
                                                    history**

  **DELETE**               **/api/history/{id}/**   **Delete a history
                                                    entry**
  -------------------------------------------------------------------------

🔹 Bookmarks API

  ---------------------------------------------------------------------------
  **Method**               **Endpoint**               **Description**
  ------------------------ -------------------------- -----------------------
  **GET**                  **/api/bookmarks/**        **Get all bookmarked
                                                      videos**

  **POST**                 **/api/bookmarks/**        **Add a video to
                                                      bookmarks**

  **DELETE**               **/api/bookmarks/{id}/**   **Delete a bookmark
                                                      entry**
  ---------------------------------------------------------------------------

🔹 Sorting Support\
To sort history or bookmarks, append a query parameter:

-   ?sort=title → Sort by title (A-Z)

-   ?sort=url → Sort by URL (A-Z)

-   ?sort=oldest → Sort by oldest entry

-   ?sort=newest (default) → Sort by newest first

**For Example:** GET http://127.0.0.1:8000/api/history/?sort=title

**6. Sorting in the Frontend**

Sorting is available in the UI, and users can click buttons to sort by
Title, URL, or Date.

🔹 To Change Sorting, click:

-   Title → Alphabetically

-   URL → Alphabetically

-   Date → Newest or Oldest

**7. Project Structure**

media-tracker/

│── media_tracker/ (Django backend)

│ ├── media_app/ (API app)

│ ├── manage.py

│ ├── db.sqlite3

│ ├── requirements.txt

│── media_tracker-frontend/ (Angular frontend)

│ ├── src/

│ ├── angular. json

│ ├── package. json

| ├── tsconfig. json

**8. Technologies Used**

-   Backend: Django REST Framework

-   Frontend: Angular 19

-   Database: SQLite (default)

-   API Communication: RESTful API with CORS enabled

**9. Future Improvements**

-   Add User Authentication (Login/Signup)

-   Implement Docker for containerization (if needed in the future)

-   Migrate to PostgreSQL for production databases

**10. Author & Contact**

Name: Kavya Shree Vangapandu\
Email ID: kavyavangapandu2212@gmail.com\
Contact.no: +49 15560048756

**\
**

**\
**
