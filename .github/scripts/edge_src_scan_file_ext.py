#!/usr/bin/env python3
"""
分析 edge_src_structure.txt 文件中的文件扩展名统计

功能：
- 读取 ./.outputs/edge_src_structure.txt
- 按文件名后缀计数
- 按降序输出到 ./.outputs/edge_src_file_exts.txt

后缀规则：
- xx.ext -> 后缀名为.ext
- xx -> 无后缀名
- .xx.ext -> 后缀名为.ext  
- .xx -> 无后缀名
"""

import os
import re
from collections import Counter
from pathlib import Path


def extract_file_extension(filename):
    """
    根据规则提取文件扩展名
    
    Args:
        filename (str): 文件名
        
    Returns:
        str: 扩展名（包含点号）或 "无后缀名"
    """
    # 移除路径，只保留文件名
    basename = os.path.basename(filename.strip())
    
    # 如果是空字符串或只有路径分隔符，跳过
    if not basename or basename in ['/', '\\', '.', '..']:
        return None
    
    # 如果以点开头，去掉开头的点
    if basename.startswith('.'):
        basename = basename[1:]
        # 如果去掉点后为空，说明只是一个隐藏文件名，无扩展名
        if not basename:
            return "无后缀名"
    
    # 查找最后一个点的位置
    last_dot_index = basename.rfind('.')
    
    # 如果没有点或点在开头，则无扩展名
    if last_dot_index == -1 or last_dot_index == 0:
        return "无后缀名"
    
    # 提取扩展名（包含点号）
    extension = basename[last_dot_index:]
    return extension


def analyze_file_extensions(input_file, output_file):
    """
    分析文件扩展名并输出统计结果
    
    Args:
        input_file (str): 输入文件路径
        output_file (str): 输出文件路径
    """
    try:
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            print(f"错误：输入文件 {input_file} 不存在")
            return
        
        print(f"正在分析文件：{input_file}")
        
        # 存储所有文件扩展名
        extensions = []
        total_files = 0
        
        # 读取文件并提取扩展名
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                # 跳过空行
                line = line.strip()
                if not line:
                    continue
                
                # 尝试提取文件名（可能包含路径）
                # 假设文件结构是树状结构，包含文件路径
                # 匹配各种可能的文件路径格式
                
                # 移除可能的树状结构字符
                cleaned_line = re.sub(r'^[├└│\s\-\+\*]*', '', line)
                cleaned_line = cleaned_line.strip()
                
                # 如果行中包含文件路径分隔符，提取最后一部分作为文件名
                if '/' in cleaned_line or '\\' in cleaned_line:
                    # 这可能是一个完整路径
                    filename = os.path.basename(cleaned_line)
                else:
                    filename = cleaned_line
                
                # 跳过明显的目录（以/结尾）或空字符串
                if not filename or filename.endswith('/') or filename.endswith('\\'):
                    continue
                
                # 跳过可能的目录名（没有扩展名且常见的目录名）
                common_dirs = {
                    'src', 'lib', 'test', 'tests', 'docs', 'doc', 'bin', 'build', 
                    'dist', 'node_modules', 'vendor', 'target', 'out', 'output',
                    'static', 'public', 'assets', 'resources', 'config', 'conf'
                }
                
                if filename.lower() in common_dirs:
                    continue
                
                # 提取扩展名
                ext = extract_file_extension(filename)
                if ext is not None:
                    extensions.append(ext)
                    total_files += 1
                
                # 每处理1000行输出一次进度
                if line_num % 1000 == 0:
                    print(f"已处理 {line_num} 行，找到 {total_files} 个文件...")
        
        print(f"总共找到 {total_files} 个文件")
        
        if total_files == 0:
            print("未找到任何文件，请检查输入文件格式")
            return
        
        # 统计扩展名
        ext_counter = Counter(extensions)
        
        # 创建输出目录
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # 输出结果到文件
        with open(output_file, 'w', encoding='utf-8') as f:
            # 写入表头
            f.write("扩展名,数量,占总文件数百分比\n")
            
            # 按数量降序排序并写入
            for ext, count in ext_counter.most_common():
                percentage = (count / total_files) * 100
                f.write(f"{ext},{count},{percentage:.2f}%\n")
        
        print(f"分析完成！结果已保存到：{output_file}")
        
        # 输出前10个最常见的扩展名
        print("\n前10个最常见的文件扩展名：")
        print("扩展名\t\t数量\t百分比")
        print("-" * 40)
        for ext, count in ext_counter.most_common(10):
            percentage = (count / total_files) * 100
            print(f"{ext:<15}\t{count}\t{percentage:.2f}%")
            
    except Exception as e:
        print(f"分析过程中出现错误：{e}")


def main():
    """主函数"""
    # 获取脚本所在目录的上级目录（项目根目录）
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    # 输入和输出文件路径
    input_file = project_root / ".outputs" / "edge_src_structure.txt"
    output_file = project_root / ".outputs" / "edge_src_file_exts.txt"
    
    print("Edge源码文件扩展名分析工具")
    print("=" * 50)
    print(f"输入文件：{input_file}")
    print(f"输出文件：{output_file}")
    print("=" * 50)
    
    analyze_file_extensions(str(input_file), str(output_file))


if __name__ == "__main__":
    main()
