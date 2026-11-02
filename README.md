# Apna Mart - Full-Stack Django E-Commerce Web Application 🛒🥦

A modern, robust, and feature-packed full-stack e-commerce and grocery store application built with **Python**, **Django 5**, **JavaScript**, **jQuery**, **Bootstrap**, and **SQLite**.

Designed specifically for local retail and quick-commerce operations, featuring local currency support (Indian Rupee - ₹), multi-vendor architecture, end-to-end checkout, and interactive customer reviews.

---

## 👨‍💻 Developer & Project Info
- **Project Name:** Apna Mart
- **Developer:** Md Kamar Rza Khan
- **Year:** 2026
- **Store Location:** Law Gate, LPU, Phagwara, Punjab - 144411
- **Support Contact:** +91 98765 43210 | support@apnamart.in
- **Currency:** Indian Rupee (₹)
- **🌐 Live Storefront:** [https://mdkamarrzakhan.pythonanywhere.com](https://mdkamarrzakhan.pythonanywhere.com)
- **🔐 Live Admin Panel:** [https://mdkamarrzakhan.pythonanywhere.com/admin/](https://mdkamarrzakhan.pythonanywhere.com/admin/)

---

## 🚀 Key Features

### 🛒 Customer Experience
- **Product Catalog & Categorization:** Browse fresh groceries, vegetables, fruits, dairy, and meat.
- **Search & Filters:** Real-time search, price filtering, category filtering, and product tags.
- **Shopping Cart & AJAX Counter:** Real-time cart updates without page reload.
- **Checkout & Order Flow:** Streamlined shipping address collection, COD & Online payment options, and instant automated order invoices.
- **Customer Order Tracking:** Dedicated "My Orders" dashboard to monitor delivery status (Processing, Shipped, Delivered).
- **Wishlist:** Save favorite products for later purchase.
- **Product Ratings & Reviews:** 5-star ratings and verified buyer reviews.
- **Blog & Community:** Articles, health tips, and reader comments.

### 🏪 Vendor & Merchant Support
- **Multi-Vendor Architecture:** Dedicated vendor profiles showcasing address, phone, email, and catalog.
- **Direct Contact:** Quick access to call or message vendors directly.

### ⚙️ Admin & Store Management (Jazzmin Panel)
- **Modern Dashboard:** Sleek, responsive admin interface powered by Django Jazzmin.
- **Order Management:** View all placed orders with inline order item details, customer address, and payment status.
- **Product & Inventory Management:** Add/edit products, stock counts, manufacturing dates (mfd), and multiple product images.
- **Review Moderation:** Monitor, edit, or remove customer reviews and spam comments.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.14, Django 5.2
- **Frontend:** HTML5, CSS3, JavaScript (ES6+), jQuery, Bootstrap
- **Database:** SQLite (`db.sqlite3`)
- **Admin UI:** Django Jazzmin
- **Authentication:** Custom User model supporting login via **Email or Username**

---

## 💻 Quick Start & Running Locally

### 1. Navigate to Project Directory
```powershell
cd django-ecommerce-main
```

### 2. Activate Virtual Environment
- **Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate
  ```

### 3. Run the Development Server
```powershell
.\.venv\Scripts\python manage.py runserver
```

Open your browser and navigate to:
- **E-Commerce Storefront:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Control Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔐 Default Login Credentials

| Role | Username / Email | Password | Access |
| :--- | :--- | :--- | :--- |
| **Super Admin** | `admin` (or `admin@admin.com`) | `admin123` | Full Admin Dashboard & Storefront |
| **Customer** | `user` (or `user@user.com`) | `admin123` | Storefront, Cart, Orders, Wishlist |
| **Customer** | `Asmit` (or `asmitmishra8299@gmail.com`) | `admin123` | Storefront, Cart, Orders, Wishlist |

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.  
Copyright (c) 2026 Md Kamar Rza Khan. All rights reserved.
