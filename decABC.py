def decABC(pw2check,text2dec):
  #Notice: Use my another program Encrypt Remainder Text Advanced to get the encrypted numbers first.
  #A symmetric text decryptor, using a decryption text reference generated by finding remainer after using password to divide constants
  from getpass import getpass
  temp0 = 0
  gonum = '' #gonum has to remain as a string even it stores numbers
  base = "0abcdefghijklmnopqrstuvwxyz !:)(&^%$#@*1234567890,.'ABCDEFGHIJKLMNOPQRSTUVWXYZ~`|?><;}{+_-=äßüöæ█★♥" #the first index (0) will never go checking #the length is 99
  gowd = text2dec  #it will remain as str
  convertedToIntPw = ''
  for i in range(len(gowd)):
    temp0 = int(temp0)
    temp0 = base.index(gowd[i])
    temp0 = str(temp0)
    if len(temp0) == 1:
      temp0 = '0' + temp0   
    gonum = gonum + temp0

  dec_key = pw2check
  for drivePw in dec_key:
      wordIndexToFind = base.index(drivePw,1)  #It starts searching from index 1, since base[0] shall never goes checking; wordIndexToFind is an integer, while drivePw is every single letter in the key var
      wordIndexToFind = f"{wordIndexToFind:02d}" #`f"{wordIndexToFind:02d}` means: Format the value of wordIndex2Find as a decimal integer, ensure it's at least 2 digits wide, and if it's not, pad it with zeros on the left........0 = the stuff to fill in the blank (if the var lengthed 1); 2 = required length of the var; d = decimal
      convertedToIntPw += wordIndexToFind
  dec_key = int(convertedToIntPw)




  doublepick = ''
  decode_result = ''
  constants = [3.141592561739,2.492828282828,1.0838171034,0.7896201647]
  all_dec_ref = ''
  temp1 = 0
  temp2 = 0
  temp3 = 0
  all_dec_ref_len = 0
  dec_arr_driver = 0
  #func zone{

  def makekey():
    nonlocal constants, all_dec_ref, temp1, all_dec_ref_len, dec_key
    for i in range(0,4):
      temp1 = float(temp1)
      temp1 = dec_key / constants[i]
      temp1 = str(temp1)
      all_dec_ref = all_dec_ref + temp1
      all_dec_ref = all_dec_ref.replace(".","1")
    all_dec_ref_len = len(all_dec_ref)

  def decrypt2():
    nonlocal temp2, all_dec_ref, all_dec_ref_len, dec_arr_driver, dec_key, doublepick, gonum
    if dec_arr_driver >= all_dec_ref_len:
      dec_arr_driver = 0
    else:
      temp2 = str(temp2)
      temp2 = all_dec_ref[dec_arr_driver]
      temp2 = int(temp2)
      if (dec_key / 2) > 0:
        doublepick += temp2
      else:
        doublepick -= temp2
      dec_arr_driver += 1 
    

  makekey()
  for x in range(0, len(gonum), 2):
    #doublepick {
    doublepick = gonum[x]
    doublepick += gonum[x + 1]
    doublepick = int(doublepick)
    #}
    decrypt2()

    doublepick -= (dec_key % (len(gonum) / 2))
    if doublepick < 0:
      doublepick += 99
    if doublepick > 99:
      doublepick -= 99  
    decode_result = (decode_result + base[int(doublepick)])

  return decode_result
