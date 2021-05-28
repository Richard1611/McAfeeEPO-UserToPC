# McAfeeEPO-UserToPC
Python tool that get all computers where users login within an environment with McAfee AV + EPO.  
The script use filter the devices by Tags and print just the workstations ( =! 'Server).

## Usage:
McAfeeEpo-UserToPC.py -i c:\path\to\inputfiletxt -o c:\path\to\outputfile.txt  

* Note: Outputfile is created if not exist
* Install dependencies:
  - [McAfee Epo Python Module](https://github.com/Richard1611/McAfeeEPO-UserToPC/blob/main/mcafee.py) must be located at the same directory of McAfeeEpo-UserToPC.py.
  - Install other dependencies from [requirements.txt](https://github.com/Richard1611/McAfeeEPO-UserToPC/blob/main/requirements.txt)
