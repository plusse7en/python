#!/usr/bin/env python3

from wyethAES import AESCipher
import pandas as pd

cipher = AESCipher()

input_path = 'input_values.csv' # 一行一个手机号或者加密码
output_path = 'cipher_phone_numbers.csv'

# 读取输入文件
df = pd.read_csv(input_path, header=None)
input_values = df[0].tolist()  # 手机号码都在第一列（索引为 0）

output = []
for input_value in input_values:
  input_value = str(input_value)
  if len(input_value) == 11:
    # 加密
    encrypted_text = cipher.encrypt(input_value)
    phone_number = input_value
    cipher_code = encrypted_text
  else:
    # 解密
    decrypted_text = cipher.decrypt(input_value)
    phone_number = decrypted_text
    cipher_code = input_value

  output.append(phone_number + ' => ' + cipher_code)

#写入文件
series = pd.Series(output, name="Phone Numbers")
series.to_csv(output_path, index=False, header=False)
