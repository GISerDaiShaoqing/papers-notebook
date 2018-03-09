论文阅读笔记
这个repo主要记录平时阅读论文的一些笔记，论文包括关于GIS、地理、遥感、生态等相关方向，主要是感兴趣的方向或者是目前研究相关文章。笔记内容主要是我看文章时的想法，大致包括论文的idea，一些重要的要点和我的评价。目录按照类别进行整理,刚刚建立，内容将慢慢添加。

**目录**
[TOC]
# Urban Blue Space and Green Space

# Forest and landscape Ecology

## 1 Global patterns of tropical forest fragmentation/全球热带森林破碎化格局
**Title:** Global patterns of tropical forest fragmentation
**Link:** [原文链接](https://www.nature.com/articles/nature25508)
**Doi:** 10.1038/nature25508
**Notes：** 遥感技术能够在高分辨率上定量化热带森林砍伐

# Mapping High resolution Carbon Emission

## 1  China’s $CO_2$ emissions estimated from the bottom up: Recent trends, spatial distributions, and quantification of uncertainties/自下而上估计中国$CO_2$排放：近期趋势，空间分布与不确定性的定量化 
**Title:** China’s $CO_2$ emissions estimated from the bottom up: Recent trends, spatial distributions, and quantification of uncertainties
**Link：** [原文链接](https://www.sciencedirect.com/science/article/pii/S1352231012004761?via%3Dihub)
**Doi:** 10.1016/j.atmosenv.2012.05.027
**Notes：** 这个研究是根据经济部门、省级经济与能源详细分类的数据，构建了一个自下而上的排放清单框架估算中国人类活动的$CO_2$排放量。该研究包一个新编制采用中国最新实地调查的$CO_2$排放量数据库。节能减排政策对限制电力和钢铁厂的$CO_2$排放量作用较大，对于水泥生产没有什么影响。这篇文章是第一篇使用Monte-Carlo模拟定量化中国$CO_2$排放量的不确定性。2005年总排放量的95%置信区间为-9%~+11%。对于行业排放不确定性最大贡献的是大部分工业园的排放因子与火电厂、交通、居住与商业排放源的活动水平。方法部分考虑了（火电厂、交通、居民、工业）四个大的清单排放源，每个部分还有细分下去的各类排放源。这里先有个定义：
$$ Carbon Dioxide Emission = Acitivity Levels * Emission Factos $$
AL（Activity Levels）， EF（Emission Factors）各自有其概率分布，进行10000 次Monte-Carlo模拟分析。有精细的排放因子对照表及对应的概率分布置信区间。

Highlights:
> (1)  一个按行业确定的中国特有的$CO_2$排放因子数据库；
> (2) 基于自下而上方法估计的中国2005~2009年$CO_2$排放；
> (3) 使用Monte-Carlo模拟定量化了中国$CO_2$排放不确定性；
> (4) 提高能源效率减缓了某些行业二氧化碳排放量的增加。

Research gap/question：
全世界$CO_2$排放最多的中国在估计$CO_2$排放及不确定性上研究贫乏

Disscussion：
> (1) The difference can be attributed to the more detailed source categories in the current study, Which significantly reduce the random errors by the “compensation-of-error” mechanism realized through Monte-Carlo simulation. 数据差异的原因有可能是本研究更为精细的分类排放源，Monte-Carlo模拟中的误差补偿机制显著降低随机误差。
> (2) Use of provincial-level energy statistics in the current work is likely the primary determinant of this difference. 使用省级能源统计数据可能是差异的主要原因（前文提到省级数据比全国数据更精确）。
> (3) 政策影响和预测分析。

这篇文章主要的讨论点不是太明显，因为是把结果和讨论混在一起写到的，总体来说讨论部分除了上面我提到的两个关键点之外，就是跟IPCC等机构的数据做对比，还有对政策部分的一些预测，EF排放因子表是非常不错的数据，此外生成了一个0.25°×0.25°的产品，以人口和经济摊的。

Graph/Table Interest:

Emission Factors Table:

[]()

Uncertainty of $CO_2$

[]()

# Urban Computing and GIS

# GIS,RS and IT Technology
## 1 R Package gdistance: Distances and Routes on Geographical Grids/R包gdistance：地理格网的距离和路径
**Title:** R Package gdistance: Distances and Routes on Geographical Grids
**Link:** [原文链接](https://www.jstatsoft.org/article/view/v076i13)
**Doi:** 10.18637/jss.v076.i13
**Notes:** 