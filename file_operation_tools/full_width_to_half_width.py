"""
    将全角字符转为半角字符
"""


def to_half_width(text):
    half_width = ""
    for char in text:
        if char == u'\u3000':  # 处理全角空格
            half_width += u' '
        elif char >= u'\uff01' and char <= u'\uff5e':
            half_width += chr(ord(char) - 0xfee0)
        else:
            half_width += char
    return half_width


text = input("请输入要转换的字符串：")
converted_text = to_half_width(text)
print("转换后的字符串为：", converted_text)


