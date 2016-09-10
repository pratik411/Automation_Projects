from woocommerce import API
print "Lets Get Started"
class REQ():

    def __init__(self):

        admin_consumer_key = 'ck_09a6e74d39c45b2b171711124f68556f426a9ff0'
        admin_consumer_secret = 'cs_1ddfd29412736fc55eac22aad0d9cc181ec23995'

        self.wcapi = API (
            url="http://127.0.0.1/ak_store",
            consumer_key = admin_consumer_key,
            consumer_secret= admin_consumer_secret,
            version="v3")

    def test_api(self):

        print self.wcapi.get("").json()

#x = REQ()
#x.test_api()
#...

    def Post(self, endpoint, data):

        result = self.wcapi.post(endpoint,data)
        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]

    def Get(self, endpoint):
        result = self.wcapi.post(endpoint)

        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]