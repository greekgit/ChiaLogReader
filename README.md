# ChiaLogReader
Very simple Python 3 script to read and analyse the current chia debug log to calculate average time between proof attempts, longest lookup time, number of proof attempts and number of proofs found.


 ## Introduction

  I wanted to keep an eye on the performance of my chia farm - in particular the lookup times when a plot passed the filter. 
  I got tired of using grep to pull the data from the log so decided to write a small python script to do it for me.
  
  
 ## Technologies
  
  The script was written in Pycharm for a Windows 10 system but I believe it should work for any chia system.
  
 ## Parameters
  
 
  No parameters required. Just hardcode your debug.log path into the 'logpath' variable and off you go!
  
  ## Notes
  
  For this to work you will need to ensure the chia logging level is set to INFO. Instructions on how to do this can be found here. https://thechiafarmer.com/2021/04/20/how-to-enable-chia-logs-on-windows/  

## Possible enhancements
 
 Recently extended to include older logs. 
 
