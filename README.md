# 论文阅读笔记

| 项目 | 信息 |
|:--|:--|
| 作者 | 戴劭勍（Shaoqing Dai） |
| 主页 | <https://gisersqdai.top/mycv/> |
| GitHub | [@GISerDaiShaoqing](https://github.com/GISerDaiShaoqing) |
| 邮箱 | <dsq1993qingge@163.com> |
| ORCID | [0000-0003-0858-4728](https://orcid.org/0000-0003-0858-4728) |
| 在线笔记 | [Dai_PNS · Paper Note Studio](https://giserdaishaoqing.github.io/papers-notebook/) |
| License | MIT |

这里是 Dai_PNS 论文笔记仓库的入口。笔记正文以独立 Markdown 文件保存，桌面端用于编辑和精读，静态网站用于分类浏览与分享。

[打开在线笔记网站](https://giserdaishaoqing.github.io/papers-notebook/) · [查看分类与笔记索引](notes/INDEX.md)

## 完整笔记范例

下面五篇作为后续精读与写作的范例。图片资源保存在 `Picture/`。

- [R Package gdistance: Distances and Routes on Geographical Grids](notes/gis-remote-sensing-and-spatial-methods/r-package-gdistance-distances-and-routes-on-geographical-grids.md)
- [Characterizing mixed-use buildings based on multi-source big data](notes/urban-analytics-mobility-and-land-use/characterizing-mixed-use-buildings-based-on-multi-source-big-data.md)
- [China’s CO2 emissions estimated from the bottom up: Recent trends, spatial distributions, and quantification of uncertainties](notes/carbon-emissions-and-urban-development/chinas-co2-emissions-estimated-from-the-bottom-up-recent-trends-spatial-b078b474.md)
- [A simplified data assimilation method for reconstructing time-series MODIS NDVI data](notes/remote-sensing-data-assimilation/a-simplified-data-assimilation-method-for-reconstructing-time-series-mo-2377ffec.md)
- [Global patterns of tropical forest fragmentation](notes/forest-landscape-and-ecosystem-services/global-patterns-of-tropical-forest-fragmentation.md)

分类清单单独保存在 [notes/categories.json](notes/categories.json)，即使暂时没有笔记也会保留。维护和阅读标准见 [AGENTS.md](AGENTS.md)。

## Dai_PNS · Paper Note Studio

`app/` 提供 Markdown 编辑与预览、DOI 原文跳转、本地 PDF 阅读与高亮，以及可配置的 AI 助手。AI 请求只在用户点击相应操作后发送到配置的模型服务。Windows、macOS 和 Linux 构建由 GitHub Actions 分别生成。软件名取自 Dai 的 Paper Note Studio，显示名为 `Dai_PNS`。

笔记网站由 `notes/` 和 `Picture/` 自动生成。PowerShell 可运行 `scripts/serve_site.ps1` 预览；部署工作流位于 `.github/workflows/deploy-site.yml`。

## 论文精读 Skill

仓库内提供 Codex Skill：`$paper-reading`。它会参考上面的五篇范例，帮助起草或补充论文笔记。
