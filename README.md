# College Management System

## 📌 Project Overview
This is a **Django-based College Management System** that provides role-based access for **Admins, Teachers, Students, Library Staff, and Accountants**. Each user has a separate dashboard based on their role.

## 🚀 Features
- **User Authentication & Role-Based Access**
- **Admin Panel:** Manage users, courses, and reports
- **Teacher Dashboard:** Upload assignments, mark attendance, and manage courses
- **Student Dashboard:** View courses, submit assignments, and track attendance
- **Library Management:** Book issuance, returns, and catalog management
- **Accounting System:** Fee management, salary records, and financial reports
- **Responsive HTML Frontend**

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** PostgreSQL / SQLite
- **Version Control:** Git & GitHub

## 📂 Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_ORG/YOUR_REPO.git
   cd YOUR_REPO
   ```
2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```
5. **Run the server**
   ```bash
   python manage.py runserver
   ```

## 👥 User Roles & Access
| Role         | Features |
|-------------|----------|
| **Admin** | Manage users, courses, financial reports |
| **Teacher** | Upload assignments, mark attendance |
| **Student** | View courses, submit assignments |
| **Library Staff** | Manage books, issue & return books |
| **Accountant** | Manage fees, salaries, financial reports |

## 🌿 Git Branching Strategy
- **`main`** → Production branch (stable releases)
- **`develop`** → Default branch for development
- **Feature branches** should be created for new tasks and merged into `develop` via pull requests.

## 🏗️ Contributing
1. **Fork the repository** & clone it locally.
2. **Create a feature branch** (`feature/branch-name`).
3. **Commit your changes** & push the branch.
4. **Submit a pull request** to the `develop` branch.

## 📄 License
This project is **open-source** and available under the [MIT License](LICENSE).

---
🚀 **Happy Coding!** 🚀

