# StaffHub – Employee Management System

A web-based Employee Management System developed using Python and Django to simplify employee information management and HR operations. StaffHub provides an organized platform for HR managers to manage employee records, monitor workforce information, and maintain important company updates.

## 🚀 Live Demo

**Live Application:** https://staffhub-vgsz.onrender.com/

**Source Code:** https://github.com/tejaM-SENG/EmpManagement

## 📌 Project Overview

StaffHub is a Django-based Employee Management System designed to streamline employee administration through a centralized web application.

The application provides dedicated interfaces for HR managers and employees, allowing employee information to be maintained efficiently through a user-friendly dashboard.

## ✨ Key Features

- **HR Manager Dashboard:** Centralized dashboard for managing employee information.
- **Employee Management:** Add, view, update, and manage employee records.
- **Employee Profiles:** Maintain employee details, contact information, and profile photographs.
- **Resume Management:** Upload and view employee resumes in PDF format.
- **Employment Information:** Manage designation, department, employment type, annual CTC, and joining date.
- **Skills Management:** Store and display employee skills.
- **Company News:** Publish and manage organizational announcements.
- **Holiday Management:** Maintain company holiday information.
- **Job Openings:** Display available job opportunities.
- **Authentication:** Secure login and logout functionality.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Django |
| Frontend | HTML, CSS, JavaScript |
| UI Framework | Bootstrap 5 |
| Database | SQLite / MySQL |
| Icons | Bootstrap Icons |
| Deployment | Render |
| Version Control | Git & GitHub |

## 🔐 Demo Login Credentials

Use the following accounts to explore the live application.

| Username | Password |
|---|---|
| demo@hr | demo@1234 |


## 📂 Project Structure

```text
EmpManagement/
│
├── empmngt/
│   ├── migrations/
│   ├── __init__.py
│   ├── apps.py
│   ├── tests.py
│   ├── middle.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── admin.py
│
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
│   ├── employee_photos
│   └── employee_resumes
│
├── static/
│   ├── css
│   └── images
│
├── templates/
│   ├── empmngt
│   └── registration
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

*Note: The structure above is illustrative. Adjust it to match your actual repository.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/tejaM-SENG/EmpManagement.git
```

### 2. Navigate to the Project Directory

```bash
cd EmpManagement
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

## 🖥️ Application Screenshots

Screenshots demonstrating the application's interface and functionality will be added here.

| Interface | Screenshots |
|---|---|
| Dashboard | <img width="2844" height="1270" alt="image" src="https://github.com/user-attachments/assets/c08b06c8-87c9-4dc5-b2ec-13195c87478f" /><img width="2842" height="1284" alt="image" src="https://github.com/user-attachments/assets/e0cfc42f-104c-444b-b61b-7d35246876f6" /><img width="2838" height="1268" alt="image" src="https://github.com/user-attachments/assets/6874b65e-e332-44c5-8624-95ef41486229" />  |
| Employee Management |  <img width="2816" height="1232" alt="image" src="https://github.com/user-attachments/assets/889d4e5e-f9db-4a57-9e88-24562f3fb46a" /><img width="2850" height="1096" alt="image" src="https://github.com/user-attachments/assets/b60cbd33-3ca0-456a-ad41-b282a95cd794" /><img width="2780" height="1090" alt="image" src="https://github.com/user-attachments/assets/9aae5017-ac69-49a5-b522-29af7ac686fc" /><img width="2844" height="1084" alt="image" src="https://github.com/user-attachments/assets/37c5b676-e1e1-4939-bae8-d435cb2bc455" />  |
| Employee Profile | <img width="2834" height="1272" alt="image" src="https://github.com/user-attachments/assets/8df3a46f-8414-464d-ae2e-00c508f26e18" /><img width="2794" height="1274" alt="image" src="https://github.com/user-attachments/assets/fb808785-2d9c-4e8b-836e-a4507d34d6c0" /><img width="2800" height="1282" alt="image" src="https://github.com/user-attachments/assets/e69d5028-0939-4a05-9083-31372e45cc79" />  |
| Company News | <img width="2844" height="1282" alt="image" src="https://github.com/user-attachments/assets/fb34a3d6-374a-4933-bbff-ca42d14939d7" /> |

## ☁️ Deployment

The application is deployed using **Render**.

Deployment workflow:

1. Push the project source code to GitHub.
2. Connect the GitHub repository to Render.
3. Configure the Python environment and dependencies.
4. Set the required environment variables.
5. Configure database and static/media file storage.
6. Deploy the application.

**Live URL:** https://staffhub-vgsz.onrender.com/

## 🎯 Project Objectives

- Simplify employee record management.
- Centralize HR-related information.
- Provide an organized employee administration interface.
- Implement backend functionality using Django.
- Develop a responsive web application with Bootstrap.
- Gain practical experience in full-stack web development and cloud deployment.

## 👨‍💻 Developer

**Teja Muddangula**

Python Full-Stack Developer

- GitHub: https://github.com/tejaM-SENG
- LinkedIn: https://linkedin.com/in/teja-muddangula-38a92a218

---

*Developed as a Python Full-Stack Web Development project.*
