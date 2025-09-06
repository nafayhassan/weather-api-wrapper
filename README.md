---

# 🌦️ Weather API Wrapper

<img width="1536" height="1024" alt="Weather API Wrapper Dashboard" src="https://github.com/user-attachments/assets/a3d54011-3299-4742-b87d-5bf1981fd713" />

A simple and professional Weather API Wrapper built with **FastAPI**, **SQLite**, and **httpx**.
This project fetches weather data from the free [Open-Meteo API](https://open-meteo.com/) and stores query history locally.

<img width="1536" height="1024" alt="Weather API Wrapper Flowchart" src="https://github.com/user-attachments/assets/88f056ec-985f-4be4-8a55-4e885f1e71c8" />

---

## ⚡ Features

* Fetch **current weather** by city 🌍
* Fetch **current weather by GPS coordinates** 📍
* Fetch **5-day forecast** for a city 📅
* Store weather history in SQLite 🗄️
* Retrieve all history records 📖
* Delete history records ❌
* List all unique cities queried 🏙️

---

## 🛠️ Tech Stack

* **FastAPI** – Web framework
* **httpx** – Async HTTP client for API calls
* **SQLite + SQLAlchemy** – Database & ORM
* **Pydantic** – Data validation

---

## 📦 Installation

```bash
# Clone repo
git clone https://github.com/your-username/weather-api-wrapper.git
cd weather-api-wrapper

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
```

---

## 🔗 API Endpoints

### 1. Health Check

```http
GET /ping
```

✅ Response:

```json
{
  "message": "pong"
}
```

---

### 2. Get Current Weather by City

```http
GET /weather/{city}
```

✅ Example:

```http
GET /weather/Lagos
```

Response:

```json
{
  "id": 1,
  "city": "Lagos",
  "temperature": 29.5,
  "description": "Partly cloudy",
  "timestamp": "2025-09-05T17:50:23"
}
```

---

### 3. Get Current Weather by Coordinates

```http
GET /weather/coordinates?lat={lat}&lon={lon}
```

✅ Example:

```http
GET /weather/coordinates?lat=6.5244&lon=3.3792
```

Response:

```json
{
  "id": 2,
  "city": "(6.5244,3.3792)",
  "temperature": 29.0,
  "description": "Clear sky",
  "timestamp": "2025-09-05T17:55:42"
}
```

---

### 4. Get 5-Day Forecast

```http
GET /forecast/{city}?days=5
```

✅ Example:

```http
GET /forecast/London?days=5
```

Response:

```json
{
  "city": "London",
  "daily": {
    "temperature_2m_max": [23.5, 22.1, 21.7, 24.0, 25.3],
    "temperature_2m_min": [15.2, 14.8, 14.5, 15.0, 16.3]
  }
}
```

---

### 5. Get Weather History

```http
GET /history
```

✅ Response:

```json
[
  {
    "id": 1,
    "city": "Lagos",
    "temperature": 29.5,
    "description": "Partly cloudy",
    "timestamp": "2025-09-05T17:50:23"
  },
  {
    "id": 2,
    "city": "(6.5244,3.3792)",
    "temperature": 29.0,
    "description": "Clear sky",
    "timestamp": "2025-09-05T17:55:42"
  }
]
```

---

### 6. Delete History Record

```http
DELETE /history/{id}
```

✅ Example:

```http
DELETE /history/2
```

Response:

```json
{
  "message": "Record 2 deleted"
}
```

---

### 7. List All Queried Cities

```http
GET /cities
```

✅ Response:

```json
{
  "cities": ["Lagos", "London", "(6.5244,3.3792)"]
}
```

---

## 🧪 Testing with Postman

* Import the endpoints above into Postman
* Start the server with:

  ```bash
  uvicorn main:app --reload
  ```
* Test endpoints like:

  * `http://127.0.0.1:8000/weather/Lagos`
  * `http://127.0.0.1:8000/forecast/London?days=3`

---

## 🚀 Future Improvements

* Add caching with **Redis** for faster repeated lookups
* Add user authentication with **JWT tokens**
* Build a **React frontend** for visualizing weather

---

## 📄 License

MIT License. Free to use and modify.

---

---

## 👤 Author

**Ipaye Babatunde**

* 🌍 Lagos, Nigeria
* 📧 [b.tunde.ipaye@gmail.com](mailto:b.tunde.ipaye@gmail.com)
* 🔗 [LinkedIn](https://linkedin.com/in/engripayebabatunde)
* 💻 [GitHub](https://github.com/engripaye)

---

