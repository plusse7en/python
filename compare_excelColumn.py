import argparse
import pandas as pd


def main():
    # 传参初始化
    parser = argparse.ArgumentParser(
        description='比较两个excel文件中指定列的值，获得对应的交并差集，结果存于compare_result.xlsx文件',
        epilog='',
        add_help=True
    )

    default_message = '获取更多帮助请使用-h查看。'

    # 设置参数
    parser.add_argument('-i1', '--input1', dest='input_file1', help='第一个待比较的excel文件名，第一行是列名称。')
    parser.add_argument('-i2', '--input2', dest='input_file2', help='第二个待比较的excel文件名，第一行是列名称。')
    parser.add_argument('-c', '--column', dest='column_name', help='待比较的列名，两个excel要相同。')

    # 获取参数
    args = parser.parse_args()

    if not bool(args):
        print(default_message)

    # 处理参数
    input_file1 = args.input_file1
    if not input_file1:
        print('提示：请在-i1后输入第一个待比较的excel文件名，第一行是列名称。')
        print(default_message)
        return

    input_file2 = args.input_file2
    if not input_file1:
        print('提示：请在-i2后输入第二个待比较的excel文件名，第一行是列名称。')
        print(default_message)
        return

    column = args.column_name
    if not column:
        print('提示：请在-c后输入待比较的列名，两个excel要相同。')
        print(default_message)
        return

    # 程序主体逻辑...
    # 读取整个Excel文件
    try:
        df1 = pd.read_excel(input_file1, usecols=[column])
        df2 = pd.read_excel(input_file2, usecols=[column])
    except:
        print('提示：-c后输入待比较的列名在excel文件里不存在。')
        print(default_message)
        return

    # 如果需要，可以去除重复值（根据实际情况决定是否执行此步）
    # df1 = df1.drop_duplicates()
    # df2 = df2.drop_duplicates()

    # 使用merge函数，inner join得到交集
    intersection = pd.merge(df1, df2, how='inner', on=column)

    # 使用concat函数，drop_duplicates去除重复值后得到并集
    union = pd.concat([df1, df2]).drop_duplicates(subset=column)

    # 文件1差集
    difference1 = pd.merge(df1, df2, how='outer', indicator=True, on=column)
    difference1 = difference1[difference1['_merge'] == 'left_only'].drop('_merge', axis=1)

    # 文件2差集
    difference2 = pd.merge(df1, df2, how='outer', indicator=True, on=column)
    difference2 = difference2[difference2['_merge'] == 'right_only'].drop('_merge', axis=1)

    # 比较结果写入指定文件
    with pd.ExcelWriter('compare_result.xlsx') as writer:
        df1.to_excel(writer, sheet_name='文件1', index=False)
        df2.to_excel(writer, sheet_name='文件2', index=False)
        intersection.to_excel(writer, sheet_name='交集', index=False)
        union.to_excel(writer, sheet_name='并集', index=False)
        difference1.to_excel(writer, sheet_name='文件1差集', index=False)
        difference2.to_excel(writer, sheet_name='文件2差集', index=False)

    print('数据处理完成，请打开compare_result.xlsx文件查看处理结果。')


if __name__ == '__main__':
    main()
