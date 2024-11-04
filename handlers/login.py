from controllers.login_controller import LoginController

def handler(event, context):
    return LoginController().login(event)