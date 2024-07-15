import redis
import time

# Configuración de Redis
redis_host = 'redis-11879.c322.us-east-1-2.ec2.redns.redis-cloud.com'
redis_port = 11879  # Cambia al puerto correspondiente
redis_password = 'K8rK7a7ZsTD8Zf0Qb98ZV2ca9CMiNfdP'

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Publicador
def publisher():
    while True:
        message = input("Introduce un mensaje para publicar: ")
        redis_client.publish('canal_prueba', message)
        print(f"Publicado: {message}")

if __name__ == "__main__":
    publisher()
