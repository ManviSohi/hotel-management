# 🏨 GrandStay Hotel Management System

A full-stack **Hotel Management & Chatbot Web Application** built using **Flask (Python)** and **HTML, CSS, JavaScript**.

This project provides an interactive hotel website with a smart chatbot that helps users get information about rooms, pricing, amenities, and more.

---

## 🚀 Features

* 💬 **AI Chatbot API**

  * Ask about rooms, prices, amenities, etc.
  * Endpoint: `/chat`

* 🛏️ **Room Information**

  * View available rooms with pricing and details
  * Endpoint: `/rooms`

* 📞 **Contact Information**

  * Get hotel contact details
  * Endpoint: `/contact`

* 🌐 **Modern Frontend UI**

  * Elegant hotel website design
  * Integrated chatbot interface

* 🔗 **Frontend + Backend Integration**

  * JavaScript `fetch()` connects UI to Flask API

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **API Testing:** Postman / Thunder Client

---

## 📂 Project Structure

```
hotel-management/
│
├── main.py            # Flask backend server
├── index.html         # Frontend UI
├── script.js          # Chatbot frontend logic
├── styles.css         # Styling (if separate)
├── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/hotel-management.git
cd hotel-management
```

### 2️⃣ Install dependencies

```
pip install flask flask-cors
```

### 3️⃣ Run the server

```
python main.py
```

---

## 🌐 API Endpoints

### 🔹 Home

```
GET /
```

### 🔹 Chatbot

```
POST /chat
```

**Request Body:**

```
{
  "message": "room price"
}
```

---

### 🔹 Rooms

```
GET /rooms
```

---

### 🔹 Contact

```
GET /contact
```

---

## 🧪 Example Response

```
{
  "reply": "💰 GrandStay Room Rates...",
  "status": "ok",
  "hotel": "GrandStay Hotel"
}
```

---

## 🎯 Future Improvements

* 🧠 Integrate real AI (OpenAI / LLM)
* 🗄️ Add database (MongoDB / MySQL)
* 🔐 User authentication (Login/Signup)
* 🛒 Room booking system
* 🌍 Deploy on cloud (Render / Railway / Vercel)

---

## 👩‍💻 Author

**Manvi Sohi**

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!

##Video Review

https://drive.google.com/file/d/1pfeFspBM3igYiQsNSA67fozUpF4IIKhC/view?usp=sharing
