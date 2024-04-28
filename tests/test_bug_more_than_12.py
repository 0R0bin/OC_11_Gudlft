import app as personnal_app
from app import app

class TestBugBook12:
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
            "points": "50"
        }
    ]

    places_booked = {
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
        personnal_app.competitions = self.competition
        personnal_app.clubs = self.club
        personnal_app.count_places = self.places_booked

    def test_book_ok(self):

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": 1,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )

        assert result.status_code == 200

    def test_book_12_os(self):

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": 13,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )

        assert result.status_code == 400

    def test_book_12_total(self):

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": 3,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )

        assert result.status_code == 400
