
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        admin = request.form.get('username')
        password = request.form.get('password')
        if admin and password == 'admin123':
            session['admin'] = admin
            return redirect(url_for('dashboard'))
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'admin' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', admin=session['admin'])

@app.route('/log_events')
def log_events():
    if 'admin' not in session:
        return redirect(url_for('login'))
    logs = [
        {"event": "CREATED", "file": "report.txt"},
        {"event": "MODIFIED", "file": "report.txt"},
        {"event": "DELETED", "file": "data.csv"}
    ]
    return render_template("log_events.html", logs=logs, admin=session['admin'])

@app.route('/pattern_analysis')
def pattern_analysis():
    if 'admin' not in session:
        return redirect(url_for('login'))
    return render_template("pattern_analysis.html", admin=session['admin'])

@app.route('/alerts')
def alerts():
    if 'admin' not in session:
        return redirect(url_for('login'))
    return render_template("alerts.html", admin=session['admin'])

@app.route('/admin_panel')
def admin_panel():
    if 'admin' not in session:
        return redirect(url_for('login'))
    return render_template("admin_panel.html", admin=session['admin'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
