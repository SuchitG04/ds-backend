#!/bin/bash

python populate_queue_quizzes.py
python populate_recursion_quizzes.py
python populate_videos.py

fastapi run app/main.py --port 8001
