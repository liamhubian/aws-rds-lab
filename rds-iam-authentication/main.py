import boto3
import mysql.connector


ENDPOINT="database-1.cq3sdvkw2sxo.ap-southeast-1.rds.amazonaws.com"
PORT="3306"
USER="admin"
REGION="ap-southeast-1"
DBNAME="mydb"

def main():
    session = boto3.Session(profile_name='defaul')
    client = session.client('rds')

    token = client.generate_db_auth_token(
            DBHostname=ENDPOINT,
            Port=PORT,
            DBUsername=USER
        )

    try:
        connection = mysql.connector.connect(
                host=ENDPOINT,
                user=USER,
                passwd=token,
                port=PORT
            )
        cur = conn.cursor()
        cur.execute("""SELECT now()""")
        query_results = cur.fetchall()
        print(query_results)
    except Exception as e:
        print("Database connection failed due to {}".format(e))

def if __name__ == "__main__":
    main()
