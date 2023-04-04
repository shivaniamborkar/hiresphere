from sqlalchemy import create_engine, text
import os 

db_connection_string = os.getenv("DB_CONNECTION_STRING")
engine = create_engine(
    db_connection_string,
    connect_args = {
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        #column_names = ['id','title','location','salary','currency','responsibilities','requirements']
        column_names = result.keys()
        jobs = []
        for row in result.all():
            #print(dict(row))
            jobs.append(dict(zip(column_names,row)))
        return jobs