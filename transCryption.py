import argparse
from wyethAES import AESCipher
import pandas as pd
from jacklib import get_md5


def main():
    # 传参初始化
    parser = argparse.ArgumentParser(
        description='加密手机号或解密。',
        epilog='',
        add_help=True
    )

    default_message = '获取更多帮助请使用-h查看。'

    # 设置参数
    parser.add_argument('-a', '--aes', action='store_true', help='使用AES进行加密和解密')
    parser.add_argument('-j', '--jd', action='store_true', help='京东自营加密')
    parser.add_argument('-w', '--wyeth', action='store_true', help='天猫惠氏奶粉加密')
    parser.add_argument('-f', '--qifu', action='store_true', help='天猫启赋官方加密')

    parser.add_argument('-i', '--input', dest='input_file', help='待处理的csv文件名。只有一列，第一行为列标题，一行一个手机号或加密码。')
    parser.add_argument('-o', '--output', dest='output_file', help='保存处理后结果的csv文件名。')

    # 获取参数
    args = parser.parse_args()

    # 处理参数
    input_file = args.input_file  # 一行一个手机号或者加密码
    if not input_file:
        print('提示：请在-i后输入待处理的文件名（.csv文件，文件全名带扩展名，一行一个手机号或加密码）。')
        print(default_message)
        return

    output_file = args.output_file
    if not output_file:
        print('提示：请在-o后输入保存处理结果的文件名（.csv文件，文件全名带扩展名）。')
        print(default_message)
        return

    aes = args.aes
    jd = args.jd
    wyeth = args.wyeth
    qifu = args.qifu
    cnt = 0
    cnt += 1 if aes else 0
    cnt += 1 if jd else 0
    cnt += 1 if wyeth else 0
    cnt += 1 if qifu else 0
    if cnt != 1:
        print("提示：处理方式只能输入一个参数。")
        print(default_message)
        return

    # 程序主体逻辑...
    # 读取输入文件
    try:
        df = pd.read_csv(input_file)
        input_values = df.iloc[:, 0].tolist()  # 手机号码都在第一列（索引为 0）
    except:
        print('提示：读取文件出现异常。')
        print(default_message)
        return

    phone_number = ''
    cipher_code = ''
    phone_list = []
    cipher_list = []

    # 逐条处理
    for input_value in input_values:
        input_value = str(input_value)
        if aes:  # AES加密解密
            aescipher = AESCipher()
            if len(input_value) == 11:
                # 加密
                encrypted_text = aescipher.encrypt(input_value)
                phone_number = input_value
                cipher_code = encrypted_text
            else:
                # 解密
                decrypted_text = aescipher.decrypt(input_value)
                phone_number = decrypted_text
                cipher_code = input_value
        elif jd:  # 只有加密
            salt1 = 'dede5ceaa1ce0130a54388648548b6d4100000000000060'
            salt2 = 'dede5ceaa1ce0130a54388648548b6d4'

            phone_number = input_value
            cipher_code = salt1 + input_value + salt2
            cipher_code = get_md5(cipher_code).upper()
            cipher_code = get_md5(cipher_code).upper()
        elif wyeth:  # 只有加密
            secret_key = 'YuPqtH'

            phone_number = input_value
            cipher_code = get_md5(get_md5('tmall' + input_value + secret_key))
        elif qifu:  # 只有加密
            secret_key = 'tGZ9dj'

            phone_number = input_value
            cipher_code = get_md5(get_md5('tmall' + input_value + secret_key))

        phone_list.append(phone_number)
        cipher_list.append(cipher_code)

    # 写入文件
    df['phone_number'] = phone_list
    df['cipher_code'] = cipher_list
    df_output = df[['phone_number', 'cipher_code']]
    df_output.to_csv(output_file, index=False)
    # series = pd.Series(output, name="Phone Numbers")
    # series.to_csv(output_file, index=False, header=False)
    print('数据处理完成，请打开对应文件查看处理结果。')


if __name__ == '__main__':
    main()
