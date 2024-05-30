@echo off
SET MONGODB_URI=mongodb://localhost:27017/messengerapp_fastapi
SET JWT_SECRET=rs123456789


echo ====================== messengerapp_api ========================
uvicorn app:app --reload --port 5000 --host localhost