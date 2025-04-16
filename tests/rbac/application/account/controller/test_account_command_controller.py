class TestAccountController:
    def test_유저_가입_Role_User(self, client):
        # Arrange
        payload = {
            "email": "test11@example.com",
            "password": "password123",
            "tenant_key": "demo-tenant",
            "role": "ADMIN"
        }

        # Action
        response = client.post("/account/signup", json=payload)

        # Assert
        assert response.status_code == 200
