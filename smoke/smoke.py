import smspool_sdk
from smspool_sdk.rest import ApiException

config = smspool_sdk.Configuration(host="https://api.smspool.net")
with smspool_sdk.ApiClient(config) as client:
    countries = smspool_sdk.InformationApi(client).country_retrieve_all()
    assert isinstance(countries, list) and countries, countries
    print("countries:", len(countries), countries[0])
    rates = smspool_sdk.InformationApi(client).request_success_rate(service="1")
    assert rates, rates
    print("success_rate (form POST):", str(rates)[:80])

config = smspool_sdk.Configuration(host="https://api.smspool.net", access_token="0" * 32)
with smspool_sdk.ApiClient(config) as client:
    try:
        smspool_sdk.InformationApi(client).request_balance()
        raise SystemExit("expected an auth error")
    except ApiException as e:
        assert e.status in (401, 403), e.status
        print("bad key ->", e.status, e.body[:80])
print("PYTHON OK")
