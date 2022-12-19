import json
from dataclasses import asdict, dataclass

from django.http import HttpResponse
from django.urls import path


@dataclass
class Sport:
    kind: str
    qulity_players: int
    famous_team: list


def get_result(variebles):
    football = Sport(
        kind="Football",
        qulity_players=11,
        famous_team=["Barselona", "Milan", "Manchester United"],
    )
    content = json.dumps(asdict(football))
    return HttpResponse(content)


urlpatterns = [
    path("result/", get_result),
]
