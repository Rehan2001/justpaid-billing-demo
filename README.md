# 🚀 JustPaid Billing Demo — Mini B2B Invoice Automation SaaS

<p align="center">
  <b>Upload invoices → auto-process → detect overdue → visualize insights</b>
</p>

---

## 📌 Overview

This project is a **mini B2B billing automation tool** inspired by real-world fintech platforms like Stripe & JustPaid.

It enables users to upload invoice data, automatically process it, detect overdue payments, and visualize everything in a clean dashboard.

---

## ✨ Features

* 📂 CSV Upload System
* ⚡ Real-time Invoice Processing (Pandas)
* ⏰ Overdue Detection Engine
* 📊 Dashboard with Summary Metrics
* 🌐 REST API (Flask Backend)
* 🎯 Simple, Clean UI

---

## 🖼️ Demo Preview (Proof of Work)

👉 **Live UI Screenshot (Invoice Dashboard):**
[View Screenshot](https://github.com/Rehan2001/justpaid-billing-demo/blob/main/Invoice.png)

---

## 🧠 How It Works

1. Upload a CSV file containing invoice data
2. Backend processes:

   * Cleans amount values
   * Converts dates
   * Calculates overdue days
3. System classifies invoices:

   * ✅ Paid
   * ⚠️ Upcoming
   * ❌ Overdue
4. Results displayed in:

   * Summary dashboard
   * Invoice table

---

## 📄 Sample CSV Format

```csv
customer,amount,due_date,paid
Acme Corp,$4500,2025-03-15,no
ByteWave Inc,$12000,2025-04-01,yes
Stripe Ltd,$8750,2025-05-20,no
NovaBuild,$3200,2025-02-10,no
CloudSoft,$6100,2025-06-15,no
```

---

## 🏗️ Tech Stack

* **Backend:** Python, Flask
* **Data Processing:** Pandas
* **Frontend:** HTML, CSS, JavaScript
* **Dev Environment:** GitHub Codespaces

---

## ⚙️ Run Locally

```bash
git clone https://github.com/your-username/justpaid-billing-demo.git
cd justpaid-billing-demo

pip install -r requirements.txt
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 📊 API Endpoints

| Endpoint      | Method | Description                   |
| ------------- | ------ | ----------------------------- |
| `/api/upload` | POST   | Upload CSV & process invoices |
| `/api/health` | GET    | Health check                  |

---

## 💡 Key Highlights

* Built full-stack system from scratch
* Handles real-world invoice data processing
* Demonstrates backend + frontend integration
* Designed as a **mini SaaS product**

---

## 🚀 Future Improvements

* 📈 Charts & analytics (Chart.js)
* 🔐 Authentication system
* 📤 Export reports (PDF/CSV)
* 🧲 Drag & drop file upload
* ☁️ Docker + Cloud deployment

---

## 👨‍💻 Author

**Rehan Ahmad**
DevOps & Cloud Engineer

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---
