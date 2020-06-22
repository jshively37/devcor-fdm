# WWT DEVCOR FDM Demo

### Installation

```pip install -r requirements.txt```

This is also designed to run off the [Cisco Reservable FDM Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/0920f396-6ebe-4445-af04-72a4a38ba374?diagramType=Topology)

### Usage

From the command prompt type in ```ipython```.

To create an instance:
```python
client = FTDClient()
client.login()
bclient = client.get_client()
```

Return all network objects:
```python
bclient.NetworkObject.getNetworkObjectList().result()
```

Return interface information:
```python
bclient.Interface.getPhysicalInterfaceList().result()
```