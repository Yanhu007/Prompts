#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Edge源码目录扫描器
扫描Edge源码目录并生成树状结构输出
"""

import os
import sys
import platform
from pathlib import Path
from typing import List, Tuple, Optional


class EdgeSourceScanner:
    def __init__(self):
        self.system = platform.system()
        self.edge_src_path = self._get_edge_src_path()
        self.output_dir = Path("./.outputs")
        self.output_file = self.output_dir / "edge_src_structure.txt"
        self.scanned_count = 0
        self.total_items = 0
        
    def _get_edge_src_path(self) -> Optional[Path]:
        """根据操作系统获取Edge源码路径"""
        if self.system == "Darwin":  # macOS
            path = Path("/Users/pumpedgechina/edge/src/")
        elif self.system == "Windows":
            path = Path("C:/Edge/src/")
        else:
            print(f"不支持的操作系统: {self.system}")
            return None
            
        if not path.exists():
            print(f"错误: Edge源码路径不存在: {path}")
            return None
            
        return path
    
    def _count_total_items(self, root_path: Path) -> int:
        """预先计算总项目数用于显示进度"""
        count = 0
        try:
            for root, dirs, files in os.walk(root_path):
                count += len(dirs) + len(files)
        except (PermissionError, OSError) as e:
            print(f"警告: 无法访问某些目录: {e}")
        return count
    
    def _update_progress(self):
        """更新扫描进度"""
        self.scanned_count += 1
        if self.total_items > 0:
            progress = (self.scanned_count / self.total_items) * 100
            print(f"\r扫描进度: {self.scanned_count}/{self.total_items} ({progress:.1f}%)", end="", flush=True)
    
    def _scan_directory_structure(self, root_path: Path) -> List[str]:
        """
        扫描目录结构并返回格式化的路径列表
        格式: ./src/ -> ./../子目录/ -> ./../../文件
        """
        structure_lines = []
        
        def scan_recursive(current_path: Path, relative_prefix: str = "./"):
            """递归扫描目录"""
            try:
                # 获取当前目录下的所有项目
                items = list(current_path.iterdir())
                items.sort(key=lambda x: (not x.is_dir(), x.name.lower()))
                
                # 分别处理目录和文件
                directories = [item for item in items if item.is_dir()]
                files = [item for item in items if item.is_file()]
                
                # 先添加目录
                for directory in directories:
                    dir_line = f"{relative_prefix}../{directory.name}/"
                    structure_lines.append(dir_line)
                    self._update_progress()
                    
                    # 递归扫描子目录
                    scan_recursive(directory, relative_prefix + "../")
                
                # 再添加文件
                for file in files:
                    file_line = f"{relative_prefix}../{file.name}"
                    structure_lines.append(file_line)
                    self._update_progress()
                    
            except (PermissionError, OSError) as e:
                print(f"\n警告: 无法访问目录 {current_path}: {e}")
        
        # 添加根目录
        structure_lines.append("./src/")
        
        # 开始递归扫描
        scan_recursive(root_path)
        
        return structure_lines
    
    def scan(self) -> bool:
        """执行扫描"""
        if not self.edge_src_path:
            return False
            
        print(f"开始扫描Edge源码目录: {self.edge_src_path}")
        print("正在计算总项目数...")
        
        # 计算总项目数
        self.total_items = self._count_total_items(self.edge_src_path)
        print(f"找到 {self.total_items} 个项目")
        
        # 确保输出目录存在
        self.output_dir.mkdir(exist_ok=True)
        
        print("开始扫描目录结构...")
        
        # 扫描目录结构
        structure_lines = self._scan_directory_structure(self.edge_src_path)
        
        print(f"\n扫描完成! 共处理 {self.scanned_count} 个项目")
        
        # 写入输出文件
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                for line in structure_lines:
                    f.write(line + '\n')
            print(f"目录结构已保存到: {self.output_file}")
            print(f"输出文件大小: {os.path.getsize(self.output_file)} 字节")
            return True
        except Exception as e:
            print(f"错误: 无法写入输出文件: {e}")
            return False


def main():
    """主函数"""
    print("=" * 50)
    print("Edge源码目录扫描器")
    print("=" * 50)
    
    scanner = EdgeSourceScanner()
    
    if scanner.scan():
        print("扫描任务成功完成!")
        return 0
    else:
        print("扫描任务失败!")
        return 1


if __name__ == "__main__":
    sys.exit(main())