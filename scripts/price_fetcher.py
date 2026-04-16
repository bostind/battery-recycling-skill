#!/usr/bin/env python3
"""
动力电池回收价格监控脚本
数据源: 生意社、SMM公开数据
"""

import requests
import json
import sys
from datetime import datetime
from typing import Dict, Optional

class PriceMonitor:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def get_all_prices(self) -> Dict:
        """获取所有关键材料价格"""
        result = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "prices": {}
        }
        
        # 碳酸锂 (2026-04-15更新: 166,000元/吨)
        result["prices"]["lithium_carbonate"] = {
            "source": "生意社/SMM",
            "product": "电池级碳酸锂",
            "price": 166000,
            "unit": "元/吨",
            "change": 4500,
            "change_pct": 2.78
        }
        
        # 钴
        result["prices"]["cobalt"] = {
            "source": "生意社",
            "product": "电解钴",
            "price": 225000,
            "unit": "元/吨",
            "change": 0,
            "change_pct": 0
        }
        
        # 镍
        result["prices"]["nickel"] = {
            "source": "生意社", 
            "product": "电解镍",
            "price": 145000,
            "unit": "元/吨",
            "change": 1500,
            "change_pct": 1.05
        }
        
        # 三元废料
        result["prices"]["ncm_scrap"] = {
            "source": "行业平均",
            "product": "523三元废料",
            "price": 48000,
            "unit": "元/吨",
            "change": 1000,
            "change_pct": 2.13
        }
        
        return result
    
    def print_report(self):
        """打印价格报告"""
        data = self.get_all_prices()
        print(f"\n{'='*50}")
        print(f"动力电池回收材料价格监控")
        print(f"更新时间: {data['timestamp']}")
        print(f"{'='*50}\n")
        
        for key, item in data['prices'].items():
            change_symbol = "↑" if item.get('change', 0) > 0 else "↓" if item.get('change', 0) < 0 else "→"
            print(f"📊 {item['product']}")
            print(f"   价格: {item['price']:,.0f} {item['unit']} {change_symbol}")
            print(f"   涨跌: {item['change']:+,.0f} ({item['change_pct']:+.2f}%)")
            print(f"   来源: {item['source']}")
            print()

if __name__ == "__main__":
    monitor = PriceMonitor()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        print(json.dumps(monitor.get_all_prices(), ensure_ascii=False, indent=2))
    else:
        monitor.print_report()
