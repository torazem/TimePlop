SCHEMA = dict(
    project={
        "id": 1,
        "wid": 1,
        "cid": 1,
        "name": "foo",
        "billable": False,
        "is_private": True,
        "active": True,
        "template": False,
        "at": "2020-04-26T11:08:22+00:00",
        "created_at": "2020-04-24T13:05:35+00:00",
        "color": "9",
        "auto_estimates": False,
        "actual_hours": 20,
        "hex_color": "#a01aa5",
    },
    workspace={
        "id": 1,
        "name": "workspace",
        "profile": 0,
        "premium": False,
        "admin": True,
        "default_hourly_rate": 0,
        "default_currency": "USD",
        "only_admins_may_create_projects": False,
        "only_admins_see_billable_rates": False,
        "only_admins_see_team_dashboard": False,
        "projects_billable_by_default": True,
        "rounding": 1,
        "rounding_minutes": 0,
        "api_token": "foo",
        "at": "2018-05-14T15:07:19+00:00",
        "ical_enabled": True,
    },
    time_entries={
        "id": 1,
        "guid": "foo",
        "wid": 1,
        "pid": 1,
        "billable": False,
        "start": "2020-04-26T14:25:53+00:00",
        "stop": "2020-04-26T16:56:32+00:00",
        "duration": 123123,
        "description": "doing things",
        "duronly": False,
        "at": "2020-04-26T16:56:34+00:00",
        "uid": 1,
    },
    project_name={"id": 1, "name": "foo | bar"},
)
