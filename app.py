from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

# JOBS = [
#     {
#     'id' : 1,
#     'title' : 'Data Scientist',
#     'location' : 'Remote',
#     'salary' : '1,20,000 Rs'
#     },

#     {
#     'id' : 2,
#     'title' : 'Data Scientist',
#     'location' : 'Bangalore, India',
#     'salary' : '1,20,000 Rs'
#     },

#     {
#     'id' : 3,
#     'title' : 'Data Scientist',
#     'location' : 'Remote',
#     }
# ]


@app.route('/')
def hello_hiresphere():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not found", 404
    return render_template('jobpage.html', job=job)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)