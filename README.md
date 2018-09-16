论文阅读笔记
这个repo主要记录平时阅读论文的一些笔记，论文包括关于GIS、地理、遥感、生态等相关方向，主要是感兴趣的方向或者是目前研究相关文章。笔记内容主要是我看文章时的想法，大致包括论文的idea，一些重要的要点和我的评价。目录按照类别进行整理,刚刚建立，内容将慢慢添加。

Table of Contents
=================

* [Urban Blue Space and Green Space](#urban-blue-space-and-green-space)
  * [1 Dynamic assessments of population exposure to urban greenspace using multi\-source big data](#1-dynamic-assessments-of-population-exposure-to-urban-greenspace-using-multi-source-big-data)
* [Forest and Landscape Ecology](#forest-and-landscape-ecology)
  * [1 Global patterns of tropical forest fragmentation](#1-global-patterns-of-tropical-forest-fragmentation)
  * [2 Mapping Ecosystem Service Bundles to Detect Distinct Types of Multifunctionality within the Diverse Landscape of the Yangtze River Basin, China](#2-mapping-ecosystem-service-bundles-to-detect-distinct-types-of-multifunctionality-within-the-diverse-landscape-of-the-yangtze-river-basin-china)
  * [3 Coupled natural and human systems: a landscape ecology perspective](#3-coupled-natural-and-human-systems-a-landscape-ecology-perspective)
  * [4 A scalable cyberinfrastructure and cloud computing platform for forest aboveground biomass estimation based on the Google Earth Engine](#4-a-scalable-cyberinfrastructure-and-cloud-computing-platform-for-forest-aboveground-biomass-estimation-based-on-the-google-earth-engine)
* [Data Assimilation](#data-assimilation)
  * [1 A simplified data assimilation method for reconstructing time\-series MODIS NDVI data](#1-a-simplified-data-assimilation-method-for-reconstructing-time-series-modis-ndvi-data)
  * [2 A review of data assimilation of remote sensing and crop models](#2-a-review-of-data-assimilation-of-remote-sensing-and-crop-models)
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
  * [14 The Combined Use of Remote Sensing and Social Sensing Data in Fine\-Grained Urban Land Use Mapping: A Case Study in Beijing, China](#14-the-combined-use-of-remote-sensing-and-social-sensing-data-in-fine-grained-urban-land-use-mapping-a-case-study-in-beijing-china)
  * [15 Mapping China’s Ghost Cities through the Combination of Nighttime Satellite Data and Daytime Satellite Data](#15-mapping-chinas-ghost-cities-through-the-combination-of-nighttime-satellite-data-and-daytime-satellite-data)
  * [16 Urban growth simulation by incorporating planning policies into a CA\-based future land\-use simulation model](#16-urban-growth-simulation-by-incorporating-planning-policies-into-a-ca-based-future-land-use-simulation-model)
  * [17 Portraying Urban Functional Zones by Coupling Remote Sensing Imagery and Human Sensing Data](#17-portraying-urban-functional-zones-by-coupling-remote-sensing-imagery-and-human-sensing-data)
* [GIS RS and IT Technology](#gis-rs-and-it-technology)
  * [1 R Package gdistance: Distances and Routes on Geographical Grids](#1-r-package-gdistance-distances-and-routes-on-geographical-grids)
  * [2 A New Set of Spatial\-Interaction Models: The Theory of Competing Destinations](#2-a-new-set-of-spatial-interaction-models-the-theory-of-competing-destinations)
  * [3 Mapping local variation in educational attainment across Africa](#3-mapping-local-variation-in-educational-attainment-across-africa)
  * [4 Spatiotemporal model for assessing the stability of urban human convergence and divergence patterns](#4-spatiotemporal-model-for-assessing-the-stability-of-urban-human-convergence-and-divergence-patterns)
  * [5 Designing an Experiment to Investigate Subpixel Mapping as an Alternative Method to Obtain Land Use/Land Cover Maps](#5-designing-an-experiment-to-investigate-subpixel-mapping-as-an-alternative-method-to-obtain-land-useland-cover-maps)
  * [6 Spatial association detector (SPADE)](#6-spatial-association-detector-spade)
  * [7 Spatiotemporal Fusion of Multisource Remote Sensing Data: Literature Survey, Taxonomy, Principles, Applications, and Future Directions](#7-spatiotemporal-fusion-of-multisource-remote-sensing-data-literature-survey-taxonomy-principles-applications-and-future-directions)
  * [8 Modeling the Distributions of Brightness Temperatures of a Cropland Study Area Using a Model that Combines Fast Radiosity and Energy Budget Methods](#8-modeling-the-distributions-of-brightness-temperatures-of-a-cropland-study-area-using-a-model-that-combines-fast-radiosity-and-energy-budget-methods)
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
  * [10 Estimating national\-scale ground\-level PM25 concentration in China using geographically weighted regression based on MODIS and MISR AOD](#10-estimating-national-scale-ground-level-pm25-concentration-in-china-using-geographically-weighted-regression-based-on-modis-and-misr-aod)
  * [11 Evaluation of machine learning techniques with multiple remote sensing datasets in estimating monthly concentrations of ground\-level PM2\.5](#11-evaluation-of-machine-learning-techniques-with-multiple-remote-sensing-datasets-in-estimating-monthly-concentrations-of-ground-level-pm25)
  * [12 Spatiotemporal Distribution of Satellite\-Retrieved Ground\-Level PM2\.5 and Near Real\-Time Daily Retrieval Algorithm Development in Sichuan Basin, China](#12-spatiotemporal-distribution-of-satellite-retrieved-ground-level-pm25-and-near-real-time-daily-retrieval-algorithm-development-in-sichuan-basin-china)
* [Urban Resilience and Disasters](#urban-resilience-and-disasters)
  * [1 Assessing local resilience to typhoon disasters: A case study in Nansha, Guangzhou](#1-assessing-local-resilience-to-typhoon-disasters-a-case-study-in-nansha-guangzhou)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Urban Blue Space and Green Space

## 1 Dynamic assessments of population exposure to urban greenspace using multi-source big data
**Title:** Dynamic assessments of population exposure to urban greenspace using multi-source big data

**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

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

**Discussion/Conclusion:**

(1) The findings of the extended percolation models underpin the universality of fragmentation patterns close to the critical point. 扩展渗透模型发现支撑了接近临界值的破碎化景观格局的普遍性。

(2) This is a general feature of critical phenomena: their large-scale behaviour is independent of the underlying small-scale mechanisms.关键现象的一般特征，大尺度的行为是独立于小尺度的机制的。

(3)Even though land use appears to be complex and diverse, our outcomes emphasize that simple mechanisms are sufficient for describing forest fragmentation structures at larger scales. 尽管土地利用变化多样复杂，我们的结果显示了简单的机制足以描述大尺度森林结构的破碎化。

景观生态理论，遥感，森林生态学与气候变化的结合，从理论到实践。

**Graph/Table interested：**

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/3.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/4.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/5.png)

**Resources:**

[幂律分布拟合相关代码（Matlab）](http://tuvalu.santafe.edu/~aaronc/powerlaws/bins/)

## 2 Mapping Ecosystem Service Bundles to Detect Distinct Types of Multifunctionality within the Diverse Landscape of the Yangtze River Basin, China
**Title:** Mapping Ecosystem Service Bundles to Detect Distinct Types of Multifunctionality within the Diverse Landscape of the Yangtze River Basin, China

**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 3 Coupled natural and human systems: a landscape ecology perspective
**Title:** Coupled natural and human systems: a landscape ecology perspective

**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 4 A scalable cyberinfrastructure and cloud computing platform for forest aboveground biomass estimation based on the Google Earth Engine

**Title:** A scalable cyberinfrastructure and cloud computing platform for forest aboveground biomass estimation based on the Google Earth Engine

**Link:** [原文链接](https://www.tandfonline.com/doi/abs/10.1080/17538947.2018.1494761?journalCode=tjde20)

**Doi:** 10.1080/17538947.2018.1494761

**Notes:** 

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

**Discussion/Conclusion:**

(1)  The background NDVI field has certain limitations in capturing detailed variations, but it can offer valuable information with respect to identifying and correcting noisy points in a multi-year average profile of vegetation. NDVI背景场在捕获详细变化方面有一定的局限性，但它可以提供有价值的信息，用于识别和纠正多年平均NDVI中的噪声点。

(2)An important reason for this is the use of the synchronous QA flag to estimate the NDVI and to enable realistic corrections. However, the current reconstructing scheme can not always perform well at the onset of spring green due to the average background. The effects of outliers (e.g. strong spurious lows) will be considered as well for reducing the extension from neighboring data points. So a more effective scheme to determine the weight coefficient K will be developed.其中一个重要原因是使用QA数据来估计NDVI并校正。然而，由于背景场是多年平均得到的，目前的重建方案在春季植被变绿的开始阶段并表现不总是良好。异常值的影响（例如强烈的低估）也将被用于减少相邻数据点的扩展。因此，未来应当开发一个更有效的确定权重系数K的方案。

这篇文章对于数据同化的概念理解是非常好的，而且也提供了一个范例，将数据同化的方法引入到生态学研究中。

**Graph/Table interested:**

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/13.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/14.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/15.png)

**Resources:**
无

## 2 A review of data assimilation of remote sensing and crop models

**Title:** A review of data assimilation of remote sensing and crop models/遥感数据与作物生长模型数据同化的综述

**Link:** [原文链接](https://www.sciencedirect.com/science/article/pii/S1161030117301685)

**Doi:** 10.1016/j.eja.2017.11.002

**Notes:** 这是一篇关于作物生长模型、遥感数据与数据同化的综述文章。比较全面地讲述了作物生长模型、遥感数据与数据同化最近的发展综述。这里给了一个比较通用的数据同化概念解释。同化的目的是在空间和时间上整合各种信息的状态变量，以利用遥感方法优化作物模型中的作物参数。在处理数据同化时，首先必须区分观测变量（来自遥感数据资源），状态变量（来自完整的作物模型系统），模型参数（描述的观测变量与状态变量之间的关系，从这个角度也可以称其为观测算子）和输出变量（在大部分数据同化中产量）。在这篇文章里将数据同化算法分为三类：校准方法，强制方法和更新方法。第一部分是关于不同数据同化方法的优缺点比较和分析。

这里可以重点阐述下优缺点，方法比较有个重要的表格。

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/16.png)

优缺点比较：KF方法不能用于处理高维数据，作物冠层状态变量和结构往往难以作为输入，并且这会导致作物模型中输入的不确定性。因此，Evensen开发了EnKF来克服这些问题。一些研究表明，EnKF方法对作物模型和遥感数据之间的数据同化非常有用。变分方法（3DVAR和4DVAR）比卡尔曼滤波的集合变体更为成熟，并且在预测天气预报方面非常成功。在同化过程中，3DVAR模型可以使用复杂的观测算子;同化非直接或相关非线性观测的状态变量更容易。然而，3DVAR模型在实际应用中受到限制，因为计算成本较高。为了改善3DVAR的缺点，开发了基于3DVAR的4DVAR。它弥补了在某些情况下状态变量时间变化和初始化时3DVAR的不足。自提出以来，4DVAR广泛应用，并受到相当的关注和应用。 PF模型也被称为序贯蒙特卡罗滤波器，它是基于顺序重要性抽样滤波理论的贝叶斯估计而开发的。与KF系列算法相比，PF算法不受高斯分布假设的非线性误差的限制。 KF系列算法只能使用均值和方差的后验概率，而PF算法可以采用蒙特卡罗采样方法的后验分布概率。它在非线性系统的变化中具有更好的性能，并且更容易进行并行计算。 Berliner提出的HBM模型基于条件概率分布的理论基础，将复杂问题分解建立不同层次，各层之间通过条件概率相连，然后进行复杂的联合概率问题求解被转换成一系列简单的问题解决后验概率。 HBM是数据同化问题的理想方法。它具有贝叶斯理论和分层建模的优点;这两个性质使得HBM与其他数据同化方法有明显的区别。 HBM对数据同化的研究还远远落后于其他算法，但我们相信，随着计算机性能的发展和对物理过程的理解的提高，它将为数据同化带来新的发展。遥感技术和作物模型通过一定的算法相结合来提高生理生长模拟精度，并且该方法已被用于提高区域研究中作物产量的估计精度。

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/17.png)

校准方法：将作物模型的初始参数调整为遥感数据与模拟状态变量（作物模型的模拟数据）之间的最佳一致性。使用不同积分参数值的真实范围手动或自动运行作物模型，以校准作物模型参数的灵敏度和不确定性。利用校正方法对作物模型和遥感数据进行数据同化。单纯形搜索算法，最大似然解（MLS），最小二乘法（LSM），Powell共轭方向法（PCDM），快速模拟退火算法（VFSA）和粒子群优化算法。

强迫方法：强迫方法使用遥感数据替代作物模型模拟数据。遥感数据直接用于规定模拟数据，这些数据需要每个作物模型时间步骤的遥感数据的可行性，这些时间步骤在大多数作物模型中是每天，每周或每月。在正常情况下，卫星通行频率小于作物模型的时间步长。为了在作物模型的模拟数据中的时间步长驱动遥感数据，使用线性插值，快速傅立叶变换和小波方法来填补遥感数据观测之间的差距。遥感数据估算的LAI主要用作状态变量并输入作物模型。除了LAI，通过遥感提取开花日期或者用遥感估计截留效率指数（ε）和FAPAR也有部分研究。基于强迫法，作物模型和遥感数据的数据同化易于操作，严格来说，不涉及数据同化方法。作物模型的模拟状态变量或初始输入数据仅被估计的状态变量或遥感数据的初始输入数据替代。遥感提供了高精度的状态变量，并能够获得良好的估计结果。

更新方法：当获得遥感数据是可行的时，更新方法包括不断更新农作物模型模拟数据。这是基于这样的假设，即在第t天更好的模拟数据将提高随后几天模拟数据的准确性。更新方法通常被称为数据同化，并且一些算法已被应用于遥感数据和作物模型的同化。利用EnKF，4DVar，PF，4DVar（POD4DVar）的适当正交分解技术和集合平方根滤波方法，将遥感数据和作物模型的状态变量整合起来用来估计土壤水分，AGB，LAI和产量。

理论上校准方法优于强制和更新方法，但这种方法的主要缺点是需要大量的优化迭代，导致计算时间更长。与校准方法相比，更新方法显着减少了计算时间，因为只有作物模型运行。但是，这种方法也存在缺陷，因为它需要最昂贵的计算和测量不确定度。此外，更新方法需要在运行作物模型时调整作物参数变量。选择遥感影像的日期是影响估计精度的重要因素。同样已有研究证实了更新方法中物候转移对数据同化效率的影响。

接着是不同误差源对数据同化链中不同部分的影响分析。

(1) 作物生长模型——1.无法反应病虫害影响；2.模型遗传参数的误差；3.品种和区域管理参数合并；4.空间数据误差；5.单点开发模型，尺度扩展中违背系统边界。具体解决方案包括：1.增加模型中病虫害影响的响应；2.敏感性分析方法组合（EFAST, MCMC, GA, SCE-UA, GLUE)；4.遥感数据用来提供土壤属性、作物生长情况与天气数据；4.不同作物模型的整合。

(2) 遥感数据——遥感技术的优点是它可以在不同的空间尺度上持续提供各种有用的作物信息。监测作物生长过程是农业收获的关键;主要指标包括LAI，冠层覆盖度，叶绿素含量，作物根系层土壤含水量，冠层含水量和胁迫因子等。目前，遥感数据的植被指数难以满足作物模型的要求。目前，定量遥感面临着定向问题，尺度效应和尺度转换以及反演策略和方法等主要问题。这些因素影响数据同化链上遥感数据的冠层状态变量的估计精度。

(3) 方向问题——定量遥感中通常假设地表是理想朗伯体，从而进行各项推导，但是事实上，地面物体和电磁波相互作用不是各向同性的，并且具有明显的方向性。这种反射方向信息不仅包括光谱特征信息，还包含空间结构特征信息。一个复杂的检测环境可能具有相似的反射率（相同光谱的不同物体）并具有不同的反射率（同一物体的同义谱），从而导致模糊的结果。尝试探讨这方面的一些研究。1.基于场尺度的面向对象图像分析;它通过描绘来自多时间遥感图像的物体来获取各种纹理和空间特征以提高分类准确性;2.基于像素尺度的光学或雷达遥感图像;使用多时间光学或雷达遥感数据和机器学习方法来改善分类的准确性;3.基于像素尺度的光学和雷达遥感数据的组合;使用机器学习方法对多时相光学和雷达图像的不同组合进行评估，以更好地区分作物;4.基于像素或场规模的多分类器（机器学习方法）的组合;与使用单个分类器相比，两个或多个分类器的集成提供了改进的分类准确性。

(4) 尺度效应——由于自然环境非常复杂，地面物体在空间特征（空间异质性）方面存在很大差异。也就是说，地面物体在不同的空间尺度上显示的不同，它被称为尺度效应。不同地物的描述和研究需要根据不同的空间尺度进行。遥感技术为地球观测系统中的地球科学分析提供多空间和多时间分辨率数据，然后提供地面物体的不同空间尺度和时间数据。地面观测与不同尺度遥感数据之间的尺度转换是提高遥感数据应用效率和实用性的重要一步。此外关于高时空分辨率的权衡也是个关键问题。

(5) 反演策略和方法——遥感反演模型用于估算作物冠层状态变量是非常广泛的、准确的状态变量定量描述需要考虑太阳的角度，叶面积密度和叶角空间的分布，并且必须有足够的样本数量。然而，遥感信息有限，地表条件复杂多变，有用的遥感观测资料较少获得，估计作物冠层状态变量就越困难。主要包括经验和物理方法。当前关键问题之一是许多遥感反演是不适当的;没有问题的确切解决方案。遥感反演策略和方法，如何引入先验知识至关重要。另外，它涉及了对遥感数据的理解，遥感机制的研究，遥感模型的精度，遥感和非遥感数据融合，和时空表面元素的转换。

(6) 数据同化算法——目前的算法误差主要是指采样误差和各种数据同化方法的计算误差。采样误差是数据同化阶段的主要误差来源。大量的研究表明，采样数量的增加显着减少了采样误差，但增加了计算负担。计算错误来源于数据同化算法本身的问题。为了减少数据同化方法的误差，将不同数据同化算法的优点结合起来，进一步提高冠状态变量的估计精度（ENKF-3DVAR/4DVAR）。

(7) 观测数据——观测数据主要包括仪器和代表性误差。仪器误差主要是由仪器测量的缺陷造成的;主要原因是仪器无法准确测量所需数据。代表性误差主要包括区间（样本与区间之间的距离），范围（时空测量的覆盖范围）和覆盖范围（样本的平均面积）。上述误差在数据同化系统的计算过程中相互影响，因此很难量化这些相关项目的误差。在集合数据同化中，“净”误差的影响将使得误差协方差矩阵产生小的偏差，而在预测误差中产生新的空间特征。已经开发了一系列错误处理方法来减少当前数据同化系统中的这些错误。这些方法不是对模式先验误差和观测误差的估计，而是在整个链中减少了各种误差对数据同化系统的影响。

最后是未来的机遇。随着卫星的增多，可使用的遥感数据与观测数据越来越多。无人机数据、智能算法、物理光学方法与数据同化会进一步提升作物模拟的精度。

**Highlights:**

(1) 作物生长模型、遥感数据与数据同化最近的发展综述；

(2) 不同同化方法优缺点比较；

(3) 不同误差源对数据同化链中不同部分的影响分析；

(4) 它为今后的研究提供了进一步的机会和数据同化的发展方向。

**Research gap/question:**

作物生长模型、遥感数据与数据同化的整合用来提高模型预测精度。

**Discussion/Conclusion:**

(1) The main error sources include crop models, remote sensing data (directional problem, scale effect, retrieval strategy and method, and linking remote sensing model and crop model), data assimilation methods, and observation data. 数据同化的主要误差源包括作物模型，遥感数据（方向问题，尺度效应，反演策略与方法，遥感模型与作物模型的耦合），数据同化算法与观测数据。

(2) The data assimilation of remote sensing data and crop models will better improve the estimation accuracy of canopy state variables and yield based on new data assimilation algorithms by reducing the various errors of data assimilation chain in the future.通过减少未来数据同化链的各种误差，遥感数据和作物模型的数据同化将更好地提高基于新数据同化算法的冠层状态变量和产量的估计精度。

**Graph/Table interested:**

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/18.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/19.png)

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/20.png)

**Resources:**

无

# Mapping High Resolution Carbon Emission

## 1  China’s CO2 emissions estimated from the bottom up: Recent trends, spatial distributions, and quantification of uncertainties

**Title:** China’s CO2 emissions estimated from the bottom up: Recent trends, spatial distributions, and quantification of uncertainties/自下而上估计中国CO2排放：近期趋势，空间分布与不确定性的定量化 

**Link:** [原文链接](https://www.sciencedirect.com/science/article/pii/S1352231012004761?via%3Dihub)

**Doi:** 10.1016/j.atmosenv.2012.05.027

**Notes:** 这个研究是根据经济部门、省级经济与能源详细分类的数据，构建了一个自下而上的排放清单框架估算中国人类活动的CO2排放量。该研究包一个新编制采用中国最新实地调查的CO2排放量数据库。节能减排政策对限制电力和钢铁厂的CO2排放量作用较大，对于水泥生产没有什么影响。这篇文章是第一篇使用Monte-Carlo模拟定量化中国CO2排放量的不确定性。2005年总排放量的95%置信区间为-9%~+11%。对于行业排放不确定性最大贡献的是大部分工业园的排放因子与火电厂、交通、居住与商业排放源的活动水平。方法部分考虑了（火电厂、交通、居民、工业）四个大的清单排放源，每个部分还有细分下去的各类排放源。这里先有个定义：

Carbon Dioxide Emission = Acitivity Levels * Emission Factos 

AL（Activity Levels）， EF（Emission Factors）各自有其概率分布，进行10000 次Monte-Carlo模拟分析。有精细的排放因子对照表及对应的概率分布置信区间。

**Highlights:**

(1)  一个按行业确定的中国特有的CO2排放因子数据库；

(2) 基于自下而上方法估计的中国2005~2009年CO2排放；

(3) 使用Monte-Carlo模拟定量化了中国CO2排放不确定性；

(4) 提高能源效率减缓了某些行业二氧化碳排放量的增加。

**Research gap/question:**

全世界CO2排放最多的中国在估计CO2排放及不确定性上研究贫乏

**Discussion/Conclusion:**

(1) The difference can be attributed to the more detailed source categories in the current study, Which significantly reduce the random errors by the “compensation-of-error” mechanism realized through Monte-Carlo simulation. 数据差异的原因有可能是本研究更为精细的分类排放源，Monte-Carlo模拟中的误差补偿机制显著降低随机误差。

(2) Use of provincial-level energy statistics in the current work is likely the primary determinant of this difference. 使用省级能源统计数据可能是差异的主要原因（前文提到省级数据比全国数据更精确）。

(3) 政策影响和预测分析。

这篇文章主要的讨论点不是太明显，因为是把结果和讨论混在一起写到的，总体来说讨论部分除了上面我提到的两个关键点之外，就是跟IPCC等机构的数据做对比，还有对政策部分的一些预测，EF排放因子表是非常不错的数据，此外生成了一个以人口和经济分配得到的0.25°×0.25°的产品。

**Graph/Table interested:**

Tab.1 Emission Factors Table:

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/1.png)

Tab.2 Uncertainty of CO2

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/2.png)

**Resources:**

无

## 2 Effect of Urbanization on Carbon Dioxide Emissions Efficiency in the Yangtze River Delta, China
**Title:** Effect of Urbanization on Carbon Dioxide Emissions Efficiency in the Yangtze River Delta, China


**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

# Urban Computing and GIS
## 1 Characterizing mixed-use buildings based on multi-source big data
**Title:** Characterizing mixed-use buildings based on multi-source big data/基于多源大数据的混合功能建筑物分类

**Link:** [原文链接](https://www.tandfonline.com/doi/abs/10.1080/13658816.2017.1410549)

**Doi:** 10.1080/13658816.2017.1410549

**Notes:** 这个研究主要是集成了多源大数据（社交网络数据、出租车轨迹数据、POI兴趣点数据和遥感图像），利用一个概率模型来表征城市当中的混合功能建筑物的识别。并且以广州市天河区为例，模型分类精度达到了85%，同时对建筑物的空间分布模式进一步探究，大多数混合功能的建筑物都位于主要街道，而这个方法也将为小尺度城市规划评估和决策研究提供支持。文章主要重点是这个可以分类的概率模型。技术流程图如下：

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/8.png)

数据源有四个社交网络数据（腾讯宜出行平台的时空数据）、出租车轨迹数据、POI兴趣点数据以及建筑足迹（Quick Bird影像解译），多源大数据共计两天时间获取（一天周末，一天工作日）。First Stage：首先出租车轨迹数据先提取了上下车的地点，接着用POI数据基于贝叶斯原理进行修正，得到不同建筑物乘客乘出租车出行目的的最大概率，当有多个出行目的的最大概率，就认为是混合功能建筑物。后期用IDW插值，最后与建筑足迹数据叠加。Second Stage：随机选取一些建筑物通过POI和百度街景地图识别出建筑物功能作为训练样本，统计建筑物内微信使用者的数量。这里有一个假设，人由于特定的目的（休息、吃饭等 ）长时间位于固定地点（家、餐厅），这些被称为活动中心，而关键假设就是，同一种功能的建筑物与微信用户的日常活动有相同的高峰时间。接着使用核密度估计方法来识别这些功能，如果有多个高峰时期就认为是混合功能建筑物。First Stage和Second Stage叠加之后，可能结果存在差异，又构建了一个correctation rule来进行推断。

**Hightlights:**

(1) 一种集成多源大数据和概率模型表征城市混合功能建筑物识别的方法；

(2) 高精度分类模型；

(3) 混合功能建筑空间分布模式。

**Research gap/question:**

到目前为止很少有研究能成功整合多源大数据描述城市混合功能建筑物识别。

**Discussion/Conclusion:**

(1) Spatial distribution of mixed-use buildings. 混合功能区建筑物的分布与距城市中心的距离是一致的。从城市的内部到外部，建筑物的功能从混合到单一变化。

(2) Spatial interaction between human activities and buildings’ functions. 建筑物类型影响了人类活动，建筑物类型越复杂，混合程度越高，居民通勤距离就越短。

(3) Sources of inference errors. 多源数据，结构不同，采集时间也有差异。

IJGIS这篇文章的讨论部分偏向于研究结果的解释以及目前研究的不足缺陷。

**Graph/Table interested:**

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

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 3 Sensing Urban Land-Use Patterns By Integrating Google Tensorflow And Scene-Classification Models
**Title:** Sensing Urban Land-Use Patterns By Integrating Google Tensorflow And Scene-Classification Models


**Link:** [原文链接](https://arxiv.org/abs/1708.01580)

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 4 The Combined Use of Remote Sensing and Social Sensing Data in Fine-Grained Urban Land Use Mapping: A Case Study in Beijing, China
**Title:** The Combined Use of Remote Sensing and Social Sensing Data in Fine-Grained Urban Land Use Mapping: A Case Study in Beijing, China


**Link:** [原文链接](https://arxiv.org/abs/1711.03641)

**Doi:** 10.3390/rs9090865

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 5 Urban Land Use Mapping by Combining Remote Sensing Imagery and Mobile Phone Positioning Data
**Title:** Urban Land Use Mapping by Combining Remote Sensing Imagery and Mobile Phone Positioning Data


**Link:** [原文链接](http://www.mdpi.com/2072-4292/10/3/446/xml)

**Doi:** 10.3390/rs10030446

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 6 Spatio-Temporal Analytics for Exploring Human Mobility Patterns and Urban Dynamics in the Mobile Age
**Title:** Spatio-Temporal Analytics for Exploring Human Mobility Patterns and Urban Dynamics in the Mobile Age


**Link:** [原文链接](https://www.tandfonline.com/doi/abs/10.1080/13875868.2014.984300)

**Doi:** 10.1080/13875868.2014.984300

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 7 Simulating urban dynamics in China using a gradient cellular automata model based on S-shaped curve evolution characteristics
**Title:** Simulating urban dynamics in China using a gradient cellular automata model based on S-shaped curve evolution characteristics


**Link:** [原文链接](https://www.tandfonline.com/doi/abs/10.1080/13658816.2017.1376065)

**Doi:** 10.1080/13658816.2017.1376065

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 8 Identifying Local Spatiotemporal Autocorrelation Patterns of Taxi Pick-ups and Dropoffs
**Title:** Identifying Local Spatiotemporal Autocorrelation Patterns of Taxi Pick-ups and Dropoffs

**Link:** [原文链接](http://escholarship.ucop.edu/uc/item/04b2d8xp)

**Doi:** DOI10.21433/B31104B2D8XP

**Notes:**

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 9 Challenges and Prospects of Uncertainties in Spatial Big Data Analytics
**Title:** Challenges and Prospects of Uncertainties in Spatial Big Data Analytics

**Link:** [原文链接](https://www.researchgate.net/publication/322265057_Challenges_and_Prospects_of_Uncertainties_in_Spatial_Big_Data_Analytics)

**Doi:** DOI10.1080/24694452.2017.1421898

**Notes:**

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 10 Estimating Vehicle Fuel Consumption and Emissions Using GPS Big Data
**Title:** Estimating Vehicle Fuel Consumption and Emissions Using GPS Big Data


**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 11 Environmental benefits of bike sharing: A big data-based analysis
**Title:** Environmental benefits of bike sharing: A big data-based analysis


**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 12 Growth, innovation, scaling, and the pace of life in cities
**Title:** Growth, innovation, scaling, and the pace of life in cities


**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 13 Street as a big geo-data assembly and analysis unit in urban studies: A case study using Beijing taxi data
**Title:** Street as a big geo-data assembly and analysis unit in urban studies: A case study using Beijing taxi data


**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 14 The Combined Use of Remote Sensing and Social Sensing Data in Fine-Grained Urban Land Use Mapping: A Case Study in Beijing, China
**Title:** The Combined Use of Remote Sensing and Social Sensing Data in Fine-Grained Urban Land Use Mapping: A Case Study in Beijing, China


**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 15 Mapping China’s Ghost Cities through the Combination of Nighttime Satellite Data and Daytime Satellite Data
**Title:** Mapping China’s Ghost Cities through the Combination of Nighttime Satellite Data and Daytime Satellite Data

**Link:** [原文链接](http://www.mdpi.com/2072-4292/10/7/1037)

**Doi:** 10.3390/rs10071037

**Notes:**

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 16 Urban growth simulation by incorporating planning policies into a CA-based future land-use simulation model
**Title:** Urban growth simulation by incorporating planning policies into a CA-based future land-use simulation model
**Link:** [原文链接](https://www.tandfonline.com/doi/full/10.1080/13658816.2018.1502441)

**Doi:** 10.1080/13658816.2018.1502441

**Notes:**

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 17 Portraying Urban Functional Zones by Coupling Remote Sensing Imagery and Human Sensing Data
**Title:** Portraying Urban Functional Zones by Coupling Remote Sensing Imagery and Human Sensing Data
**Link:** [原文链接](http://www.mdpi.com/2072-4292/10/1/141)

**Doi:** 10.3390/rs10010141

**Notes:**

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

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

**Discussion/Conclusion：**

(1) The section on distance transforms in de Smith, Goodchild, and Longley (2009) also discusses 16-cell neighborhoods.Connecting in 16 directions may increase the accuracy of the calculations.16邻域的邻域计算法则可能会提高距离计算的精度。

(2) More research on the consequences of connecting grids in different ways is necessary, as indicated in Section 2. This should bring more precision to random walk calculations in geospatial analysis. Comparing the results of grid-based calculations to continuous space simulations or analytical solutions would be the way forward. 不同邻域设置导致研究后果差异是值得关注的，这些会提高计算精度。

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/6.png)

软件开发类文章讨论较少，Future Study是一个比较值得关注的点。

**Graph/Table interested：**

![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/7.png)

**Resources:**

[gdistance](https://github.com/cran/gdistance)

[circuitscape](http://www.circuitscape.org)


## 2 A New Set of Spatial-Interaction Models: The Theory of Competing Destinations
**Title:** A New Set of Spatial-Interaction Models: The Theory of Competing Destinations

**Link:** [原文链接](http://journals.sagepub.com/doi/pdf/10.1177/0308518X8301500103)

**Doi:** 10.1177/0308518X8301500103

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 3 Mapping local variation in educational attainment across Africa
**Title:** Mapping local variation in educational attainment across Africa

**Link:** [原文链接](https://www.nature.com/articles/nature25761)

**Doi:** 10.1038/nature25761

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 4 Spatiotemporal model for assessing the stability of urban human convergence and divergence patterns
**Title:** Spatiotemporal model for assessing the stability of urban human convergence and divergence patterns


**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 5 Designing an Experiment to Investigate Subpixel Mapping as an Alternative Method to Obtain Land Use/Land Cover Maps
**Title:** Designing an Experiment to Investigate Subpixel Mapping as an Alternative Method to Obtain Land Use/Land Cover Maps


**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 6 Spatial association detector (SPADE)
**Title:** Spatial association detector (SPADE)

**Link:** [原文链接](https://www.tandfonline.com/doi/abs/10.1080/13658816.2018.1476693?journalCode=tgis20)

**Doi:** 10.1080/13658816.2018.1476693

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**


## 7 Spatiotemporal Fusion of Multisource Remote Sensing Data: Literature Survey, Taxonomy, Principles, Applications, and Future Directions
**Title:** Spatiotemporal Fusion of Multisource Remote Sensing Data: Literature Survey, Taxonomy, Principles, Applications, and Future Directions

**Link:** [原文链接](http://www.mdpi.com/2072-4292/10/4/527)

**Doi:** 10.3390/rs10040527

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**


## 8 Modeling the Distributions of Brightness Temperatures of a Cropland Study Area Using a Model that Combines Fast Radiosity and Energy Budget Methods
**Title:** Modeling the Distributions of Brightness Temperatures of a Cropland Study Area Using a Model that Combines Fast Radiosity and Energy Budget Methods

**Link:** [原文链接](http://www.mdpi.com/2072-4292/10/5/736)

**Doi:** 10.3390/rs10050736

**Notes:**

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**


# Public Health and Environmental Risk Factors
## 1 Mapping child growth failure in Africa between 2000 and 2015
**Title:** Mapping child growth failure in Africa between 2000 and 2015

**Link:** [原文链接](https://www.nature.com/articles/nature25760)

**Doi:** 10.1038/nature25760

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**


## 2 Real-time and Seamless Monitoring of Ground-level PM2.5 Using Satellite Remote Sensing

**Title:** Real-time and Seamless Monitoring of Ground-level PM2.5 Using Satellite Remote Sensing

**Link:** [原文链接](https://www.researchgate.net/publication/323694623_Real-time_and_Seamless_Monitoring_of_Ground-level_PM25_Using_Satellite_Remote_Sensing)

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 3 Estimation of Ground PM2.5 Concentrations using a DEM-assisted Information Diffusion Algorithm: A Case Study in China

**Title:** Estimation of Ground PM2.5 Concentrations using a DEM-assisted Information Diffusion Algorithm: A Case Study in China

**Link:** [原文链接](https://www.nature.com/articles/s41598-017-14197-z?WT.feed_name=subjects_physical-sciences)

**Doi:** 10.1038/s41598-017-14197-z

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 4 Natural and Built Environmental Exposures on Children's Active School Travel: A Dutch Global Positioning System-based Cross-sectional Study

**Title:** Natural and Built Environmental Exposures on Children's Active School Travel: A Dutch Global Positioning System-based Cross-sectional Study

**Link:** [原文链接](http://europepmc.org/abstract/MED/27010106)

**Doi:** 10.1016/j.healthplace.2016.03.003  

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 5 The Uncertain Geographic Context Problem in the Analysis of the Relationships between Obesity and the Built Environment in Guangzhou

**Title:** The Uncertain Geographic Context Problem in the Analysis of the Relationships between Obesity and the Built Environment in Guangzhou

**Link:** [原文链接](http://europepmc.org/abstract/MED/29439392)

**Doi:** 10.3390/ijerph15020308

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 6 Spatio-Temporal Pattern Estimation of PM2.5 in Beijing-Tianjin-Hebei Region Based on MODIS AOD and Meteorological Data Using the Back Propagation Neural Network
**Title:** Spatio-Temporal Pattern Estimation of PM2.5 in Beijing-Tianjin-Hebei Region Based on MODIS AOD and Meteorological Data Using the Back Propagation Neural Network

**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 7 Spatiotemporal Distribution of Satellite-Retrieved Ground-Level PM2.5 and Near Real-Time Daily Retrieval Algorithm Development in Sichuan Basin, China
**Title:** Spatiotemporal Distribution of Satellite-Retrieved Ground-Level PM2.5 and Near Real-Time Daily Retrieval Algorithm Development in Sichuan Basin, China

**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**


## 8 Assessment of human health impact from exposure to multiple air pollutants in China based on satellite observations
**Title:** Assessment of human health impact from exposure to multiple air pollutants in China based on satellite observations


**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 9 High-Resolution Satellite Mapping of Fine Particulates Based on Geographically Weighted Regression
**Title:** High-Resolution Satellite Mapping of Fine Particulates Based on Geographically Weighted Regression


**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 10 Estimating national-scale ground-level PM25 concentration in China using geographically weighted regression based on MODIS and MISR AOD
**Title:** Estimating national-scale ground-level PM25 concentration in China using geographically weighted regression based on MODIS and MISR AOD


**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 11 Evaluation of machine learning techniques with multiple remote sensing datasets in estimating monthly concentrations of ground-level PM2.5

**Title:** Evaluation of machine learning techniques with multiple remote sensing datasets in estimating monthly concentrations of ground-level PM2.5

**Link:** [原文链接](https://www.sciencedirect.com/science/article/pii/S0269749118324229?via%3Dihub)

**Doi:** 10.1016/j.envpol.2018.08.029

**Notes:**

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

## 12 Spatiotemporal Distribution of Satellite-Retrieved Ground-Level PM2.5 and Near Real-Time Daily Retrieval Algorithm Development in Sichuan Basin, China
**Title:** Spatiotemporal Distribution of Satellite-Retrieved Ground-Level PM2.5 and Near Real-Time Daily Retrieval Algorithm Development in Sichuan Basin, China

**Link:** [原文链接](http://www.mdpi.com/2073-4433/9/2/78)

**Doi:** 10.3390/atmos9020078

**Notes:**

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**

# Urban Resilience and Disasters
## 1 Assessing local resilience to typhoon disasters: A case study in Nansha, Guangzhou
**Title:** Assessing local resilience to typhoon disasters: A case study in Nansha, Guangzhou

**Link:** [原文链接](https://doi.org/10.1371/journal.pone.0190701)

**Doi:** 10.1371/journal.pone.0190701

**Notes:**

**Hightlights:** 

**Research gap/question:** 

**Discussion/Conclusion** 

**Graph/Table interested:** 

**Resources:**




