# 这个脚本会检查每行中文字幕的长度，并将超长（超过 35 个全角字符，一行中的每个半角字符按照 0.5 个计算）的行的行数标出。
# 注意：这个脚本只适用于 .srt 格式字幕。

def has_chinese(text: str) -> bool:  # 确定本行是否是含有汉字的行
    for char in text:

        # 40ee - 9fff 是中文文字（貌似包括了简体和繁体）的编码范围，3000 - 303f 是中/日/韩标点符号的编码范围
        if u'\u40ee' <= char <= u'\u9fff' or u'\u3000' <= char <= u'\u303f':
            return True
        return False

file_dir = input("请输入你想要检查的文件地址：")
subtitle_file = open(file_dir, mode="r", encoding="utf-8")

subtitle_lines = subtitle_file.readlines()
subtitle_file.close()

char_count = 0
line_index = 0

for line in subtitle_lines:
    if has_chinese(line):
        for char in line:
            if u'\u40ee' <= char <= u'\u9fff' or u'\u3000' <= char <= u'\u303f':
                char_count += 1
            else:
                char_count += 0.5

        if char_count > 35:
            line_index = subtitle_lines.index(line) + 1

            print("第", line_index, "行")

        char_count = 0
        line_index = 0
