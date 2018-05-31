论文阅读笔记
这个repo主要记录平时阅读论文的一些笔记，论文包括关于GIS、地理、遥感、生态等相关方向，主要是感兴趣的方向或者是目前研究相关文章。笔记内容主要是我看文章时的想法，大致包括论文的idea，一些重要的要点和我的评价。目录按照类别进行整理,刚刚建立，内容将慢慢添加。

**目录**
Table of Contents
=================

* [Urban Blue Space and Green Space](#urban-blue-space-and-green-space)
  * [1 Dynamic assessments of population exposure to urban greenspace using multi\-source big data](#1-dynamic-assessments-of-population-exposure-to-urban-greenspace-using-multi-source-big-data)
* [Forest and Landscape Ecology](#forest-and-landscape-ecology)
  * [1 Global patterns of tropical forest fragmentation](#1-global-patterns-of-tropical-forest-fragmentation)
  * [2 Mapping Ecosystem Service Bundles to Detect Distinct Types of Multifunctionality within the Diverse Landscape of the Yangtze River Basin, China](#2-mapping-ecosystem-service-bundles-to-detect-distinct-types-of-multifunctionality-within-the-diverse-landscape-of-the-yangtze-river-basin-china)
* [Data Assimilation](#data-assimilation)
  * [1 A simplified data assimilation method for reconstructing time\-series MODIS NDVI data](#1-a-simplified-data-assimilation-method-for-reconstructing-time-series-modis-ndvi-data)
* [Mapping High Resolution Carbon Emission](#mapping-high-resolution-carbon-emission)
  * [1  China’s CO2 emissions estimated from the bottom up: Recent trends, spatial distributions, and quantification of uncertainties](#1--chinas-co2-emissions-estimated-from-the-bottom-up-recent-trends-spatial-distributions-and-quantification-of-uncertainties)
  * [2 Effect of Urbanization on Carbon Dioxide Emissions Efficiency in the Yangtze River Delta, China](#2-effect-of-urbanization-on-carbon-dioxide-emissions-efficiency-in-the-yangtze-river-delta-china)
* [Urban Computing and GIS](#urban-computing-and-gis)
  * [1 Characterizing mixed\-use buildings based on multi\-source big data](#1-characterizing-mixed-use-buildings-based-on-multi-source-big-data)
  * [2 Quantitative Comparison of Open\-Source Data for Fine\-Grain Mapping of Land Use](#2-quantitative-comparison-of-open-source-data-for-fine-grain-mapping-of-land-use)
  * [3 Sensing Urban Land\-Use Patterns By Integrating Google Tensorflow And Scene\-Classification Models](#3-sensing-urban-land-use-patterns-by-integrating-google-tensorflow-and-scene-classification-models)
  * [4 The Combined Use of Remote Sensing and Social Sensing Data in Fine\-Grained Urban Land Use Mapping: A Case Study in Beijing, China](#4-the-combined-use-of-remote-sensing-and-social-sensing-data-in-fine-grained-urban-land-use-mapping-a-case-study-in-beijing-china)
  * [5 Urban Land Use Mapping by Combining Remote Sensing Imagery and Mobile Phone Positioning Data](#5-urban-land-use-mapping-by-combining-remote-sensing-imagery-and-mobile-phone-positioning-data)
  * [6 Spatio\-Temporal Analytics for Exploring Human Mobility Patterns and Urban Dynamics in the Mobile Age](#6-spatio-temporal-analytics-for-exploring-human-mobility-patterns-and-urban-dynamics-in-the-mobile-age)
  * [7 Simulating urban dynamics in China using a gradient cellular automata model based on S\-shaped curve evolution characteristics](#7-simulating-urban-dynamics-in-china-using-a-gradient-cellular-automata-model-based-on-s-shaped-curve-evolution-characteristics)
  * [8 Identifying Local Spatiotemporal Autocorrelation Patterns of Taxi Pick\-ups and Dropoffs](#8-identifying-local-spatiotemporal-autocorrelation-patterns-of-taxi-pick-ups-and-dropoffs)
  * [9 Challenges and Prospects of Uncertainties in Spatial Big Data Analytics](#9-challenges-and-prospects-of-uncertainties-in-spatial-big-data-analytics)
  * [10 Estimating Vehicle Fuel Consumption and Emissions Using GPS Big Data](#10-estimating-vehicle-fuel-consumption-and-emissions-using-gps-big-data)
  * [11 Environmental benefits of bike sharing: A big data\-based analysis](#11-environmental-benefits-of-bike-sharing-a-big-data-based-analysis)
  * [12 Growth, innovation, scaling, and the pace of life in cities](#12-growth-innovation-scaling-and-the-pace-of-life-in-cities)
  * [13 Street as a big geo\-data assembly and analysis unit in urban studies: A case study using Beijing taxi data](#13-street-as-a-big-geo-data-assembly-and-analysis-unit-in-urban-studies-a-case-study-using-beijing-taxi-data)
* [GIS RS and IT Technology](#gis-rs-and-it-technology)
  * [1 R Package gdistance: Distances and Routes on Geographical Grids](#1-r-package-gdistance-distances-and-routes-on-geographical-grids)
  * [2 A New Set of Spatial\-Interaction Models: The Theory of Competing Destinations](#2-a-new-set-of-spatial-interaction-models-the-theory-of-competing-destinations)
  * [3 Mapping local variation in educational attainment across Africa](#3-mapping-local-variation-in-educational-attainment-across-africa)
  * [4 Spatiotemporal model for assessing the stability of urban human convergence and divergence patterns](#4-spatiotemporal-model-for-assessing-the-stability-of-urban-human-convergence-and-divergence-patterns)
  * [5 Designing an Experiment to Investigate Subpixel Mapping as an Alternative Method to Obtain Land Use/Land Cover Maps](#5-designing-an-experiment-to-investigate-subpixel-mapping-as-an-alternative-method-to-obtain-land-useland-cover-maps)
* [Public Health and Environmental Risk Factors](#public-health-and-environmental-risk-factors)
  * [1 Mapping child growth failure in Africa between 2000 and 2015](#1-mapping-child-growth-failure-in-africa-between-2000-and-2015)
  * [2 Real\-time and Seamless Monitoring of Ground\-level PM2\.5 Using Satellite Remote Sensing](#2-real-time-and-seamless-monitoring-of-ground-level-pm25-using-satellite-remote-sensing)
  * [3 Estimation of Ground PM2\.5 Concentrations using a DEM\-assisted Information Diffusion Algorithm: A Case Study in China](#3-estimation-of-ground-pm25-concentrations-using-a-dem-assisted-information-diffusion-algorithm-a-case-study-in-china)
  * [4 Natural and Built Environmental Exposures on Children's Active School Travel: A Dutch Global Positioning System\-based Cross\-sectional Study](#4-natural-and-built-environmental-exposures-on-childrens-active-school-travel-a-dutch-global-positioning-system-based-cross-sectional-study)
  * [5 The Uncertain Geographic Context Problem in the Analysis of the Relationships between Obesity and the Built Environment in Guangzhou](#5-the-uncertain-geographic-context-problem-in-the-analysis-of-the-relationships-between-obesity-and-the-built-environment-in-guangzhou)
  * [6 Spatio\-Temporal Pattern Estimation of PM2\.5 in Beijing\-Tianjin\-Hebei Region Based on MODIS AOD and Meteorological Data Using the Back Propagation Neural Network](#6-spatio-temporal-pattern-estimation-of-pm25-in-beijing-tianjin-hebei-region-based-on-modis-aod-and-meteorological-data-using-the-back-propagation-neural-network)
  * [7 Spatiotemporal Distribution of Satellite\-Retrieved Ground\-Level PM2\.5 and Near Real\-Time Daily Retrieval Algorithm Development in Sichuan Basin, China](#7-spatiotemporal-distribution-of-satellite-retrieved-ground-level-pm25-and-near-real-time-daily-retrieval-algorithm-development-in-sichuan-basin-china)
  * [8 Assessment of human health impact from exposure to multiple air pollutants in China based on satellite observations](#8-assessment-of-human-health-impact-from-exposure-to-multiple-air-pollutants-in-china-based-on-satellite-observations)
  * [9 High\-Resolution Satellite Mapping of Fine Particulates Based on Geographically Weighted Regression](#9-high-resolution-satellite-mapping-of-fine-particulates-based-on-geographically-weighted-regression)
  * [10 Estimating national\-scale ground\-level PM2\.5 concentration in China using geographically weighted regression based on MODIS and MISR AOD](#10-estimating-national-scale-ground-level-pm25-concentration-in-china-using-geographically-weighted-regression-based-on-modis-and-misr-aod)
* [Urban Resilience and Disasters](#urban-resilience-and-disasters)
  * [1 Assessing local resilience to typhoon disasters: A case study in Nansha, Guangzhou](#1-assessing-local-resilience-to-typhoon-disasters-a-case-study-in-nansha-guangzhou)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Urban Blue Space and Green Space

## 1 Dynamic assessments of population exposure to urban greenspace using multi-source big data

# Forest and Landscape Ecology

## 1 Global patterns of tropical forest fragmentation
**Title:** Global patterns of tropical forest fragmentation/全球热带森林破碎化格局

**Link:** [原文链接](https://www.nature.com/articles/nature25508)

**Doi:** 10.1038/nature25508

**Notes：** 遥感技术能够在高分辨率上定量化热带森林砍伐，这种技术使得在洲际尺度热带森林破碎化研究成为可能。该研究识别了三个大洲的13亿个热带森林破碎化区域。而这些破碎化区域的大小和周长呈现类似的幂律分布特征和分形维数。渗透理论为这个格局提供了一种解释：森林的破碎化接近渗透理论的临界点。模拟结果也支持了这个结论，同时发现随机毁林或者毁林恢复的管理方式也可以塑造出这种格局。该研究以渗透理论为研究框架分析当前美洲、非洲、亚洲、澳洲热带和亚热带森林结构的破碎化。使用了高分辨率的影像（30m)和一种聚类算法识别13亿个破碎化斑块。本身预期结果是，不同大洲不同的土地利用状况可能导致森林结构破碎化的差异，但事实却是在三个大洲上都呈现了相似的幂律分布规律。

渗透理论解释：
定义森林占据景观总栅格数的概率为p。渗透理论临界点值为0.59。当p很大时，整个景观都被森林占据（a）。当p接近临界点的时候，会形成所谓的"spanning cluster",能够从景观的一侧到达另一侧,相当于廊道。而当小于临界值p的时候（c,d），森林斑块无法连通景观，将导致森林斑块会愈加破碎化。

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

景观生态理论，遥感，森林生态学与气候变化的结合，从理论到实践。

**Graph/Table Interest：**

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/3.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/4.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/5.png)

**Resources:**

[幂律分布拟合相关代码（Matlab）](http://tuvalu.santafe.edu/~aaronc/powerlaws/bins/)

## 2 Mapping Ecosystem Service Bundles to Detect Distinct Types of Multifunctionality within the Diverse Landscape of the Yangtze River Basin, China

# Data Assimilation
## 1 A simplified data assimilation method for reconstructing time-series MODIS NDVI data

**Title:** A simplified data assimilation method for reconstructing time-series MODIS NDVI data/一种简化的数据同化方法用来重建MODIS NDVI时间序列数据

**Link:** [原文链接](https://www.sciencedirect.com/science/article/pii/S0273117709003512)

**Doi:** 10.1016/j.asr.2009.05.009

**Notes:** 这个研究提供了一种简化的数据同化方法用来重建MODIS NDVI的时间序列数据。该研究使用三点平滑方法利用前三年的数据生成一个背景场数据，这个方法可以捕捉NDVI变化的年度特征，用2006年NDVI数据来测试这种简化的数据同化方法。每个时间步长，采用MODIS的QA数据根据经验确定背景场与NDVI观测值之间的权重。结果表明该方法有很好的鲁棒性和有效性。提出了数据同化通用的代价函数，并将代价函数引入到NDVI的数据同化框架时，进行了简化和推导。从而简化了数据同化的方式，同时由于难以直接估计背景场与观测场的误差协方差，于是通过MODIS的QA数据，根据经验计算权重系数。

**Highlights:**

(1) 一种简化的NDVI数据同化方式;

(2)基于三点平滑的方法生成背景场;

(3)在难以直接估计背景场和观测场的误差时，使用QA数据对权重系数计算。

**Research gap/question:**

数据同化技术过去是在气象、水文领域率先兴起的，但是同时地学下的对地观测数据、地面观测数据都存在大量噪声，如何整合这些含有噪声的数据得到更为精确的时空数据是目前地学研究的一大重点，而数据同化就是其中的一种关键性的方法。

**Disscussion/Conclusion:**

(1)  The background NDVI field has certain limitations in capturing detailed variations, but it can offer valuable information with respect to identifying and correcting noisy points in a multi-year average profile of vegetation. NDVI背景场在捕获详细变化方面有一定的局限性，但它可以提供有价值的信息，用于识别和纠正多年平均NDVI中的噪声点。

(2)An important reason for this is the use of the synchronous QA flag to estimate the NDVI and to enable realistic corrections. However, the current reconstructing scheme can not always perform well at the onset of spring green due to the average background. The effects of outliers (e.g. strong spurious lows) will be considered as well for reducing the extension from neighboring data points. So a more effective scheme to determine the weight coefficient K will be developed.其中一个重要原因是使用QA数据来估计NDVI并校正。然而，由于背景场是多年平均得到的，目前的重建方案在春季植被变绿的开始阶段并表现不总是良好。异常值的影响（例如强烈的低估）也将被用于减少相邻数据点的扩展。因此，未来应当开发一个更有效的确定权重系数K的方案。

这篇文章对于数据同化的概念理解是非常好的，而且也提供了一个范例，将数据同化的方法引入到生态学研究中。

**Graph/Table Interest：**

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/13.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/14.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/15.png)

## 2 A review of data assimilation of remote sensing and crop models

**Title:** A review of data assimilation of remote sensing and crop models/遥感数据与作物生长模型数据同化的综述

**Link:** [原文链接](https://www.sciencedirect.com/science/article/pii/S1161030117301685)

**Doi:** 10.1016/j.eja.2017.11.002

**Notes:** 这是一篇关于作物生长模型、遥感数据与数据同化的综述文章。比较全面地讲述了作物生长模型、遥感数据与数据同化最近的发展综述。这里给了一个比较通用的数据同化概念解释。同化的目的是在空间和时间上整合各种信息的状态变量，以利用遥感方法优化作物模型中的作物参数。在处理数据同化时，首先必须区分观测变量（来自遥感数据资源），状态变量（来自完整的作物模型系统），模型参数（描述的观测变量与状态变量之间的关系，从这个角度也可以称其为观测算子）和输出变量（在大部分数据同化中产量）。在这篇文章里将数据同化算法分为三类：校准方法，强制方法和更新方法。第一部分是关于不同数据同化方法的有缺点比较和分析。这里有个关键表格。

|算法|基础公式|算法机制与特点|参考文献|
|--|:--:|:--:|:--:|
|KF|$$X_k^f=M_{k-1,k}X_{k-1}^a$$ $$X_k^a=X_k^f+K_k(Y_k^o-H_kX_k^f)$$ $$K_k=(H_kP_k)^T[H_k(H_kP_k^f)^T+R_k]^{-1}$$|观测值用于在观测值存在时调整轨迹的模型状态值，得到当前时刻的最优状态值，然后重新初始化模型的当前状态估计值; 继续前向整合，直到有下一个观测数据。 它可以预测实时状态并更新状态，但当Hk和Mk非线性时不适用|Aubert et al. (2003) and Pellenq and Boulet (2004)|
|EnKF|$$X_{i,k+1}^f=M_{k,k+1}(X_{i,k}^a+w_{i,k}),w_{i,k}\sim(0, Q_k)$$ $$X_{i,k+1}^a=X_{i,k+1}^f+K_{k+1}[Y_{k+1}-H(X_{i,k+1}^f)+v_{i,k}]$$ $$K_{k+1}=P_{k+1}H_{k+1}(HP_{k+1}^fH^T+R_k)^{-1}$$ $$X_{i,k+1}^a=\frac{1}{N}\sum_{i=1}^NX_{i,k+1}^a$$|通过蒙特卡罗方法将集合预测和卡尔曼滤波结合起来计算预测误差协方差。 它可以用于数据同化的非线性系统。 它在计算上不太密集并且容易进行并行计算。|Evensen (1994), Crow and Wood (2003) and Schläpfer and Richter (2002)|
|3DVAR|$$J(X)=(X-X^b)^TB^{-1}(X-X^b)+(Y-HX)^TR^{-1}(Y-HX)$$ $$\Delta J(X)=2B^{-1}(X-X^b)-2H^TR^{-1}(Y-HX)$$|数据同化窗口T的所有观测用于调整模型中轨迹的预测值，构造成本函数J（X）表示分析场与真值之间的误差，求解成本函数的最小化最优解。 由于成本函数很难直接计算，需要借助梯度函数△J（X）和伴随模型。|Lorenc et al. (2000)|
|4DVAR|$$J(X)=(X-X^b)^TB^{-1}(X-X^b)+\sum_{K=0}^{T}\,^{(Y_k-H_k(M_k(M_{k-1}(\dots(M_1(X))))))^T}_{R^{-1}(Y_k-H_k(M_k(M_{k-1}(\dots(M_1(X))))))}$$ $$\Delta J(X)=2B^{-1}(X-X^b)-2\sum_{K=0}^{T}\,^{\begin{cases}M_1^T\cdots M_{k-1}^TM_k^TH_k^TR_k^{-1}\end{cases}}_{[Y_k-H_k(M_k(M_{k-1}(\dots(M_1(X)))))]}$$|基于3DVAR考虑状态Mt随时间的变化，T时刻状态的最优估计值为综合考虑Mt结果。 它还需要梯度函数和伴随模型的帮助。 由于考虑Mt.因此计算量更大。|Trémolet (2007)|
|PF|$$P(X_k^a \mid X_{1:k})\approx\sum^{N}_{i=1}w_{i,k}\delta(X_k^a-X_{i,k}^a)$$ $$w_{i,k}\propto \frac{p(X_{i,k}^a \mid X_{1:k})}{q(X_{i,k}^a \mid X_{1:k})}, \sum_{i=1}^N w_{i,k}=1$$|用一组粒子对后验概率分布进行采样，然后根据采样点分析后验概率分布。 它不受非线性系统的限制和高斯分布的假设。 它适用于并行计算。|Moradkhani et al. (2005)|
|HBM|$$p(\theta_D,\theta_P,Y\mid X)\approx \\ p(X_1\mid Y_1,\theta_D)\cdots p(X_n\mid Y_n, \theta_D)\\p(Y_1 \mid \theta_P,Y_2,\cdots.Y_n)\cdots p(Y_n ]mid \theta_P)\\p(\theta_D)p(\theta_P)$$|将数据同化分为数据，过程和参数桑格曾。针对每个层定义的一个条件概率模型。于是数据同化就转换为推理过程的问题和给定数据条件下参数的后验概率分布。|Sahu et al. (2009) and Plant and Holland (2011)|

**Highlights:**

(1) 作物生长模型、遥感数据与数据同化最近的发展综述；

(2) 不同同化方法优缺点比较；

(3) 不同误差源对数据同化链中不同部分的影响分析；

(4) 它为今后的研究提供了进一步的机会和数据同化的发展方向。

**Research gap/question:**




# Mapping High Resolution Carbon Emission

## 1  China’s CO2 emissions estimated from the bottom up: Recent trends, spatial distributions, and quantification of uncertainties

**Title:** China’s CO2 emissions estimated from the bottom up: Recent trends, spatial distributions, and quantification of uncertainties/自下而上估计中国CO2排放：近期趋势，空间分布与不确定性的定量化 

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

这篇文章主要的讨论点不是太明显，因为是把结果和讨论混在一起写到的，总体来说讨论部分除了上面我提到的两个关键点之外，就是跟IPCC等机构的数据做对比，还有对政策部分的一些预测，EF排放因子表是非常不错的数据，此外生成了一个以人口和经济分配得到的0.25°×0.25°的产品。

**Graph/Table Interest：**

Tab.1 Emission Factors Table:

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/1.png)

Tab.2 Uncertainty of CO2

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/2.png)

**Resources:**

无

## 2 Effect of Urbanization on Carbon Dioxide Emissions Efficiency in the Yangtze River Delta, China

# Urban Computing and GIS
## 1 Characterizing mixed-use buildings based on multi-source big data
**Title:** Characterizing mixed-use buildings based on multi-source big data/基于多源大数据的混合功能建筑物分类

**Link:** [原文链接](https://www.tandfonline.com/doi/abs/10.1080/13658816.2017.1410549)

**Doi:** 10.1080/13658816.2017.1410549

**Notes:** 这个研究主要是集成了多源大数据（社交网络数据、出租车轨迹数据、POI兴趣点数据和遥感图像），利用一个概率模型来表征城市当中的混合功能建筑物的识别。并且以广州市天河区为例，模型分类精度达到了85%，同时对建筑物的空间分布模式进一步探究，大多数混合功能的建筑物都位于主要街道，而这个方法也将为小尺度城市规划评估和决策研究提供支持。文章主要重点是这个可以分类的概率模型。技术流程图如下：

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/8.png)

数据源有四个社交网络数据（腾讯宜出行平台的时空数据）、出租车轨迹数据、POI兴趣点数据以及建筑足迹（Quick Bird影像解译），多源大数据共计两天时间获取（一天周末，一天工作日）。First Stage：首先出租车轨迹数据先提取了上下车的地点，接着用POI数据基于贝叶斯原理进行修正，得到不同建筑物乘客乘出租车出行目的的最大概率，当有多个出行目的的最大概率，就认为是混合功能建筑物。后期用IDW插值，最后与建筑足迹数据叠加。Second Stage：随机选取一些建筑物通过POI和百度街景地图识别出建筑物功能作为训练样本，统计建筑物内微信使用者的数量。这里有一个假设，人由于特定的目的（休息、吃饭等 ）长时间位于固定地点（家、餐厅），这些被称为活动中心，而关键假设就是，同一种功能的建筑物与微信用户的日常活动有相同的高峰时间。接着使用核密度估计方法来识别这些功能，如果有多个高峰时期就认为是混合功能建筑物。First Stage和Second Stage叠加之后，可能结果存在差异，又构建了一个correctation rule来进行推断。

**Hightlights：**

(1) 一种集成多源大数据和概率模型表征城市混合功能建筑物识别的方法；

(2) 高精度分类模型；

(3) 混合功能建筑空间分布模式。

**Research gap/question：**

到目前为止很少有研究能成功整合多源大数据描述城市混合功能建筑物识别。

**Disscussion/Conclusion：**

(1) Spatial distribution of mixed-use buildings. 混合功能区建筑物的分布与距城市中心的距离是一致的。从城市的内部到外部，建筑物的功能从混合到单一变化。

(2) Spatial interaction between human activities and buildings’ functions. 建筑物类型影响了人类活动，建筑物类型越复杂，混合程度越高，居民通勤距离就越短。

(3) Sources of inference errors. 多源数据，结构不同，采集时间也有差异。

IJGIS这篇文章的讨论部分偏向于研究结果的解释以及目前研究的不足缺陷。

**Graph/Table Interest：**

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/9.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/10.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/11.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/12.png)

**Resources:**

无

## 2 Quantitative Comparison of Open-Source Data for Fine-Grain Mapping of Land Use
**Title:** Quantitative Comparison of Open-Source Data for Fine-Grain Mapping of Land Use

**Link:** [原文链接](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLII-2-W7/981/2017/)

**Doi:** 

**Notes:** 

## 3 Sensing Urban Land-Use Patterns By Integrating Google Tensorflow And Scene-Classification Models
**Title:** Sensing Urban Land-Use Patterns By Integrating Google Tensorflow And Scene-Classification Models

**Link:** [原文链接](https://arxiv.org/abs/1708.01580)

**Doi:** 

**Notes:** 

## 4 The Combined Use of Remote Sensing and Social Sensing Data in Fine-Grained Urban Land Use Mapping: A Case Study in Beijing, China
**Title:** The Combined Use of Remote Sensing and Social Sensing Data in Fine-Grained Urban Land Use Mapping: A Case Study in Beijing, China

**Link:** [原文链接](https://arxiv.org/abs/1711.03641)

**Doi:** 10.3390/rs9090865

**Notes:**

## 5 Urban Land Use Mapping by Combining Remote Sensing Imagery and Mobile Phone Positioning Data
**Title:** Urban Land Use Mapping by Combining Remote Sensing Imagery and Mobile Phone Positioning Data

**Link:** [原文链接](http://www.mdpi.com/2072-4292/10/3/446/xml)

**Doi:** 10.3390/rs10030446

**Notes:**

## 6 Spatio-Temporal Analytics for Exploring Human Mobility Patterns and Urban Dynamics in the Mobile Age
**Title:** Spatio-Temporal Analytics for Exploring Human Mobility Patterns and Urban Dynamics in the Mobile Age

**Link:** [原文链接](https://www.tandfonline.com/doi/abs/10.1080/13875868.2014.984300)

**Doi:** 10.1080/13875868.2014.984300

**Notes:**

## 7 Simulating urban dynamics in China using a gradient cellular automata model based on S-shaped curve evolution characteristics
**Title:** Simulating urban dynamics in China using a gradient cellular automata model based on S-shaped curve evolution characteristics

**Link:** [原文链接](https://www.tandfonline.com/doi/abs/10.1080/13658816.2017.1376065)

**Doi:** 10.1080/13658816.2017.1376065

**Notes:**

## 8 Identifying Local Spatiotemporal Autocorrelation Patterns of Taxi Pick-ups and Dropoffs
**Title:** Identifying Local Spatiotemporal Autocorrelation Patterns of Taxi Pick-ups and Dropoffs

**Link:** [原文链接](http://escholarship.ucop.edu/uc/item/04b2d8xp)

**Doi:** DOI10.21433/B31104B2D8XP

**Notes:**

## 9 Challenges and Prospects of Uncertainties in Spatial Big Data Analytics
**Title:** Challenges and Prospects of Uncertainties in Spatial Big Data Analytics

**Link:** [原文链接](https://www.researchgate.net/publication/322265057_Challenges_and_Prospects_of_Uncertainties_in_Spatial_Big_Data_Analytics)

**Doi:** DOI10.1080/24694452.2017.1421898

**Notes:**

## 10 Estimating Vehicle Fuel Consumption and Emissions Using GPS Big Data

## 11 Environmental benefits of bike sharing: A big data-based analysis

## 12 Growth, innovation, scaling, and the pace of life in cities

## 13 Street as a big geo-data assembly and analysis unit in urban studies: A case study using Beijing taxi data

# GIS RS and IT Technology
## 1 R Package gdistance: Distances and Routes on Geographical Grids
**Title:** R Package gdistance: Distances and Routes on Geographical Grids/R包gdistance：地理格网的距离和路径

**Link:** [原文链接](https://www.jstatsoft.org/article/view/v076i13)

**Doi:** 10.18637/jss.v076.i13

**Notes:** 这篇文章源自统计学SCI顶刊（Journal of Statistical Software），偏向于软件开发类的文章。主要介绍的就是作者开发的R包——gdistance，对栅格数据的距离和路径计算（除了普通距离，包括像基于受限随机游走等的最小成本距离）的一个包。另外是提供一些class，基于内存稀疏格式可以存储从一个栅格到达另一个栅格的概率或成本的栅格数据。这篇文章分为12个部分。第一部分引言介绍了一些基础的概念。第二章阐述的是这个包的计算基础理论。这篇文章在基础理论部分谈到了很多不同GIS软件关于距离和计算的原理。包括四邻域、八邻域、十六邻域的问题。这里给出一个gdistance的概念——阻抗栅格也就是transition matrices,且存储的是类似于阻抗n而不是过往GIS软件里的阻抗率1/n，这一点主要是存储方便。不对称矩transition matrices的建立主要通过定义一个function，使得f(i,j)≠f(j,i)。第三部分讲的是栅格基础的内容（这个包依赖于raster）。第四部分讲的是本包根本的类transition* classes。第四部分到第八部分是gdistance求取栅格距离和最短路径计算的步骤。先创建transition* classes，接着由于投影造成的栅格失真，可以通过第五部分的校正处理。第六部分就可以计算距离了（依赖于igraph）。第七部分计算基于随机游走的离散距离。第八部分介绍的是如何确定轨迹的重叠程度。第九部分和第十部分是两个案例研究——登山路径以及遗传的地理隔绝现象。第十一部分是future study。第十二部分是联系方式等。

总的来说，这篇文章偏向于软件开发和算法，针对栅格数据的距离计算展开了一系列的研究，并开发了gdistance，两个 案例研究体现了gdistance关键函数和算法。


**Highlights:**

(1)  gdistance包；

(2) transition* classes；

(3) 多种应用场景的不同距离算法函数。

**Research gap/question：**

栅格数据的距离计算和最短路径求取的优化以及更精确表达。

**Disscussion/Conclusion：**

(1) The section on distance transforms in de Smith, Goodchild, and Longley (2009) also discusses 16-cell neighborhoods.Connecting in 16 directions may increase the accuracy of the calculations.16邻域的邻域计算法则可能会提高距离计算的精度。

(2) More research on the consequences of connecting grids in different ways is necessary, as indicated in Section 2. This should bring more precision to random walk calculations in geospatial analysis. Comparing the results of grid-based calculations to continuous space simulations or analytical solutions would be the way forward. 不同邻域设置导致研究后果差异是值得关注的，这些会提高计算精度。

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/6.png)

软件开发类文章讨论较少，Future Study是一个比较值得关注的点。

**Graph/Table Interest：**

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/7.png)

**Resources:**

[gdistance](https://github.com/cran/gdistance)

[circuitscape](http://www.circuitscape.org)


## 2 A New Set of Spatial-Interaction Models: The Theory of Competing Destinations
**Title:** A New Set of Spatial-Interaction Models: The Theory of Competing Destinations

**Link:** [原文链接](http://journals.sagepub.com/doi/pdf/10.1177/0308518X8301500103)

**Doi:** 10.1177/0308518X8301500103

**Notes:** 

## 3 Mapping local variation in educational attainment across Africa
**Title:** Mapping local variation in educational attainment across Africa

**Link:** [原文链接](https://www.nature.com/articles/nature25761)

**Doi:** 10.1038/nature25761

**Notes:** 

## 4 Spatiotemporal model for assessing the stability of urban human convergence and divergence patterns


## 5 Designing an Experiment to Investigate Subpixel Mapping as an Alternative Method to Obtain Land Use/Land Cover Maps


# Public Health and Environmental Risk Factors
## 1 Mapping child growth failure in Africa between 2000 and 2015
**Title:** Mapping child growth failure in Africa between 2000 and 2015

**Link:** [原文链接](https://www.nature.com/articles/nature25760)

**Doi:** 10.1038/nature25760

**Notes:** 

## 2 Real-time and Seamless Monitoring of Ground-level PM2.5 Using Satellite Remote Sensing

**Title:** Real-time and Seamless Monitoring of Ground-level PM2.5 Using Satellite Remote Sensing

**Link:** [原文链接](https://www.researchgate.net/publication/323694623_Real-time_and_Seamless_Monitoring_of_Ground-level_PM25_Using_Satellite_Remote_Sensing)

**Doi:** 

**Notes:** 

## 3 Estimation of Ground PM2.5 Concentrations using a DEM-assisted Information Diffusion Algorithm: A Case Study in China

**Title:** Estimation of Ground PM2.5 Concentrations using a DEM-assisted Information Diffusion Algorithm: A Case Study in China

**Link:** [原文链接](https://www.nature.com/articles/s41598-017-14197-z?WT.feed_name=subjects_physical-sciences)

**Doi:** 10.1038/s41598-017-14197-z

**Notes:** 

## 4 Natural and Built Environmental Exposures on Children's Active School Travel: A Dutch Global Positioning System-based Cross-sectional Study

**Title:** Natural and Built Environmental Exposures on Children's Active School Travel: A Dutch Global Positioning System-based Cross-sectional Study

**Link:** [原文链接](http://europepmc.org/abstract/MED/27010106)

**Doi:** 10.1016/j.healthplace.2016.03.003  

**Notes:** 

## 5 The Uncertain Geographic Context Problem in the Analysis of the Relationships between Obesity and the Built Environment in Guangzhou

**Title:** The Uncertain Geographic Context Problem in the Analysis of the Relationships between Obesity and the Built Environment in Guangzhou

**Link:** [原文链接](http://europepmc.org/abstract/MED/29439392)

**Doi:** 10.3390/ijerph15020308

**Notes:** 

## 6 Spatio-Temporal Pattern Estimation of PM2.5 in Beijing-Tianjin-Hebei Region Based on MODIS AOD and Meteorological Data Using the Back Propagation Neural Network

## 7 Spatiotemporal Distribution of Satellite-Retrieved Ground-Level PM2.5 and Near Real-Time Daily Retrieval Algorithm Development in Sichuan Basin, China

## 8 Assessment of human health impact from exposure to multiple air pollutants in China based on satellite observations

## 9 High-Resolution Satellite Mapping of Fine Particulates Based on Geographically Weighted Regression

## 10 Estimating national-scale ground-level PM25 concentration in China using geographically weighted regression based on MODIS and MISR AOD

# Urban Resilience and Disasters
## 1 Assessing local resilience to typhoon disasters: A case study in Nansha, Guangzhou
**Title:** Assessing local resilience to typhoon disasters: A case study in Nansha, Guangzhou

**Link:** [原文链接](https://doi.org/10.1371/journal.pone.0190701)

**Doi:** 10.1371/journal.pone.0190701

**Notes:**