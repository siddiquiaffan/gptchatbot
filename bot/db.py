import redis
from dotenv import load_dotenv
load_dotenv()

db = redis.Redis(host=os.getenv('REDIS_HOST') , port=int(os.getenv('REDIS_PORT')), password=os.getenv('REDIS_PASSWORD') )

db.ping()

