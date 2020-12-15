import jaydebeapi
import sys

argv = sys.argv

multicast_address = argv[1] # default : 239.0.0.1
port_no = argv[2] # default : 41999
cluster_name = argv[3]
username = argv[4]
password = argv[5]

url = "jdbc:gs://" + multicast_address + ":" + port_no + "/" + cluster_name
conn = jaydebeapi.connect("com.toshiba.mwcloud.gs.sql.Driver", url, [username, password], "./gridstore-jdbc.jar")

curs = conn.cursor()

curs.execute("DROP TABLE IF EXISTS Emotion")
curs.execute("CREATE TABLE IF NOT EXISTS Emotion ( name text, create_date date, created_at timestamp)")
print('SQL Create Table name=Emotion')
curs.execute("CREATE TABLE IF NOT EXISTS User ( email_address text, created_at timestamp)")
print('SQL Create Table name=User')
curs.close()
conn.close()
print('success!')