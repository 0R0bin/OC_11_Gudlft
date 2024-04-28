import app as personnal_app
from app import app


class TestBugPointsUpdateDisplayed:
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

    def test_points_changed(self):
        """
        Test points bien enlevés
        """
        previous_points = int(self.club[0]["points"])
        nb_bookings = int(self.club[0]["points"]) - 1

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": nb_bookings,
                "club": self.club[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 200
        assert previous_points - nb_bookings == int(self.club[0]["points"])

