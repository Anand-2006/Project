#!/bin/bash
python3 backend/app.py &
cd frontend && npm start &