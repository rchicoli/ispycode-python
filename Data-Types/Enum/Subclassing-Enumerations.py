from enum import Enum

class Color(Enum):
 pass

class MoreColor(Color):
  red = 1
  orange = 2
  green = 3



The following example (example2.py) will cause a TypeError because the parent class has members: 

from enum import Enum

class Color(Enum):
  red = 1
  orange = 2

class MoreColor(Color):
  green = 3


Output (example2.py):

$ python3 example2.py
Traceback (most recent call last):
  File "example.py", line 7, in <module>
    class MoreColor(Color):
  File "/usr/lib/python3.5/enum.py", line 93, in __new__
    member_type, first_enum = metacls._get_mixins_(bases)
  File "/usr/lib/python3.5/enum.py", line 374, in _get_mixins_
    raise TypeError("Cannot extend enumerations")
TypeError: Cannot extend enumerations




<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-4058794840952844"
     data-ad-slot="4835580402"
     data-ad-format="auto">

(adsbygoogle = window.adsbygoogle || []).push({});



   
 


  
    Related ExamplesComparing EnumsCreating EnumerationsDuplicating Enum MembersDuplicating Enum ValuesEnsuring Unique Enumeration ValuesIntEnumIterating Over EnumsOrdered EnumSubclassing Enumerations


<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-4058794840952844"
     data-ad-slot="1144086401"
     data-ad-format="auto">

(adsbygoogle = window.adsbygoogle || []).push({});


9
   
 

 


  
  







