import json
import os


def save_info(data_dir, data, desc):
    # 创建保存目录
    save_path = os.path.join(data_dir, desc)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 保存 JSON 文件
    file_path = os.path.join(save_path, f'{desc}.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def convert_test_data_to_json(test_dir, save_dir):
    # 假设您的文件名为 'all_test_data.txt'
    all_test_data_file = os.path.join(test_dir, '1500.txt')

    # 初始化测试样例列表
    test_examples = []

    # 读取包含所有测试数据的文件
    with open(all_test_data_file, encoding='utf-8') as f:
        # 假设文件内容是一个 JSON 数组，直接解析为 Python 对象
        test_examples = json.load(f)

    # 保存为 JSON 格式
    save_info(save_dir, test_examples, 'test')


if __name__ == '__main__':
    test_dir = './tcdata/juesai'
    save_dir = './data/raw_data_random'
    convert_test_data_to_json(test_dir, save_dir)
    print('测试数据转换完成')
