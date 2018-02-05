import jsonrpclib
import ENV

URL = "http://" + ENV.RECOMMENDATION_SERVER_HOST + ":" + str(ENV.RECOMMENDATION_SERVER_PORT)

client = jsonrpclib.ServerProxy(URL)

def getPreferenceForUser(userId):
    preference = client.getPreferenceForUser(userId)
    print("Preference list: %s" % str(preference))
    return preference
