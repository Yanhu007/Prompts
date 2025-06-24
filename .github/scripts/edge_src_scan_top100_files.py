#!/usr/bin/env python3
"""
分析edge_src_structure.txt文件，统计文件名出现次数，输出前100个最常见的文件名

功能：
- 读取./.outputs/edge_src_structure.txt文件
- 按文件名计数
- 输出数量最多的前100个文件名
- 输出文件：./.outputs/edge_src_top100_files.txt
- 输出格式：filename, count, 占总文件数百分比
"""

import os
import sys
from pathlib import Path
from collections import Counter


def extract_filename_from_path(file_path):
    """
    从文件路径中提取文件名
    """
    return os.path.basename(file_path.strip())


def analyze_file_structure(input_file_path):
    """
    分析文件结构，统计文件名出现次数
    
    Args:
        input_file_path (str): 输入文件路径
        
    Returns:
        tuple: (文件名计数器, 总文件数)
    """
    if not os.path.exists(input_file_path):
        print(f"错误：输入文件不存在 - {input_file_path}")
        return None, 0
    
    filename_counter = Counter()
    total_files = 0
    
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                # 跳过空行和目录行（通常以/结尾或不包含文件扩展名）
                if not line or line.endswith('/') or line.endswith('\\'):
                    continue
                
                # 提取文件名
                filename = extract_filename_from_path(line)
                
                # 只统计有文件名的行
                if filename and '.' in filename:
                    filename_counter[filename] += 1
                    total_files += 1
    
    except Exception as e:
        print(f"错误：读取文件时出现异常 - {e}")
        return None, 0
    
    return filename_counter, total_files


def write_top100_files(filename_counter, total_files, output_file_path, top_n=100):
    """
    写入前N个最常见的文件名到输出文件
    
    Args:
        filename_counter (Counter): 文件名计数器
        total_files (int): 总文件数
        output_file_path (str): 输出文件路径
        top_n (int): 输出前N个文件名，默认100
    """
    # 确保输出目录存在
    output_dir = os.path.dirname(output_file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    # 获取前N个最常见的文件名
    top_files = filename_counter.most_common(top_n)
    
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            # 写入表头
            f.write("filename,count,percentage\n")
            
            # 写入数据
            for filename, count in top_files:
                percentage = (count / total_files * 100) if total_files > 0 else 0
                f.write(f"{filename},{count},{percentage:.2f}%\n")
        
        print(f"成功生成文件：{output_file_path}")
        print(f"总文件数：{total_files}")
        print(f"独特文件名数：{len(filename_counter)}")
        print(f"输出前{len(top_files)}个最常见的文件名")
        
    except Exception as e:
        print(f"错误：写入输出文件时出现异常 - {e}")


def main():
    """
    主函数
    """
    # 设置文件路径
    script_dir = Path(__file__).parent.parent.parent  # 回到项目根目录
    input_file = script_dir / ".outputs" / "edge_src_structure.txt"
    output_file = script_dir / ".outputs" / "edge_src_top100_files.txt"
    
    print("Edge源码文件名统计分析工具")
    print("=" * 50)
    print(f"输入文件：{input_file}")
    print(f"输出文件：{output_file}")
    print()
    
    # 分析文件结构
    print("正在分析文件结构...")
    filename_counter, total_files = analyze_file_structure(str(input_file))
    
    if filename_counter is None:
        print("分析失败，程序退出")
        sys.exit(1)
    
    if total_files == 0:
        print("没有找到有效的文件记录")
        sys.exit(1)
    
    # 生成输出文件
    print("正在生成输出文件...")
    write_top100_files(filename_counter, total_files, str(output_file))
    
    # 显示一些统计信息
    print("\n统计摘要：")
    print("-" * 30)
    top_5 = filename_counter.most_common(5)
    for i, (filename, count) in enumerate(top_5, 1):
        percentage = (count / total_files * 100) if total_files > 0 else 0
        print(f"{i}. {filename}: {count} 次 ({percentage:.2f}%)")


if __name__ == "__main__":
    main()
