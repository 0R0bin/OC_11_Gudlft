import app as personnal_app
from app import app


class TestErrorMail:
    client = app.test_client()

    def test_mail_empty(self):
        """
        Mail non renseigné
        """
        result = self.client.post("/showSummary", data={"email": ""})
        assert result.status_code == 400

    def test_mail_ok(self):
        """
        Mail connu
        """
        result = self.client.post("/showSummary", data={"email": personnal_app.clubs[0]["email"]})
        assert result.status_code == 200

    def test_mail_nok(self):
        """
        Mail inexistant
        """
        result = self.client.post("/showSummary", data={"email": "cemailnexitepas@test.fr"})
        assert result.status_code == 401

