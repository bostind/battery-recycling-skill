#!/usr/bin/env python3
"""
二轮电池（电动自行车/摩托车电池）回收价格查询
报价每月初更新
"""

import json
import sys
from datetime import datetime
from typing import Dict

# 二轮电池回收报价 (元/KG)
# 更新日期: 2026-04
EV_BATTERY_PRICES = {
    "锰酸锂": {
        "软包": 6.3,
        "方块": 6.7,
        "圆柱": 4.0,
    },
    "小三元": {
        "软包": 20.5,
        "圆柱": 12.0,
        "方块": 20.0,
    },
    "磷酸铁锂": {
        "软包": 10.0,
        "圆柱": 6.5,
        "方块": 11.5,
    },
}

LOGISTICS_FEE_PER_GROUP = 50  # 自提扣除物流费 元/组


class EVBatteryPriceMonitor:
    """二轮电池价格监控"""
    
    def get_all_prices(self) -> Dict:
        """获取所有二轮电池回收价格"""
        return {
            "update_date": "2026-04",
            "next_update": "2026-05-01",
            "note": "每月初更新报价",
            "logistics_fee": {
                "description": "若需要我方自提，需扣除",
                "amount": LOGISTICS_FEE_PER_GROUP,
                "unit": "元/组"
            },
            "prices": EV_BATTERY_PRICES
        }
    
    def calculate_value(self, chemistry: str, cell_type: str, weight_kg: float, self_pickup: bool = False) -> Dict:
        """
        计算二轮电池回收价值
        
        Args:
            chemistry: 电芯化学体系 (锰酸锂/小三元/磷酸铁锂)
            cell_type: 电芯种类 (软包/方块/圆柱)
            weight_kg: 重量 (KG)
            self_pickup: 是否自提（扣除物流费）
        """
        if chemistry not in EV_BATTERY_PRICES:
            return {"error": f"不支持的电芯化学体系: {chemistry}. 支持: {list(EV_BATTERY_PRICES.keys())}"}
        
        if cell_type not in EV_BATTERY_PRICES[chemistry]:
            return {"error": f"不支持的电芯种类: {cell_type}. 支持: {list(EV_BATTERY_PRICES[chemistry].keys())}"}
        
        unit_price = EV_BATTERY_PRICES[chemistry][cell_type]
        total_value = weight_kg * unit_price
        
        logistics_deduction = LOGISTICS_FEE_PER_GROUP if self_pickup else 0
        final_value = total_value - logistics_deduction
        
        return {
            "chemistry": chemistry,
            "cell_type": cell_type,
            "weight_kg": weight_kg,
            "unit_price": unit_price,
            "total_value": round(total_value, 2),
            "self_pickup": self_pickup,
            "logistics_deduction": logistics_deduction,
            "final_value": round(final_value, 2),
        }
    
    def print_price_table(self):
        """打印价格表"""
        print("\n" + "="*60)
        print("🔋 二轮电池（电动自行车/摩托车电池）回收报价")
        print("="*60)
        print(f"\n📅 更新日期: 2026年4月")
        print(f"📅 下次更新: 2026年5月1日")
        print(f"💡 调价方案: 每月初更新报价\n")
        
        for chemistry, types in EV_BATTERY_PRICES.items():
            print(f"\n【{chemistry}】")
            for cell_type, price in types.items():
                print(f"  {cell_type}: {price} 元/KG")
        
        print(f"\n🚚 物流说明:")
        print(f"  若需要我方自提，需扣除 {LOGISTICS_FEE_PER_GROUP} 元/组物流费用")
        print("="*60 + "\n")
    
    def print_calculation(self, result: Dict):
        """打印计算结果"""
        if "error" in result:
            print(f"❌ 错误: {result['error']}")
            return
        
        print("\n" + "="*60)
        print("🔋 二轮电池回收价值计算")
        print("="*60)
        print(f"\n电芯化学体系: {result['chemistry']}")
        print(f"电芯种类: {result['cell_type']}")
        print(f"重量: {result['weight_kg']} KG")
        print(f"单价: {result['unit_price']} 元/KG")
        print(f"\n基础价值: {result['total_value']:.2f} 元")
        
        if result['self_pickup']:
            print(f"物流扣除: -{result['logistics_deduction']} 元 (自提)")
        else:
            print(f"物流扣除: 0 元 (送货上门)")
        
        print(f"\n💰 最终价值: {result['final_value']:.2f} 元")
        print("="*60 + "\n")


if __name__ == "__main__":
    monitor = EVBatteryPriceMonitor()
    
    # 参数解析
    if len(sys.argv) == 1:
        # 无参数，打印价格表
        monitor.print_price_table()
    elif len(sys.argv) == 2 and sys.argv[1] == "--json":
        # JSON 输出价格表
        print(json.dumps(monitor.get_all_prices(), ensure_ascii=False, indent=2))
    elif len(sys.argv) >= 4:
        # 计算模式: python3 ev_battery_price.py <化学体系> <种类> <重量> [--self-pickup]
        chemistry = sys.argv[1]
        cell_type = sys.argv[2]
        weight = float(sys.argv[3])
        self_pickup = "--self-pickup" in sys.argv or "-s" in sys.argv
        
        result = monitor.calculate_value(chemistry, cell_type, weight, self_pickup)
        
        if len(sys.argv) > 4 and sys.argv[-1] == "--json":
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            monitor.print_calculation(result)
    else:
        print("用法:")
        print("  python3 ev_battery_price.py              # 查看价格表")
        print("  python3 ev_battery_price.py --json       # JSON格式价格表")
        print("  python3 ev_battery_price.py <化学体系> <种类> <重量>")
        print("  python3 ev_battery_price.py 小三元 软包 100")
        print("  python3 ev_battery_price.py 磷酸铁锂 圆柱 50 --self-pickup")
        print(f"\n支持的化学体系: {', '.join(EV_BATTERY_PRICES.keys())}")
        sys.exit(1)
