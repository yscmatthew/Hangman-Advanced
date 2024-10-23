#Documentation: This program firs encodes the string you input to integer first, then 
# it gets the remainder of the (length of your string) and your password,
#then add it to the encoded result. Decrypt it with your password on (Decry) Level 1 Remainder Decryptor. https://replit.com/@yscmatthew/Decry-Level-1-Remainder-Decryptor#main.py

#With longer the password and longer the string, it will enhance the encoded result strength and complexity.
import math
constants = [3.141592561739,2.492828282828,1.0838171034,0.7896201647]
dish = 0
dishrecls = []
all_encry_keys = ''
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
temp5 = ''
key = 555
allecroad = 0
drivearr2 = 0
all_enc_keys_length = 0
convertedToIntPw = ''
result = ''
base = "0abcdefghijklmnopqrstuvwxyz !:)(&^%$#@*1234567890,.'ABCDEFGHIJKLMNOPQRSTUVWXYZ~`|?><;}{+_-=äßüöæ█★♥" #the first index (0) will never go checking #the length is 99
#function zone (py X like js where u hv to define the fun first) 
def encrypt2(key):
  global all_encry_keys,temp1, temp2, temp3, temp4, all_enc_keys_length
  temp1 = (key/constants[0])
  temp2 = key/constants[1]
  temp3 = key/constants[2]
  temp4 = key/constants[3]
  temp1 = str(temp1)
  temp2 = str(temp2)
  temp3 = str(temp3)
  temp4 = str(temp4)
  #SOMETIME WORKS as the position of '.' in temp1 isn't always same as others, anyway the longer pw, less likely to happen this
  all_encry_keys = (temp1 + temp2 + temp3 + temp4)
  #all_encry_keys = str(all_encry_keys)
  all_encry_keys = all_encry_keys.replace('.','1')
  all_enc_keys_length = len(all_encry_keys)
  all_encry_keys = int(all_encry_keys)

#use key's value to define add or minus
def erika():
  global drivearr2, dish, all_encry_keys, key, all_enc_keys_length, temp5
  all_encry_keys = int(all_encry_keys)
  
  if drivearr2 >= all_enc_keys_length:
    drivearr2 = 0
  else:
    all_encry_keys = str(all_encry_keys)
    temp5 = str(temp5)
    temp5 = all_encry_keys[drivearr2]
    temp5 = int(temp5)
    if key / 2 > 0:
      
      dish -= temp5
    else:
      dish += temp5
    all_encry_keys = int(all_encry_keys)
    drivearr2 += 1
    

def enc(key):
  global drivearr2,driveArr,convertedToIntPw,base,all_enc_keys_length,all_encry_keys,allecroad,gostr,dish,temp5,temp4,temp3,temp2,temp1,result
  #gostr = ("I personally do think that reading Reader's Digest every day doesn't improve my English skills that rapidly, but I enjoy that truely from my heart :3. As a palm-sized magazine issued since early 1900s, it is a legend.")
  gostr = 'ABCdef'
  #gostr = 'The threshould of forced auction should be decreased, in which it would be take action if more than property owners agree selling their own flats, in a building older than 50 years.'
  for drivePw in key:
      wordIndexToFind = base.index(drivePw,1)  #It starts searching from index 1, since base[0] shall never goes checking; wordIndexToFind is an integer, while drivePw is every single letter in the key var
      wordIndexToFind = f"{wordIndexToFind:02d}" #`f"{wordIndexToFind:02d}` means: Format the value of wordIndex2Find as a decimal integer, ensure it's at least 2 digits wide, and if it's not, pad it with zeros on the left........0 = the stuff to fill in the blank (if the var lengthed 1); 2 = required length of the var; d = decimal
      convertedToIntPw += wordIndexToFind
  key = int(convertedToIntPw)



  encrypt2(key)

  for i in range(len(gostr)):
      driveArr = 1
      for driveArr in range (len(base) + 1): #starts from 1
              if gostr[i] == base[driveArr]:
                  dish = driveArr
                  dish += (key % len(gostr)) #Encrypt w/ caesar ciphar's method first
                  dish = int(dish) #only serves 1 char
                  erika()
                ###
                
                  if dish > 99:
                    dish -= 99
                  if dish < 0:
                    dish += 99
                    #Insert another encrypting function here

                  break
      dish = str(dish)
      temp5 = dish
      temp5 = int(temp5)
      dish = base[temp5]
      temp5 = str(temp5)
      result += dish
  return result