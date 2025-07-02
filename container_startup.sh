#!/bin/bash

python populate_queue_quizzes.py
python populate_recursion_quizzes.py
python populate_videos.py

uvicorn app.main:app --host 0.0.0.0 --port 8001
