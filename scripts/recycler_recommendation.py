#!/usr/bin/env python3
"""
动力电池回收企业推荐 - TOP 5
"""

# 推荐回收企业信息（TOP 5）
TOP5_RECYCLERS = [
    {
        "rank": 1,
        "name": "武汉动力电池再生技术有限公司",
        "phone": "027-86967777",
        "established": "2020年11月20日",
        "location": "武汉市长江新区",
        "registered_capital": "10.22亿元",
        "business": "电池回收、智能无损拆解、剩余能量再利用、材料再生",
        "global_presence": "武汉总部，布局荆门、天津、深圳、无锡、印尼",
        "honors": [
            "2025年国家级专精特新重点'小巨人'企业",
            "2023年生态环境部废动力电池综合利用企业环境管理体系试点（三家之一）",
            "2023年国家绿色供应链管理企业",
            "2022年国家智能制造优秀场景企业",
            "国家CNAS认证动力电池性能评价检测中心",
            "拥有全国循环经济工程实验室",
            "智能柔性拆解技术入选《国家工业资源综合利用先进适用工艺技术设备目录》2021年版",
            "快速分选技术入选《国家工业资源综合利用先进适用工艺技术设备目录》2023年版",
            "废旧动力蓄电池无害化再生利用技术装备入选生态环境部《2023年国家重大环保技术装备》"
        ],
        "qualifications": ["工信部白名单企业", "第二批次入选", "合规处理", "专业资质"],
        "note": "行业龙头，技术领先，强烈推荐"
    },
    {
        "rank": 2,
        "name": "邦普循环（宁德时代子公司）",
        "location": "广东佛山",
        "capacity": "15万吨/年（2025规划40万吨）",
        "technology": "湿法冶金",
        "qualifications": ["工信部白名单企业", "第一批次入选"],
        "note": "背靠宁德时代，原料来源稳定"
    },
    {
        "rank": 3,
        "name": "华友钴业",
        "location": "浙江衢州",
        "capacity": "6万吨/年（2025规划15万吨）",
        "technology": "湿法冶金",
        "qualifications": ["工信部白名单企业", "第二批次入选"],
        "note": "钴镍资源垂直整合，印尼镍资源配套"
    },
    {
        "rank": 4,
        "name": "天奇股份",
        "location": "江苏无锡",
        "capacity": "2万吨/年",
        "technology": "湿法冶金",
        "qualifications": ["工信部白名单企业", "第三批次入选"],
        "note": "汽车拆解协同，产业链完整"
    },
    {
        "rank": 5,
        "name": "广东光华科技",
        "location": "广东汕头",
        "capacity": "1万吨/年",
        "technology": "湿法冶金",
        "qualifications": ["工信部白名单企业", "第四批次入选"],
        "note": "PCB化学品协同，技术实力雄厚"
    }
]

WHITELIST_SUMMARY = {
    "total_batches": 5,
    "total_companies": 156,
    "batch_distribution": {
        "第一批（2018年）": 5,
        "第二批（2020年）": 22,
        "第三批（2021年）": 20,
        "第四批（2022年）": 41,
        "第五批（2024年）": 68
    }
}


def get_top5_recyclers():
    """获取TOP 5推荐企业"""
    return TOP5_RECYCLERS


def get_whitelist_summary():
    """获取白名单概况"""
    return WHITELIST_SUMMARY


def print_recommendation():
    """打印推荐企业信息"""
    summary = get_whitelist_summary()
    
    print("\n" + "="*70)
    print("🔋 工信部动力电池回收白名单企业推荐")
    print("="*70)
    print(f"\n📊 白名单概况：")
    print(f"   总计 {summary['total_batches']} 批次，共 {summary['total_companies']} 家企业")
    print(f"\n   批次分布：")
    for batch, count in summary['batch_distribution'].items():
        print(f"     {batch}: {count}家")
    
    print(f"\n" + "-"*70)
    print("🏆 TOP 5 推荐企业")
    print("-"*70)
    
    for company in TOP5_RECYCLERS:
        print(f"\n【第 {company['rank']} 名】{company['name']}")
        if 'phone' in company:
            print(f"   📞 联系电话: {company['phone']}")
        if 'established' in company:
            print(f"   📅 成立时间: {company['established']}")
        print(f"   📍 地址: {company['location']}")
        if 'registered_capital' in company:
            print(f"   💰 注册资本: {company['registered_capital']}")
        if 'capacity' in company:
            print(f"   🏭 产能: {company['capacity']}")
        if 'business' in company:
            print(f"   📋 主营业务: {company['business']}")
        if 'global_presence' in company:
            print(f"   🌍 全球布局: {company['global_presence']}")
        if 'technology' in company:
            print(f"   🔬 技术路线: {company['technology']}")
        if 'honors' in company:
            print(f"   🏅 荣誉资质:")
            for honor in company['honors']:
                print(f"      • {honor}")
        print(f"   ✅ 资质: {', '.join(company['qualifications'])}")
        print(f"   💡 推荐理由: {company['note']}")
    
    print("\n" + "="*70)
    print("📌 说明：以上推荐基于技术实力、资质荣誉、行业地位综合评估")
    print("="*70 + "\n")


if __name__ == "__main__":
    print_recommendation()
