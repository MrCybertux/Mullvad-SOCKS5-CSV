# Mullvad-SOCKS5-CSV
Python Scrypt to Generate a CSV file with the Mullvad SOCKS5 URLs

The List on https://mullvad.net/en/servers is very good but sometimes not ideal.

For example if you want to quickly switch IP quickly since your Freetube tells you the IP is rate limited by google.
This list has three columms Contry, Hostname and Continent.

A third Script for adding cities is in the works.

I did not find such a list before and just wanted to share my work with you.

# How to set up
This guide is intended for debian based Linux Distros but it should work with every linux.

open a shell in the location you want your script to run this command for example in: ~/Documents/Scripts

Here we are going to create a virtual enviorment for the python script:
```
python -m venv .
```
Now we can activate the virtual enviorment, if you want to use it in the future start from here:
```
source ./bin/activate
```
Now we install the depencies (You can skip this if you done it once):
```
pip install requests weget json csv
```
then you can run the scripts:
```
python mullvad.py
python mullvad_expand.py
```
The first command will create a csv called mullvad.csv it has the two columms Contry code and hostname.
The Secon script will create mullvad_hostnames_with_full_names_and_continents.csv it has expanded country names and a continent

You can then open it with excel oder libre office calc:

![image](https://github.com/user-attachments/assets/396ca46d-e92e-4373-bbcc-b9fd1d8f14c0)







Then you can sort it:
![image](https://github.com/user-attachments/assets/192ced91-e205-421f-987b-d9648221c28b)

![image](https://github.com/user-attachments/assets/b7253bf6-df1d-4a18-894b-4d4954c908ca)

and voila here you got a sortable list of all mullvad socks adress:
![image](https://github.com/user-attachments/assets/f1051453-e436-4332-af39-85db359919cf)

## Licence

I do not think i need a licence for that but in case here we go:

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright © 2025 MrCybertux
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
