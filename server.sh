#!/bin/bash
cd Frontend/front 
tmux new-session -d 'yarn start'
cd ../..
tmux split-window -v 'python3 ./Backend/manage.py runserver'
tmux -2 attach-session -d
