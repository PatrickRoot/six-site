#!/usr/bin/env bash

cmd=$(ps aux|grep sixlab_site|grep python|awk '{print $2}')

echo -e "PID: \n\033[31m\033[05m$cmd\033[0m"
echo "PID:$cmd"

for id in ${cmd}
    do
    kill -9 ${id}
    echo "kill $id"
    done

echo 'finish kill'

source venv/bin/activate

nohup python app.py -sixlab_site &