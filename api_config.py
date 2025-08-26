# Simulerad konfigurationsfil för en Python API-server
# DENNA FIL INNEHÅLLER KÄNSLIG INFORMATION OG SHOULD NEVER BE PUBLIC!

DATABASE = {
    'host': 'production-db.aws.com',
    'user': 'admin',
    'password': 'super_secret_password_123',  # <--- MYCKET BRA FYND FÖR DETECTIFY!
    'name': 'main_database'
}

API_KEYS = {
    'stripe': 'sk_live_1234567890abcdef',
    'google_maps': 'AIzaSyA_1234567890abcdef',
    'aws_access_key_id': 'AKIAIOSFODNN7EXAMPLE'
}

DEBUG = False  # Bra att den är False i production i alla fall!
