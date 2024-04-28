import app as personnal_app
from app import app

class TestBugBook12:
    client = app.test_client()
    competitions = [
        {
            "name": "Competition Test",
            "date": "2025-04-28 18:00:00",
            "numberOfPlaces": "30"
        }
    ]

    club = [
        {
            "name": "Test club",
            "email": "test_club@test.fr",
            "points": "50"
        }
    ]

    count_places = {
        "Test club": 
        {
            'Competition Test': 
            {
                'places': 10
            },
        },
    }

    def setup_method(self):
        """
        Replace DB Informations
        """
        personnal_app.competitions = self.competitions
        personnal_app.clubs = self.club
        personnal_app.count_places = self.count_places

    def test_book_ok(self):
        """
        Test d'une réservation < 12 places
        """

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": 1,
                "club": self.club[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 200

    def test_book_12_os(self):
        """
        Test d'une réservation > 12 places d'une seule traite
        """

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": 13,
                "club": self.club[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 400

    def test_book_12_total(self):
        """
        Test d'une réservation > 12 places
        """

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": 3,
                "club": self.club[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 400
