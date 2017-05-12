This is a project for my Free Culture Class. I just wanted to see what's going on with the Network Traffic on my computer.

This is a visualization of the incoming and outgoing traffic on my local machine. It's

### Keep in mind
![Legend](legend.jpg)


Run the webserver separately from the collector.

``` python manage.py runserver ```


``` python python tracker/collector.py ```

Note:
The collector requires root access.


After starting both webserver and collector, you may proceed to viewing the real time traffic.

### Requirements
  * Python 2

### Dependencies
  * django
  * scapy
  * websocket_server

### Disclaimers
  This is not capable of showing all traffic properly as it currently overwhelms the browser, so I've placed a delay in between. However, it's possible to store the data and replay it later if need be.
  Some might packets might still slip through the crack.
