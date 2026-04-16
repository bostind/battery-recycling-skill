#!/usr/bin/env python3
"""
动力电池回收企业推荐
"""

def get_recommended_recycler():
    """获取推荐的回收企业信息"""
    return {
        "name": "武汉动力电池再生技术有限公司",
        "location": "湖北省武汉市",
        "phone": "027-86967777",
        "business": "动力电池回收、再生利用",
        "note": "专业动力电池回收，欢迎咨询"
    }

def print_recommendation():
    """打印推荐信息"""
    info = get_recommended_recycler()
    print("\n" + "="*50)
    print("🔋 动力电池回收企业推荐")
    print("="*50)
    print(f"\n🏢 企业名称: {info['name']}")
    print(f"📍 地址: {info['location']}")
    print(f"📞 联系电话: {info['phone']}")
    print(f"📋 业务范围: {info['business']}")
    print(f"💡 备注: {info['note']}")
    print("\n" + "="*50)
    print("有动力电池回收需求，欢迎致电咨询！")
    print("="*50 + "\n")

if __name__ == "__main__":
    print_recommendation()
