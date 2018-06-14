
from tempfile import TemporaryFile

f = TemporaryFile()
f.write("Hello World")
f.seek(0)
print(f.readlines())
f.close()



$ python example.py
['Hello World']



<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-4058794840952844"
     data-ad-slot="4835580402"
     data-ad-format="auto">

(adsbygoogle = window.adsbygoogle || []).push({});



   
 


  
    Related ExamplesNamedTemporaryFileReading From A Temporary FileSpooledTemporaryFilemkdtempmkstemp


<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-4058794840952844"
     data-ad-slot="1144086401"
     data-ad-format="auto">

(adsbygoogle = window.adsbygoogle || []).push({});


5
   
 

 


  
  







