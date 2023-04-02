from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://n3zy5dlc43awi5gmdyy7:pscale_pw_u2pmiuCIPgGGT6hVNuOhyK0C2sBVv901QclLPVwoqRm@aws.connect.psdb.cloud/hiresphere?charset=utf8mb4"
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