# Application Overview

## Need
The need for this type of program arises from team communication while on 
caravan. Members of the strategy team noted a distinct lack of data recorded
during a caravan session. Information such as events that happen with the car 
and how the team responds is not noted or kept, and any knowledge of situations 
is only as accurate as recounts from members involved.

Giving team members the ability to quickly note events throughout a driving
session will hopefully provide more operational insight and allow the team to
analyze events by time after a session is complete.

## Alternatives
* Text File
  * Fine for one person, but hard to compile with many users
* Online loggers
  * I'm not aware of any that exist, but we can't always rely on an internet 
  connection
* Desktop logging software
  * Again not aware, but **this may be a viable option.**

## Final functionality:
Basic use for logging of any text, with a criticality. This is the essential
functionality of the python `logging` library, and the application builds on 
this.

POS-style buttons and functionality should give any user of the program the 
ability to define buttons and quick log features to suit their positional needs.

Logs should go to one of at least 3 possible logs.
* Frontend
  * These are logs that are intended to be viewed by anyone on the team. These 
  are primarily text logs that do not contain many quantitative inputs. All 
  quantitative data should be handled by the program or output in the Data 
  Output log. 
* Backend
  * This is primarily used for debugging of the application itself. These logs 
  should only need to be read by developers or anyone interested in the 
  fundamental operation of the application. 
* Data Output
  * This log should contain specific data fields that are specified by the 
  application user. Each defined field should have a default parameter that 
  is inserted in the event a field is missing a parameter value. 
* User-Defined logs
  * _Reach Goal_
  * These n number of logs would be of use especially if certain logs would like
  to be kept from others. With the option of defining loggers and the parameters 
  associated with each included in the python `logging` library, this can be 
  leveraged to separate logs that may not be related.