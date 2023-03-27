<img src="https://cdn.dribbble.com/users/962944/screenshots/14138307/media/ca3377660c3d2053c9d91ac175871429.gif" alt="Stats" width="1000" height="200">
<h2>Football Stats</h2>
https://football-stats-rkzp.onrender.com/
<p>Football stats is a tool that allows you to compare the performance of two football teams.
This is achieved by reading stats of top European leagues from a CSV file. The tool then
calculates and displays the statistics of the selected teams in a user friendly way. 
I try to update the stats daily by automatically downloading the latest stats from a deignated Dropbox folder.
</p>

First clone the project by running: `git clone git@github.com:a-t-h-i/Football-Stats.git`

Then cd to the cloned project by running: `cd Football-Stats`

You will have to create a virtual environment so that you don't install dependencies system wide. You don't need to create it but you definetly would want to if you don't want to install useless Python libraries on your system 😄. To create a virtual env run the following command:`python -m venv env`

Run this to activate the virtual env:`source env/bin/activate`

Run this command to install the dependencies:`pip install -r requirements.txt`

After installing the dependencies, you can run this app using: `gunicorn footstats.wsgi:application`

Open your browser and goto:`127.0.0.1:8000`
