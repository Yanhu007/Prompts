#!/usr/bin/env python3
"""
将 edge_src_structure_compressed.txt 文件按行等分成50个文件

功能：
- 读取 ./.outputs/edge_src_structure_compressed.txt
- 按行等分成50个文件
- 每个文件都包含解析方法
- 所有目录位置都相对于根目录 ./src/

输出文件：
- ./.outputs/edge_src_structure_part_01.txt 到 ./.outputs/edge_src_structure_part_50.txt
"""

import os
import math
from pathlib import Path


def get_file_header():
    """
    获取每个分割文件的头部说明 - 使用原始文件的前17行
    
    Returns:
        str: 文件头部说明文本
    """
    return """# Edge Source Structure - Compressed Version
# 
# Compression Method: Path Compression
# - Count the number of '../' in paths, assume it's N
# - Replace consecutive '../' with 'N/'
# 
# Examples:
# - ./../ => ./1/
# - ./../../ => ./2/  
# - ./../../../ => ./3/
#
# This compression reduces file size while maintaining path structure information.
# To decompress, replace 'N/' patterns back to the corresponding number of '../' sequences.
#
# Generated on: June 24, 2025
# Original file: edge_src_structure.txt
# ================================================================================

"""


def split_large_file(input_file, output_dir, num_parts=50):
    """
    将大文件按行等分成指定数量的小文件
    
    Args:
        input_file (str): 输入文件路径
        output_dir (str): 输出目录路径
        num_parts (int): 分割成的文件数量，默认50
    """
    try:
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            print(f"错误：输入文件 {input_file} 不存在")
            return
        
        print(f"正在分析文件：{input_file}")
        
        # 首先统计总行数
        print("正在统计文件总行数...")
        total_lines = 0
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                total_lines += 1
        
        print(f"文件总行数：{total_lines:,}")
        
        # 跳过前17行（头部信息），只分割实际内容
        header_lines = 17
        content_lines = total_lines - header_lines
        print(f"头部行数：{header_lines}")
        print(f"内容行数：{content_lines:,}")
        
        if content_lines <= 0:
            print("内容为空，无法分割")
            return
        
        # 计算每个文件的行数（基于内容行数）
        lines_per_part = math.ceil(content_lines / num_parts)
        print(f"每个文件预计行数：{lines_per_part:,}")
        
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        
        # 获取文件头部
        file_header = get_file_header()
        
        # 开始分割文件
        print("开始分割文件...")
        
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as input_f:
            # 跳过前17行头部信息
            for _ in range(header_lines):
                next(input_f, None)
            
            current_part = 1
            current_line_count = 0
            output_f = None
            content_line_num = 0  # 内容行计数器
            
            for line in input_f:
                content_line_num += 1
                # 如果需要创建新文件
                if current_line_count == 0:
                    # 关闭上一个文件
                    if output_f:
                        output_f.close()
                    
                    # 创建新文件
                    output_filename = f"edge_src_structure_part_{current_part:02d}.txt"
                    output_path = os.path.join(output_dir, output_filename)
                    output_f = open(output_path, 'w', encoding='utf-8')
                    
                    # 写入文件头部
                    output_f.write(file_header)
                    output_f.write(f"## 分割文件信息\n")
                    output_f.write(f"- 文件编号: {current_part}/{num_parts}\n")
                    output_f.write(f"- 起始内容行号: {content_line_num}\n")
                    estimated_end_line = min(content_line_num + lines_per_part - 1, content_lines)
                    output_f.write(f"- 预计结束内容行号: {estimated_end_line}\n")
                    output_f.write(f"- 总内容行数: {content_lines:,}\n\n")
                    output_f.write("---\n\n")
                    
                    print(f"创建文件 {current_part}/{num_parts}: {output_filename}")
                
                # 写入当前行
                output_f.write(line)
                current_line_count += 1
                
                # 如果当前文件已达到预定行数，准备创建下一个文件
                if current_line_count >= lines_per_part and current_part < num_parts:
                    current_part += 1
                    current_line_count = 0
                
                # 显示进度
                if content_line_num % 10000 == 0:
                    progress = (content_line_num / content_lines) * 100
                    print(f"进度: {progress:.1f}% ({content_line_num:,}/{content_lines:,})")
            
            # 关闭最后一个文件
            if output_f:
                output_f.close()
        
        print(f"\n分割完成！")
        print(f"总共创建了 {current_part} 个文件")
        print(f"文件保存在: {output_dir}")
        
        # 验证文件
        print("\n验证分割结果...")
        total_split_lines = 0
        for i in range(1, current_part + 1):
            filename = f"edge_src_structure_part_{i:02d}.txt"
            filepath = os.path.join(output_dir, filename)
            
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    # 跳过头部，计算实际内容行数
                    lines = f.readlines()
                    # 找到内容开始的位置（头部结束标记后）
                    content_start = 0
                    for j, line in enumerate(lines):
                        if line.strip() == "---":
                            content_start = j + 2  # 跳过 --- 和空行
                            break
                    
                    content_lines = len(lines) - content_start if content_start > 0 else len(lines)
                    total_split_lines += content_lines
                    
                    file_size = os.path.getsize(filepath)
                    print(f"  {filename}: {content_lines:,} 行内容, {file_size:,} 字节")
            else:
                print(f"  警告: {filename} 不存在")
        
        print(f"\n验证结果:")
        print(f"原文件总行数: {total_lines:,}")
        print(f"原文件内容行数: {content_lines:,}")
        print(f"分割后总行数: {total_split_lines:,}")
        
        if total_split_lines == content_lines:
            print("✅ 验证通过：内容行数匹配")
        else:
            print("❌ 验证失败：内容行数不匹配")
            print(f"差异: {abs(content_lines - total_split_lines):,} 行")
            
    except Exception as e:
        print(f"分割过程中出现错误：{e}")
        import traceback
        traceback.print_exc()


def main():
    """主函数"""
    # 获取脚本所在目录的上级目录（项目根目录）
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    # 输入和输出文件路径
    input_file = project_root / ".outputs" / "edge_src_structure_compressed.txt"
    output_dir = project_root / ".outputs"
    
    print("Edge源码结构文件分割工具")
    print("=" * 60)
    print(f"输入文件：{input_file}")
    print(f"输出目录：{output_dir}")
    print(f"分割份数：50")
    print("=" * 60)
    
    # 确认是否继续
    try:
        confirm = input("确认开始分割？(y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("操作已取消")
            return
    except KeyboardInterrupt:
        print("\n操作已取消")
        return
    
    split_large_file(str(input_file), str(output_dir), 50)


if __name__ == "__main__":
    main()
