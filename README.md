# Python-Create-QR-Code

Goal is to create a python script to dynamically create QR codes based off a SN import excel file. Stores the .xlsx into a dataframe, converts to a list, gets serial numbers from the list, and adds a delimiter. The prefix and suffix is added to this string and the completed string is made into a QR code. 

In the attached example excel file, the serial numbers in the excel file will be transformed to be in the format: [)>{RS}20{GS}A35-0BW-RD6-04AA{GS}2290285393{GS}2290285394{GS}2290285395{GS}2290285396{GS}2290285397{GS}2290285398{GS}2290285399{GS}2290285400{GS}2290285401{GS}2290285402{GS}2290285403{GS}2290285404{GS}2290285405{GS}2290285406{GS}2290285407{GS}2290285408{GS}2290285409{GS}2290285410{GS}2290285411{GS}2290285412{GS}{RS}{Eot}
