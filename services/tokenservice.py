from datetime import datetime, timedelta, UTC

import jwt
# pip install pyjwt

jwt_secret = "hello_world"
jwt_alg = "HS256"

def create_token(data: dict):
    token = jwt.encode(
        data,
        key=jwt_secret,
        algorithm=jwt_alg
    )

    return token

def verify_token(token: str):

    decode_data = jwt.decode(
        token,
        key=jwt_secret,
        algorithms=jwt_alg
    )

    return decode_data



if __name__ == "__main__":

    exp_time  = datetime.now(UTC) + timedelta(minutes=30)
    
    my_data ={
        "login": "maxim",
        "role": "admin",
        "exp": exp_time,
        "type": "access"
    }

    my_token = create_token(my_data)


    print(my_token)

    print(verify_token(my_token))