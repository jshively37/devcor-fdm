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

# Add a network
NetworkObject = bclient.get_model('NetworkObject')
new_network_object = NetworkObject(name='GOOGLE_DNS',
                                   subType='HOST',
                                   value='8.8.8.8',
                                   type='networkobject')
bclient.NetworkObject.addNetworkObject(body=new_network_object).result()

# Get network object by ID
bclient.NetworkObject.getNetworkObject(objId='3223b976-b54e-11ea-9a44-ab0e5f09a958').result()

# Delete a network Object
bclient.NetworkObject.deleteNetworkObject(objId='3223b976-b54e-11ea-9a44-ab0e5f09a958').result()


# Modify an interface
InterfaceObject = bclient.get_model('PhysicalInterfaceWrapper')
update_interface_object = InterfaceObject(name='GigabitEthernet0/4',
                                          description='Updated from Bravado',
                                          linkState='UP',
                                          enabled=True)

interface_dict = {
    'name': 'GigabitEthernet0/4',
    'description': 'Updated from Bravado',
    'enabled': True,
    'mtu': 1500,
    'mode': 'ROUTED',
    'monitorInterface': False,
    'type': 'haipv4address'
}
