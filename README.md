# railway-reservation-system
"A Restful Railway Reservation System API built with FastAPI, SQLAlchemy ORM, and PostgreSQL for managing train schedules, passenger bookings, and route destinations."

# 🚆 Railway Reservation System API

A Restful backend service built with FastAPI, SQLAlchemy, and PostgreSQL to manage train bookings, passenger itineraries, and destination routes.

---

## 📌 Project Overview
The Railway Reservation System API provides a structured backend pipeline for handling passenger reservations. It allows railway administrators and applications to issue ticket records, update passenger itineraries, query bookings, and remove cancelled reservations.

---

## 🧰 Tech Stack
* **Language:** Python
* **API Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Database Adapter:** `psycopg2-binary`
* **ASGI Server:** Uvicorn

---

## 📁 Repository Structure
* **`database.py`**: Handles database engine creation, connection strings, and SQLAlchemy session generation.
* **`models.py`**: Defines the `Passenger` relational database table schema.
* **`main.py`**: Contains FastAPI API endpoints for complete reservation management (`POST`, `GET`, `PUT`, `DELETE`).
* **`requirements.txt`**: Lists all project dependencies.

---
