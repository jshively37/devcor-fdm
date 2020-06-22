# WWT DEVCOR FDM Demo

## Installation

```pip install -r requirements.txt```

This is also designed to run off the [Cisco Reservable FDM Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/0920f396-6ebe-4445-af04-72a4a38ba374?diagramType=Topology)

## Usage

From the command prompt type in ```ipython```.

To create an instance:
```python
from ftd_client import FTDClient
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

## Help

How to determine other calls that are available:
```python
dir(bclient)
```

This will return a list and you can keep issuing dir(bclient.item_from_list). For example,
```python
dir(bclient.Interface)
```
wil return:
```
In [5]: dir(bclient.Interface)
Out[5]:
['addBridgeGroupInterface',
 'addEtherChannelInterface',
 'addEtherChannelSubInterface',
 'addInterfaceMigrationImmediate',
 'addSubInterface',
 'addVlanInterface',
 'deleteBridgeGroupInterface',
 'deleteEtherChannelInterface',
 'deleteEtherChannelSubInterface',
 'deleteJobHistoryInterfaceMigration',
 'deleteSubInterface',
 'deleteVlanInterface',
 'editBridgeGroupInterface',
 'editEtherChannelInterface',
 'editEtherChannelSubInterface',
 'editPhysicalInterface',
 'editSubInterface',
 'editVlanInterface',
 'getBridgeGroupInterface',
 'getBridgeGroupInterfaceList',
 'getEtherChannelInterface',
 'getEtherChannelInterfaceList',
 'getEtherChannelSubInterface',
 'getEtherChannelSubInterfaceList',
 'getInterfaceData',
 'getInterfaceDataList',
 'getInterfaceMigrationImmediateList',
 'getJobHistoryInterfaceMigration',
 'getJobHistoryInterfaceMigrationList',
 'getPhysicalInterface',
 'getPhysicalInterfaceList',
 'getSubInterface',
 'getSubInterfaceList',
 'getVlanInterface',
 'getVlanInterfaceList']
 ```
