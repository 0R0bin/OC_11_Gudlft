import app as personnal_app
from app import app


class TestBugMorePointsThanAllowed:
    client = app.test_client()
    competition = [
        {
            "name": "Competition Test",
            "date": "2024-04-28 18:00:00",
            "numberOfPlaces": "30"
        }
    ]

    club = [
        {
            "name": "Test club",
            "email": "test_club@test.fr",
            "points": "2"
        }
    ]

    def setup_method(self):
        """
        Replace DB Informations
        """
        personnal_app.competitions = self.competition
        personnal_app.clubs = self.club

    def test_booking_ok(self):
        """
        Test Réservation OK
        """
        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": self.club[0]["points"],
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )

        assert result.status_code == 200

    def test_booking_nok(self):
        """
        Test Réservation avec un nombre de points supérieur à celui du club
        """
        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": int(self.club[0]["points"]) + 1,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )

        assert result.status_code == 400
