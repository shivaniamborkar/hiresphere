from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
    'id' : 1,
    'title' : 'Data Scientist',
    'location' : 'Remote',
    'salary' : '1,20,000 Rs'
    },

    {
    'id' : 2,
    'title' : 'Data Scientist',
    'location' : 'Bangalore, India',
    'salary' : '1,20,000 Rs'
    },

    {
    'id' : 3,
    'title' : 'Data Scientist',
    'location' : 'Remote',
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)