import json
from models.user import UserModel

class LoginController:
    def __init__(self):
        self.user.model = UserModel()
    
    def login(self, event):
        data = json.loads(event.get('body', '{}'))
        if self.user_model.authenticate(data['username'], data['password']):
            return {'statusCode':200, 'body': json.dumps({'message': 'Login bem-secedido'})}
        return {'statusCode': 401, 'body': json.dumps({'message': 'Credenciais inválidas'})}