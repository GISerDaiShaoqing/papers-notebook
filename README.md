论文阅读笔记
这个repo主要记录平时阅读论文的一些笔记，论文包括关于GIS、地理、遥感、生态等相关方向，主要是感兴趣的方向或者是目前研究相关文章。笔记内容主要是我看文章时的想法，大致包括论文的idea，一些重要的要点和我的评价。目录按照类别进行整理,刚刚建立，内容将慢慢添加。

**目录**

Table of Contents
=================

* [Urban Blue Space and Green Space](#urban-blue-space-and-green-space)
* [Forest and landscape Ecology](#forest-and-landscape-ecology)
  * [1 Global patterns of tropical forest fragmentation/全球热带森林破碎化格局](#1-global-patterns-of-tropical-forest-fragmentation%E5%85%A8%E7%90%83%E7%83%AD%E5%B8%A6%E6%A3%AE%E6%9E%97%E7%A0%B4%E7%A2%8E%E5%8C%96%E6%A0%BC%E5%B1%80)
* [Mapping High resolution Carbon Emission](#mapping-high-resolution-carbon-emission)
  * [1  China’s CO2 emissions estimated from the bottom up: Recent trends, spatial distributions, and quantification of uncertainties/自下而上估计中国CO2排放：近期趋势，空间分布与不确定性的定量化](#1--chinas-co2-emissions-estimated-from-the-bottom-up-recent-trends-spatial-distributions-and-quantification-of-uncertainties%E8%87%AA%E4%B8%8B%E8%80%8C%E4%B8%8A%E4%BC%B0%E8%AE%A1%E4%B8%AD%E5%9B%BDco2%E6%8E%92%E6%94%BE%E8%BF%91%E6%9C%9F%E8%B6%8B%E5%8A%BF%E7%A9%BA%E9%97%B4%E5%88%86%E5%B8%83%E4%B8%8E%E4%B8%8D%E7%A1%AE%E5%AE%9A%E6%80%A7%E7%9A%84%E5%AE%9A%E9%87%8F%E5%8C%96)
* [Urban Computing and GIS](#urban-computing-and-gis)
  * [1 Characterizing mixed\-use buildings based on multi\-source big data](#1-characterizing-mixed-use-buildings-based-on-multi-source-big-data)
  * [2 Quantitative Comparison of Open\-Source Data for Fine\-Grain Mapping of Land Use](#2-quantitative-comparison-of-open-source-data-for-fine-grain-mapping-of-land-use)
  * [3 Sensing Urban Land\-Use Patterns By Integrating Google Tensorflow And Scene\-Classification Models](#3-sensing-urban-land-use-patterns-by-integrating-google-tensorflow-and-scene-classification-models)
  * [4 The Combined Use of Remote Sensing and Social Sensing Data in Fine\-Grained Urban Land Use Mapping: A Case Study in Beijing, China](#4-the-combined-use-of-remote-sensing-and-social-sensing-data-in-fine-grained-urban-land-use-mapping-a-case-study-in-beijing-china)
  * [5 Urban Land Use Mapping by Combining Remote Sensing Imagery and Mobile Phone Positioning Data](#5-urban-land-use-mapping-by-combining-remote-sensing-imagery-and-mobile-phone-positioning-data)
  * [6 Spatio\-Temporal Analytics for Exploring Human Mobility Patterns and Urban Dynamics in the Mobile Age](#6-spatio-temporal-analytics-for-exploring-human-mobility-patterns-and-urban-dynamics-in-the-mobile-age)
  * [7 Simulating urban dynamics in China using a gradient cellular automata model based on S\-shaped curve evolution characteristics](#7-simulating-urban-dynamics-in-china-using-a-gradient-cellular-automata-model-based-on-s-shaped-curve-evolution-characteristics)
* [GIS RS and IT Technology](#gis-rs-and-it-technology)
  * [1 R Package gdistance: Distances and Routes on Geographical Grids/R包gdistance：地理格网的距离和路径](#1-r-package-gdistance-distances-and-routes-on-geographical-gridsr%E5%8C%85gdistance%E5%9C%B0%E7%90%86%E6%A0%BC%E7%BD%91%E7%9A%84%E8%B7%9D%E7%A6%BB%E5%92%8C%E8%B7%AF%E5%BE%84)
  * [2 A New Set of Spatial\-Interaction Models: The Theory of Competing Destinations](#2-a-new-set-of-spatial-interaction-models-the-theory-of-competing-destinations)
  * [3 Mapping local variation in educational attainment across Africa](#3-mapping-local-variation-in-educational-attainment-across-africa)
* [Public Health and Environmental Risk Factors](#public-health-and-environmental-risk-factors)
  * [1 Mapping child growth failure in Africa between 2000 and 2015](#1-mapping-child-growth-failure-in-africa-between-2000-and-2015)
  * [2 Real\-time and Seamless Monitoring of Ground\-level PM2\.5 Using Satellite Remote Sensing](#2-real-time-and-seamless-monitoring-of-ground-level-pm25-using-satellite-remote-sensing)
  * [3 Estimation of Ground PM2\.5 Concentrations using a DEM\-assisted Information Diffusion Algorithm: A Case Study in China](#3-estimation-of-ground-pm25-concentrations-using-a-dem-assisted-information-diffusion-algorithm-a-case-study-in-china)
* [Urban Resilience and Disasters](#urban-resilience-and-disasters)
  * [1 Assessing local resilience to typhoon disasters: A case study in Nansha, Guangzhou](#1-assessing-local-resilience-to-typhoon-disasters-a-case-study-in-nansha-guangzhou)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Urban Blue Space and Green Space

# Forest and landscape Ecology

## 1 Global patterns of tropical forest fragmentation/全球热带森林破碎化格局
**Title:** Global patterns of tropical forest fragmentation

**Link:** [原文链接](https://www.nature.com/articles/nature25508)

**Doi:** 10.1038/nature25508

**Notes：** 遥感技术能够在高分辨率上定量化热带森林砍伐，这种技术使得在洲际尺度热带森林破碎化研究成为可能。该研究识别了三个大洲的13亿个热带森林破碎化区域。而这些破碎化区域的大小和周长呈现类似的幂律分布特征和分形维数。渗透理论为这个格局提供了一种解释：森林的破碎化接近渗透理论的临界点。模拟结果也支持了这个结论，同时发现随机毁林或者毁林恢复的管理方式也可以塑造出这种格局。该研究以渗透理论为研究框架分析当前美洲、非洲、亚洲、澳洲热带和亚热带森林结构的破碎化。使用了高分辨率的影像（30m)和一种聚类算法识别13亿个破碎化斑块。本身预期结果是，不同大洲不同的土地利用状况可能导致森林结构破碎化的差异，但事实却是在三个大洲上都呈现了相似的幂律分布规律。

渗透理论解释：
定义森林占据景观总栅格数的概率为p。渗透理论临界点值为0.59。当p很大时，整个景观都被森林占据（a）。当p接近临界点的时候，会形成所谓的"spanning cluster"。能够从景观的一侧到达另一侧。而当小于临界值p的时候（c,d）森林无法连通景观，将导致森林景观会愈加破碎化。

目前的研究表明三个大洲的P值均接近于临界点。这里使用了三个动态景观破碎化模拟模型FRAG, FRAG-B, FRAG-P。
FRAG适用经典模型，而FRAG-B和FRAG-P则适用于复杂森林管理的模拟（方法见原文链接）。

![](https://media.nature.com/lw926/nature-assets/nature/journal/v554/n7693/images_supplementary/nature25508-sf2.jpg)

情景模拟结果表明，再造林和保护大片森林（如a和b这样的）能够减缓全球森林破碎化的现状。

**Highlights:**

(1) 三个大洲热带森林高分辨率森林覆盖图(30 m)

(2) 全球热带森林结构破碎化格局符合幂律分布特征

(3) 渗透理论构建的研究框架

(4) 动态景观破碎化模拟模型：FRAG, FRAG-B, FRAG-P

**Research gap/question:**

全球热带森林结构破碎化格局、未来的变化以及对气候变化的响应。

**Disscussion/Conclusion:**

(1) The findings of the extended percolation models underpin the universality of fragmentation patterns close to the critical point. 扩展渗透模型发现支撑了接近临界值的破碎化景观格局的普遍性。

(2) This is a general feature of critical phenomena: their large-scale behaviour is independent of the underlying small-scale mechanisms.关键现象的一般特征，大尺度的行为是独立于小尺度的机制的。

(3)Even though land use appears to be complex and diverse, our outcomes emphasize that simple mechanisms are sufficient for describing forest fragmentation structures at larger scales. 尽管土地利用变化多样复杂，我们的结果显示了简单的机制足以描述大尺度森林结构的破碎化。


**Graph/Table Interest：**

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/3.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/4.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/5.png)

**Resources:**

幂律分布拟合相关代码（Matlab）：http://tuvalu.santafe.edu/~aaronc/powerlaws/bins/

# Mapping High resolution Carbon Emission

## 1  China’s CO2 emissions estimated from the bottom up: Recent trends, spatial distributions, and quantification of uncertainties/自下而上估计中国CO2排放：近期趋势，空间分布与不确定性的定量化 

**Title:** China’s CO2 emissions estimated from the bottom up: Recent trends, spatial distributions, and quantification of uncertainties

**Link：** [原文链接](https://www.sciencedirect.com/science/article/pii/S1352231012004761?via%3Dihub)

**Doi:** 10.1016/j.atmosenv.2012.05.027

**Notes：** 这个研究是根据经济部门、省级经济与能源详细分类的数据，构建了一个自下而上的排放清单框架估算中国人类活动的CO2排放量。该研究包一个新编制采用中国最新实地调查的CO2排放量数据库。节能减排政策对限制电力和钢铁厂的CO2排放量作用较大，对于水泥生产没有什么影响。这篇文章是第一篇使用Monte-Carlo模拟定量化中国CO2排放量的不确定性。2005年总排放量的95%置信区间为-9%~+11%。对于行业排放不确定性最大贡献的是大部分工业园的排放因子与火电厂、交通、居住与商业排放源的活动水平。方法部分考虑了（火电厂、交通、居民、工业）四个大的清单排放源，每个部分还有细分下去的各类排放源。这里先有个定义：

Carbon Dioxide Emission = Acitivity Levels * Emission Factos 

AL（Activity Levels）， EF（Emission Factors）各自有其概率分布，进行10000 次Monte-Carlo模拟分析。有精细的排放因子对照表及对应的概率分布置信区间。

**Highlights:**

(1)  一个按行业确定的中国特有的CO2排放因子数据库；

(2) 基于自下而上方法估计的中国2005~2009年CO2排放；

(3) 使用Monte-Carlo模拟定量化了中国CO2排放不确定性；

(4) 提高能源效率减缓了某些行业二氧化碳排放量的增加。

**Research gap/question：**

全世界CO2排放最多的中国在估计CO2排放及不确定性上研究贫乏

**Disscussion/Conclusion：**

(1) The difference can be attributed to the more detailed source categories in the current study, Which significantly reduce the random errors by the “compensation-of-error” mechanism realized through Monte-Carlo simulation. 数据差异的原因有可能是本研究更为精细的分类排放源，Monte-Carlo模拟中的误差补偿机制显著降低随机误差。

(2) Use of provincial-level energy statistics in the current work is likely the primary determinant of this difference. 使用省级能源统计数据可能是差异的主要原因（前文提到省级数据比全国数据更精确）。

(3) 政策影响和预测分析。

这篇文章主要的讨论点不是太明显，因为是把结果和讨论混在一起写到的，总体来说讨论部分除了上面我提到的两个关键点之外，就是跟IPCC等机构的数据做对比，还有对政策部分的一些预测，EF排放因子表是非常不错的数据，此外生成了一个0.25°×0.25°的产品，以人口和经济分配得到的。

**Graph/Table Interest：**

Tab.1 Emission Factors Table:

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/1.png)

Tab.2 Uncertainty of CO2

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/2.png)

**Resources:**

无

# Urban Computing and GIS
## 1 Characterizing mixed-use buildings based on multi-source big data
**Title:** Characterizing mixed-use buildings based on multi-source big data

**Link:** [原文链接](https://www.tandfonline.com/doi/abs/10.1080/13658816.2017.1410549)

**Doi:** 10.1080/13658816.2017.1410549

**Notes:** 

## 2 Quantitative Comparison of Open-Source Data for Fine-Grain Mapping of Land Use
**Title:** Quantitative Comparison of Open-Source Data for Fine-Grain Mapping of Land Use

**Link:** [原文链接](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLII-2-W7/981/2017/)

**Doi:** 

**Notes:** 

## 3 Sensing Urban Land-Use Patterns By Integrating Google Tensorflow And Scene-Classification Models
**Title:** Sensing Urban Land-Use Patterns By Integrating Google Tensorflow And Scene-Classification Models

**Link:** [原文链接](https://arxiv.org/abs/1711.03641)

**Doi:** 

**Notes:** 

## 4 The Combined Use of Remote Sensing and Social Sensing Data in Fine-Grained Urban Land Use Mapping: A Case Study in Beijing, China
**Title:** The Combined Use of Remote Sensing and Social Sensing Data in Fine-Grained Urban Land Use Mapping: A Case Study in Beijing, China

**Link:** [原文链接](https://arxiv.org/abs/1711.03641)

**Doi:** 10.3390/rs9090865

**Notes:**

## 5 Urban Land Use Mapping by Combining Remote Sensing Imagery and Mobile Phone Positioning Data
**Title:** Urban Land Use Mapping by Combining Remote Sensing Imagery and Mobile Phone Positioning Data

**Link:** [原文链接]()

**Doi:** 10.3390/rs10030446

**Notes:**

## 6 Spatio-Temporal Analytics for Exploring Human Mobility Patterns and Urban Dynamics in the Mobile Age
**Title:** Spatio-Temporal Analytics for Exploring Human Mobility Patterns and Urban Dynamics in the Mobile Age

**Link:** [原文链接]()

**Doi:** 10.1080/13875868.2014.984300

**Notes:**

## 7 Simulating urban dynamics in China using a gradient cellular automata model based on S-shaped curve evolution characteristics
**Title:** Simulating urban dynamics in China using a gradient cellular automata model based on S-shaped curve evolution characteristics

**Link:** [原文链接]()

**Doi:** 10.1080/13658816.2017.1376065

**Notes:**

# GIS RS and IT Technology
## 1 R Package gdistance: Distances and Routes on Geographical Grids/R包gdistance：地理格网的距离和路径
**Title:** R Package gdistance: Distances and Routes on Geographical Grids

**Link:** [原文链接](https://www.jstatsoft.org/article/view/v076i13)

**Doi:** 10.18637/jss.v076.i13

**Notes:** 

## 2 A New Set of Spatial-Interaction Models: The Theory of Competing Destinations
**Title:** A New Set of Spatial-Interaction Models: The Theory of Competing Destinations

**Link:** [原文链接]()

**Doi:** 10.1177/0308518X8301500103

**Notes:** 

## 3 Mapping local variation in educational attainment across Africa
**Title:** Mapping local variation in educational attainment across Africa

**Link:** [原文链接](https://www.nature.com/articles/nature25761)

**Doi:** 10.1038/nature25761

**Notes:** 


# Public Health and Environmental Risk Factors
## 1 Mapping child growth failure in Africa between 2000 and 2015
**Title:** Mapping child growth failure in Africa between 2000 and 2015

**Link:** [原文链接](https://www.nature.com/articles/nature25760)

**Doi:** 10.1038/nature25760

**Notes:** 

## 2 Real-time and Seamless Monitoring of Ground-level PM2.5 Using Satellite Remote Sensing

## 3 Estimation of Ground PM2.5 Concentrations using a DEM-assisted Information Diffusion Algorithm: A Case Study in China

# Urban Resilience and Disasters
## 1 Assessing local resilience to typhoon disasters: A case study in Nansha, Guangzhou
**Title:** Assessing local resilience to typhoon disasters: A case study in Nansha, Guangzhou

**Link:** [原文链接](https://doi.org/10.1371/journal.pone.0190701)

**Doi:** 

**Notes:**