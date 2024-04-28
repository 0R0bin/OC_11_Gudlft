import app as personnal_app
from app import app


class TestBugBookingInPast:
    client = app.test_client()
    competitions = [
        {
            "name": "Competition Test",
            "date": "1999-11-19 11:00:00",
            "numberOfPlaces": "100"
        }
    ]

    club = [
        {
            "name": "Test club",
            "email": "test_club@test.fr",
            "points": "7"
        }
    ]

    count_places = {
        "Test club": 
        {
            'Competition Test': 
            {
                'places': 0
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

    def test_booking_in_past(self):
        """
        Test booking sur compétition passée
        """
        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": self.club[0]["points"],
                "club": self.club[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 400
