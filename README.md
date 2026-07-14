This is a basic Erp software for a small Pvc company production management using DJANGORESTFRAMEWORK and REACT.JS.
where i implemented Userbased login system for the Admin,HR,Manager,employees by providing different user interface to manage different functionalities 
# PVC Factory Management System

A comprehensive **Factory Management System** built using **Django REST Framework** and **React** to streamline the daily operations of a PVC manufacturing company. The application centralizes employee management, payroll, quality control, and administrative tasks through role-based access.

## 📌 Overview

The PVC Factory Management System is designed to digitize and simplify factory operations by providing a secure platform for managing employees, departments, attendance, payroll, quality control, and production-related activities.

The system supports multiple user roles, each with specific permissions and responsibilities.

---

## 🚀 Features

### 👨‍💼 Admin
- Manage all users and roles
- Create and manage departments
- Assign employees to managers
- Monitor overall factory activities
- View reports and analytics
- Manage system settings

### 👔 HR
- Add, update, and remove employee records
- Manage attendance
- Generate payroll
- Approve leave requests
- Maintain employee information
- Track employee status

### ✅ Quality Control (QC)
- Record product quality inspections
- Track defective products
- Generate quality reports
- Monitor production quality
- Update inspection status

### 📋 Manager
- Supervise assigned workers
- Assign daily tasks
- Monitor worker performance
- View attendance of team members
- Track production progress

### 👷 Worker
- Secure login
- View personal profile
- Check attendance
- View salary and payroll details
- Download payslips
- View assigned tasks
- Receive notifications

---

## 🛠 Tech Stack

### Backend
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication / Session Authentication

### Frontend
- React
- React Router
- Axios
- Bootstrap / Tailwind CSS

### Database
- PostgreSQL

---

## 🔐 User Roles

| Role | Permissions |
|------|-------------|
| Admin | Full system access |
| HR | Employee management, attendance, payroll |
| QC | Quality inspection and reporting |
| Manager | Team management and task assignment |
| Worker | View profile, attendance, payroll, assigned tasks |

---

## 📂 Project Structure

```
PVC-Factory/
│
├── backend/
│   ├── accounts/
│   ├── employees/
│   ├── payroll/
│   ├── attendance/
│   ├── qc/
│   ├── manager/
│   ├── api/
│   └── manage.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   └── App.jsx
│
└── README.md
```

---

## 📦 Main Modules

- Authentication
- Employee Management
- Attendance Management
- Payroll Management
- Quality Control
- Task Management
- Department Management
- Reports & Analytics
- Role-Based Access Control (RBAC)

---

## 💼 Payroll Module

Workers can:

- View monthly salary
- View overtime earnings
- Download payslips
- Check deductions
- View salary history

HR can:

- Generate payroll
- Update salary records
- Manage overtime
- Process monthly salaries

---

## 📊 Dashboard

Different dashboards are available for each role.

- Admin Dashboard
- HR Dashboard
- QC Dashboard
- Manager Dashboard
- Worker Dashboard

Each dashboard displays only the information relevant to that user.

---

## 🔒 Security

- Role-Based Authorization
- Secure Authentication
- Password Hashing
- Protected API Endpoints
- Input Validation
- CSRF Protection (Session Authentication)

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/vishnurajc1542/pvc-factory-management.git
```

### Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 📈 Future Improvements

- Inventory Management
- Machine Maintenance Module
- Production Planning
- Barcode/QR Code Integration
- Email Notifications
- SMS Notifications
- Mobile Application
- Leave Management
- Performance Analytics
- Shift Scheduling

---

						Modules


	Accounts

		1. Useraccounts
		2.UserDetails


	Quality Checking
		1.inspected
		2.rejected details
		3.rework status



	Pay Roll
		1.salary Details
			user_id=onetoone key

		2.OT Details
		3.monthly salary

	Production
		1.Daily production
			/ profile_id
			/shift-
			/workers
			/quantity
			/shift start
			/shift end
		2.Items Details
			/profile name
			 /id
			/batch code
			/die number
3.

## 🎯 Project Goals

- Digitize factory management
- Reduce manual paperwork
- Improve employee management
- Simplify payroll processing
- Enhance production monitoring
- Provide transparency for workers
- Improve communication between departments

---

## 👨‍💻 Developed By

**Vishnu Raj C**

Python Full Stack Developer

---

## 📄 License

This project is developed for educational and portfolio purposes.