from ftd_client import FTDClient

client = FTDClient()
client.login()
bclient = client.get_client()
bclient.NetworkObject.getNetworkObjectList().result()
bclient.NetworkObject.getNetworkObjectList().result()['items'][0]
bclient.InterfaceInfo.getInterfaceInfo(objId='default').result()
bclient.Interface.getPhysicalInterfaceList().result()
bclient.WebUICertificate.getWebUICertificateList().result()
bclient.WebUICertificate.getWebUICertificateList().response().result
