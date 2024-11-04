import boto3
import bcrypt

class UserModel:
    def __init__(self):
        #definir a tabela no dynamo e criar script para criar usuarios
        self.dynamo = boto3.resource('dynamodb').Table('usuarios_adm')
    
    def create_user(self, username, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.dynamo.put_item(Item={'username': username, 'password':hashed_password})

    def authenticate (self, username, password):
        user = self.dynamo.get_item(key={'username': username}).get('Item')
        if user and bcrypt.checkpw(password.encode(), user['password'].encode()):
            return True
        return False