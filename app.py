from flask import Flask, render_template, jsonify
from invasions import InvasionTimer

app = Flask(__name__)


@app.route('/invasion.json')
def json():
    invasion_timer = InvasionTimer()

    return jsonify({
        'last_invasion': invasion_timer.last_invasion_date.isoformat(),
        'next_invasion': invasion_timer.next_invasion_date.isoformat(),
        'invasion_running': invasion_timer.invasion_running,
        'time_left': invasion_timer.invasion_time_left,
    })


@app.route('/')
def index():
    invasion_timer = InvasionTimer()

    if invasion_timer.invasion_running:
        return render_template(
            'running.html',
            start=invasion_timer.last_invasion_date,
        )
    else:
        return render_template(
            'not_running.html',
            next_date=invasion_timer.next_invasion_date,
        )
