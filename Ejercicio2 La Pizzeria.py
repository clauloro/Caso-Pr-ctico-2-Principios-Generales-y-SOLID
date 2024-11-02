class DataBaseManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        print("Conectado a la base de datos:", self.connection_string)


class Authenticator:
    def __init__(self, user_database):
        self.user_database = user_database

    def authenticate(self, username, password):
        print(f"Autenticando usuario: {username}")
        return True  


class PaymentProcessor:
    def __init__(self, api_key):
        self.api_key = api_key

    def process_payment(self, amount):
        print(f"Procesando pago de ${amount} con API key {self.api_key}")
        return True  


class OrderManager:
    def __init__(self, database_manager, authenticator, payment_processor):
        self.database_manager = database_manager
        self.authenticator = authenticator
        self.payment_processor = payment_processor

    def create_order(self, username, password, amount):
        if not self.authenticator.authenticate(username, password):
            print("Autenticación fallida.")
            return False

        if not self.payment_processor.process_payment(amount):
            print("Error en el procesamiento de pago.")
            return False

        print("Pedido creado y guardado en la base de datos.")
        return True


if __name__ == "__main__":
    database_manager = DataBaseManager("cadena-de-conexión-de-mi-bd")
    authenticator = Authenticator(database_manager)
    payment_processor = PaymentProcessor("clave-de-api-de-pago")

    order_manager = OrderManager(database_manager, authenticator, payment_processor)

    order_manager.create_order("usuario1", "contraseña123", 20.0)

    class MockAuthenticator:
        def authenticate(self, username, password):
            return True

    class MockPaymentProcessor:
        def process_payment(self, amount):
            return True

    mock_authenticator = MockAuthenticator()
    mock_payment_processor = MockPaymentProcessor()
    mock_database_manager = DataBaseManager("mock-connection-string")

    order_manager_test = OrderManager(mock_database_manager, mock_authenticator, mock_payment_processor)
    assert order_manager_test.create_order("test_user", "test_password", 10.0) == True
    print("Prueba de OrderManager pasada con mocks.")
