import datetime
import base64


class Token:

    @staticmethod
    def create_email_verify_token(user_id):
        secret = user_id + " " + str(datetime.datetime.utcnow())
        message_bytes = secret.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return base64_message

    @staticmethod
    def decode_token_return_uid(token):
        try:
            base64_bytes = base64.b64decode(token).decode("utf-8") 
            user_id = base64_bytes.split(" ")[0]
            return user_id
        except:
            return None
