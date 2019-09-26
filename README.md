# JeffBlum

D3 Graph: Tenor

// Setup virtual environment:
virtualenv -p python3 venv

// enter virtual environment:
source venv/bin/activate

// exit virtual environment:
deactivate

// setup local host:
python -m http.server 9000

// local server address:
http://localhost:9000/

// This is not exactly a trivial example as lines are treated differently compared to other d3 elements. The dates are also not simple and this is made even more complicated by the fact that they are not always sequential (they do not include weekends).
