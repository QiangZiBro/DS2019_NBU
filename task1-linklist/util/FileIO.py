import os
import json

def save_json(path, data, pos=0):
    data = json.dumps(data)
    lines = []
    with open(path, 'r', encoding='utf-8') as f:
        for item in f.readlines():
            lines.append(item)

    data += ',\n'
    lines.insert(pos, data)
    s = ''.join(lines)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)


def get_file_line_num(path):
    try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                return len(lines)
    except Exception as e:
        print('File not exist!', e)
        return 0



class SaveJson(object):

    def save_file(self, path, item):

        # 先将字典对象转化为可写入文本的字符串
        item = json.dumps(item)

        try:
            if not os.path.exists(path):
                with open(path, "w", encoding='utf-8') as f:
                    f.write(item + ",\n")
                    print("^_^ write success")

            else:
                with open(path, "a", encoding='utf-8') as f:
                    f.write(item + ",\n")
                    print("^_^ write success")

            return get_file_line_num(path)
        except Exception as e:
            print("write error==>", e)


class LoadJson(object):

    def read_line(self, path, line):
        try:
            if not os.path.exists(path):
                print('File is not exist!')
            else:
                with open(path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    return lines[line]
                    print('read success!')
        except Exception as e:
            print('read error!!!', e)

if __name__ == '__main__':
    # 保存的文件名
    path = "test.json"

    s = LoadJson()
    data_str = s.read_line(path, 0)
    #去掉最后的逗号
    data_str = data_str[:-2]
    data = json.loads(data_str)
    print(type(data))
    # s = SaveJson()
    # for i in range(10):
    #
    #     item = {
    #         'ID':'id ' + str(i),
    #         'name': 'name ' + str(i),
    #         'age': 'age ' + str(i),
    #         'date': 'date ' + str(i),
    #         'sex': 'sex ' + str(i)
    #     }
    #     s.save_file(path, item)
