#
# made by fixedOtter on 10.22.24
#

# importing pymongo package and the os for the environment var
import pymongo; import os;
from dotenv import load_dotenv;

# calling load dotenv to load env vars
load_dotenv()

connectionURI = os.environ.get('MONGOURI')

print(connectionURI)

myclient = pymongo.MongoClient(connectionURI)

print(myclient.list_database_names())