---
# Weather API Wrapper 🌦️

<img width="1536" height="1024" alt="Weather API Wrapper Dashboard" src="https://github.com/user-attachments/assets/0d3d770d-5a5b-4537-8805-ad902ce285c0" />

A simple and professional **Weather API Wrapper** built with **FastAPI**.  
It fetches live weather data from the free [Open-Meteo API](https://open-meteo.com/), stores query history in **SQLite**, and returns results in a clean JSON format.  

---

## ✨ Features
- 🌍 Fetch real-time weather by city name  
- 💾 Store query history in SQLite  
- 📜 Retrieve full history of past queries  
- ⚡ Built with **FastAPI** + **httpx**  
- 🗄️ Lightweight with **SQLite**  

---

## 🛠️ Tech Stack
- **Python 3.11+**
- [FastAPI](https://fastapi.tiangolo.com/)
- [httpx](https://www.python-httpx.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- SQLite (default database)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)

---

```
````

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/weather-api-wrapper.git
cd weather-api-wrapper
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

Server will start at:
👉 `http://127.0.0.1:8000`

---

## 📌 API Endpoints

### ✅ Get Weather by City

**Request:**

```
GET /weather/{city}
```

**Example:**

```bash
curl http://127.0.0.1:8000/weather/Lagos
```

**Response:**

```json
{
  "city": "Lagos",
  "temperature": 28.5,
  "description": "Clear sky",
  "timestamp": "2025-09-05T16:30:12"
}
```

---

### 📜 Get Weather History

**Request:**

```
GET /history/
```

**Response:**

```json
[
  {
    "city": "Lagos",
    "temperature": 28.5,
    "description": "Clear sky",
    "timestamp": "2025-09-05T16:30:12"
  },
  {
    "city": "London",
    "temperature": 21.3,
    "description": "Cloudy",
    "timestamp": "2025-09-05T16:31:40"
  }
]
```

---

## 🧪 Testing with Swagger

FastAPI provides built-in API docs:

* Swagger UI 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc 👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📦 Future Improvements

* Add **weather forecasts (7-day)**
* Support for multiple weather providers (fallback API)
* Caching with **Redis**
* Docker support

---

## 👨‍💻 Author

**Your Name**
📧 [b.tunde.ipaye@gmail.com](mailto:b.tunde.ipaye@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/engripayebabatunde) | [GitHub](https://github.com/engripaye)

---

## 📜 License

This project is licensed under the MIT License.

```

---

Would you like me to also add a **section for Docker support** in the README so recruiters see it’s production-ready?
```
