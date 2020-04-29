import jwt
from datetime import datetime, timedelta


JWT_SECRET = "jwt_secret_code"
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 86400

#todo проверять здесь на длеительность жизни. Если что выбрасывать пользователя
def create_jwt(id):
    payload = {
        "user_id": id,
        "exp": datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    }
    jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return str(jwt_token.decode('utf-8'))
