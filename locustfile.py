# File created with the help of https://docs.locust.io/en/stable/writing-a-locustfile.html

from locust import HttpUser, task, between
from app import loadClubs, loadCompetitions


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    club = loadClubs()
    competition = loadCompetitions()

    def on_start(self):
        self.client.get("/", name="index")
        self.client.post("/showSummary", data={'email': self.club[0]["email"]}, name="show_summary")

    @task
    def view_booking(self):
        self.client.get(f"/book/{self.competition[0]['name']}/{self.club[0]['name']}", name="view_booking")

    @task
    def purchase_places(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "places": 1,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            },
            name="purchase_places"
        )

    @task
    def view_club_points(self):
        self.client.get("/viewClubPoints", name="view_club_points")
