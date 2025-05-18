import os
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
#import numpy as np
from time import sleep
def get_all_file_sizes(root_dir):
    file_sizes = {}
    # 遍历根目录及其子目录
    print('正在尝试读取文件，时间挺久的，等一等……')
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # 获取文件大小（单位：字节）
                file_size = os.path.getsize(file_path)
                file_sizes[file_path] = file_size
            except FileNotFoundError:
                print(f"文件未找到: {file_path}")
            except PermissionError:
                print(f"无权限访问: {file_path}")
    print('读取完成！你这文件真多，有'+str(len(file_sizes))+'这么多！')
    return file_sizes

# 修改 get_digit 函数
def dec_to_base(num, base):
    if num == 0:
        return '0'
    digits = "0123456789ABCDEF"
    result = ""
    while num:
        result = digits[num % base] + result
        num //= base
    return result
def get_digit(num, position, base):
    num_str = dec_to_base(num, base)
    if len(num_str) >= position:
        return int(num_str[position - 1], base)
    else:
        if position == 1:
            return 0
        else:
            return 0
# 可以修改为你想要遍历的根目录，例如 'C:\\' 表示 C 盘
def analyze_digits_by_base(base):
    # 提取文件大小的首个数字
    df[f'{base}进制首位数字'] = df['文件大小(字节)'].apply(lambda x: get_digit(x, 1, base))
    # 统计每个首位数字出现的次数
    first_counts = df[f'{base}进制首位数字'].value_counts().sort_index()

    # 提取文件大小的第二位数字
    df[f'{base}进制第二位数字'] = df['文件大小(字节)'].apply(lambda x: get_digit(x, 2, base))
    # 统计每个第二位数字出现的次数
    second_counts = df[f'{base}进制第二位数字'].value_counts().sort_index()
    return first_counts,second_counts
def plot_size(counts,路径):
    first_counts=counts[0]
    secend_counts=counts[1]
    base=len(secend_counts)
    # 设置图片清晰度
    plt.rcParams['figure.dpi'] = 300
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
    # 解决负号显示问题
    plt.rcParams['axes.unicode_minus'] = False
    # 设置字体大小
    plt.rcParams['font.size'] = 6

    # 设置图表风格
    plt.style.use('ggplot')
    
    # 绘制子图
    plt.figure(figsize=(12, 5))
    # 绘制首位数字柱状图
    plt.subplot(1, 2, 1)
    
    bars1 = plt.bar(first_counts.index, first_counts.values, color='#a0d4e4', edgecolor='black')
    plt.bar(first_counts.index, first_counts.values,color='#a0d4e4', edgecolor='black')
    plt.xlabel(f'首位数字 (进制: {base})')
    plt.ylabel('出现次数')
    plt.title(f'{路径[0].upper()}盘文件大小{base}进制首位数字分布')
    plt.xticks(range(0, base))
    # 在柱子上方添加百分比
    total1 = sum(first_counts.values)
    for bar in bars1:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height / total1 * 100:.1f}%', ha='center', va='bottom')
    
    # 绘制第二位数字柱状图
    plt.subplot(1, 2, 2)
    bars2 = plt.bar(secend_counts.index, secend_counts.values, color='#c7ffe7', edgecolor='black')
    plt.bar(secend_counts.index, secend_counts.values,color='#c7ffe7', edgecolor='black')
    plt.xlabel(f'第二位数字 (进制: {base})')
    plt.ylabel('出现次数')
    plt.title(f'{路径[0].upper()}盘文件大小{base}进制第二位数字分布')
    plt.xticks(range(0, base))

        # 在柱子上方添加百分比
    total2 = sum(secend_counts.values)
    for bar in bars2:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height / total2 * 100:.1f}%', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()
    #return first_counts,secend_counts

root_directory = input('请输入你想统计的盘符（C盘不一定支持）：')+':\\'
all_file_sizes = get_all_file_sizes(root_directory)
# 将字典转换为 pandas 的 DataFrame
df = pd.DataFrame(list(all_file_sizes.items()), columns=['文件路径', '文件大小(字节)'])
first_counts_nums = []
secend_counts_nums = []
errornum=0
worningnum=0
while True:
    base=input("想看哪个进制的分布？2-16都可以哦,输我全都要可以看全部，输不玩了退出：")
    if base=='我全都要':
        for i in range(2, 17):
            print(f'正在统计{i}进制的分布……')
            first_counts, secend_counts = analyze_digits_by_base(i)  # 获取首位数字的分布
            first_counts_nums.append(first_counts)  # 将 first_counts 添加到列表中
            secend_counts_nums.append(secend_counts)  # 将 secend_counts 添加到列表中
            plot_size((first_counts,secend_counts),root_directory)
    elif base=='不玩了':
        print('那不玩了，拜拜！')
        sleep(2)
        break
    else:
        try:
            base_num=int(base)
        except:
            print('不要把奇怪的东西输入进来！！！')
            errornum+=1
            if errornum==3:
                print('这个不可以！！！我不玩啦！真的！！！')
                worningnum+=1
                if worningnum==3:
                    print('把我当日本人耍是吧？')
                    sleep(4)
                    print('手机没油了挂了吧拜拜')
                    break
                errornum=0
            continue
        if base_num>=2 and base_num<=16:
            first_counts, secend_counts = analyze_digits_by_base(base_num)  # 获取首位数字的分布
            first_counts_nums.append(first_counts)  # 将 first_counts 添加到列表中
            secend_counts_nums.append(secend_counts)  # 将 secend_counts 添加到列表中
            plot_size((first_counts,secend_counts),root_directory)
        else:
            print('数字不在范围内！好好输！')
