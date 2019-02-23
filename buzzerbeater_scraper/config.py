from decouple import config

BB_USERNAME = 'rkcerman'
BB_PASSWORD = 'konzola'
BB_API_PASSWORD = 'konzola2'

DATABASE_CONFIG = {
    'hostname': config('DB_HOST'),
    'username': config('DB_USER'),
    'password': config('DB_PASSWORD'),
    'database': config('DB_NAME'),
}

DEFAULT_SEASON=45
