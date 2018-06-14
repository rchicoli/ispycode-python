
import os
import sys

# open file
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# get a file object from  file descriptor
fo = os.fdopen(fd, "w+")

# close file
fo.close()




<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-4058794840952844"
     data-ad-slot="4835580402"
     data-ad-format="auto">

(adsbygoogle = window.adsbygoogle || []).push({});



   
 


  
    Related ExamplesGet Effective Group IdGet Effective User IdGet File StatGet GroupsGet Parent Process IdGet Process IdGet Real Group IdGet Real User IdGet UnameGet User NameIterating Through OS Environment ItemsUser and group information for a processchdirclosectermidenvironfchdirfdopengetcwdgetcwdbgetegidgetenvgeteuidgetgidgetgroupsgetlogingetpgidgetpgrpgetpidgetppidgetuidnamestrerroruname


<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-4058794840952844"
     data-ad-slot="1144086401"
     data-ad-format="auto">

(adsbygoogle = window.adsbygoogle || []).push({});


34
   
 

 


  
  







