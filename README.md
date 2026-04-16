# battery-recycling-skill

动力电池回收行业专业工具。提供金属价格监控、回收价值计算、白名单企业查询等功能。

> 作者：GEM Wuhan (fengbo@gem.com.cn)

## 功能

- **价格监控**: 碳酸锂、钴、镍等关键材料价格查询
- **价值计算**: 输入电池参数，输出回收价值和采购建议
- **白名单查询**: 工信部白名单企业信息

## 安装

```bash
# 通过 skillhub 安装
skillhub install battery-recycling

# 或手动安装
git clone https://github.com/bostind/battery-recycling-skill.git
cd battery-recycling-skill
# 复制到 OpenClaw skills 目录
cp -r . ~/.openclaw/skills/battery-recycling
```

## 快速使用

### 查询当前价格
```bash
cd ~/.openclaw/skills/battery-recycling
python3 scripts/price_fetcher.py
```

### 计算回收价值
```bash
python3 scripts/value_calculator.py NCM523 320
# 参数: <电池类型> <重量kg>
# 支持的类型: NCM523, NCM622, NCM811, LFP
```

### 获取回收企业推荐
```bash
python3 scripts/recycler_recommendation.py
```

### 查询白名单企业
查看 `references/whitelist.md` 获取完整列表。

## 电池类型金属含量参考

| 类型 | 镍 | 钴 | 锰 | 锂 | 回收率 |
|------|----|----|----|----|----|
| NCM523 | 12% | 12% | 5% | 7% | 95% |
| NCM622 | 12% | 12% | 5% | 7% | 94% |
| NCM811 | 8% | 8% | 2% | 8% | 93% |
| LFP | 0% | 0% | 0% | 4.5% | 90% |

## 输出格式

所有脚本支持 `--json` 参数输出结构化数据：
```bash
python3 scripts/price_fetcher.py --json
python3 scripts/value_calculator.py NCM523 320 --json
```

## 数据源

- 价格数据：生意社、SMM（上海有色网）公开数据
- 金属含量：行业通用数据
- 白名单：工信部《新能源汽车废旧动力蓄电池综合利用行业规范条件》

## 触发词

在 OpenClaw 中可以使用以下方式触发：
- "查一下碳酸锂价格"
- "帮我算一下这批电池的回收价值"
- "现在NCM523废料多少钱"
- "动力电池回收同行业企业有哪些"

## 许可证

MIT
