# 神以先知婚姻比喻以色列不忠 · 讲章学习站

## 🔗 三个链接

| | 链接 |
|---|---|
| 📦 **GitHub 仓库** | **<https://github.com/08-Ser-Grok-Je-Personal-20261003/hosea-marriage-unfaithful-israel-20261114-v1-GROKser>** |
| 🌐 **GitHub Pages** | **<https://08-ser-grok-je-personal-20261003.github.io/hosea-marriage-unfaithful-israel-20261114-v1-GROKser/>** |
| 🌐 **Surge** | **<https://hosea-marriage-unfaithful-israel-20261114-v1-grokser.surge.sh>** |

> 诗歌：圣诗第65首；韵诗21篇1–3节；韵诗18篇1–3节；诗篇23篇（只列编号，不含歌词）
> 读经：**何西阿书 1:1–11**　证经：**何西阿书 1:1–3**
> 题目：**神以先知婚姻比喻以色列不忠**
> 一、命令娶淫妇　二、比喻民淫乱　三、顺服显神心

这是一个多页静态讲章学习站，全部用简体中文，按欧陆改革宗传统编写：三项联合信条（海德堡要理问答、比利时信条、多特信经）加三大普世信经。

- 纯静态，不用 CDN，使用系统中文字体。
- 亮色／深色、玻璃拟态、可折叠目录、可折叠的讨论答案、响应式布局。
- 主线：神用先知的婚姻照出以色列的不忠；审判是真实的；「然而」把「非我民」称为「永生神的儿子」。这应许在基督为不忠的新妇舍命时成就。
- 页面用相对链接，放在仓库根目录或 GitHub Pages 子路径下都可以打开。

版本：**v1（2026-11-14）**，变更见 [CHANGELOG.md](CHANGELOG.md)。

## 页面一览

**核心页面（顶部导航）**

| 文件 | 内容 |
|---|---|
| `index.html` | 首页：一句话总结、最感动的3点、三点、学习路径 |
| `sermon.html` | **讲章**：逐节、词义、歌篾三种看法、三个名字与反转、家谱图、新妇主线、四闭环 |
| `background.html` | 背景·地图：作者、受众、约前755–715年、耶户与亚述；以色列／犹大示意图与耶斯列谷局部框 |
| `discussion.html` | 14 道讨论题；答案分析可折叠 |
| `memory.html` | 记忆：口诀、一页回忆、导图、流程、总结表、翻转卡片 |
| `creeds.html` | 三大信经干净阅读与背诵 |
| `compare.html` | 三大信经对比：为什么是三份而不是一份 |
| `worship.html` | 诗歌只列编号；韵诗暂按篇号附诗篇和合本；诗篇23篇 |

**参考资料（菜单「页面」中）**

| 文件 | 内容 |
|---|---|
| `tfu.html` | 信条精选（原文）。威斯敏斯特仅意译 |
| `extension.html` | 大图景（创世到启示录）、第2–3章、对照经文、圣约公式 |
| `hc.html` `bc.html` `cd.html` | 海德堡要理问答、比利时信条、多特信经全文 |
| `sources.html` | 资料来源与逐字核对报告 |
| `404.html` | 未找到页面 |

## 目录结构

```
├── *.html                 # 生成结果（连同 assets/ 即可部署）
├── assets/style.css       # 亮／暗、玻璃拟态、响应式、动画
├── assets/app.js          # 主题、可折叠目录、背诵、翻转卡片
├── content/*.html         # 源：front-matter + HTML + {{宏}}
├── data/
│   ├── bop.json           # ccifellowship.org 的信经／信条文本
│   ├── cuv_used.json      # 本站用到的和合本章节
│   └── source_pages/      # 信经简介等被引用页面的存档
├── tools/
│   ├── build.py           # 生成器（引句必须是原文子串）
│   ├── maps.py            # 示意图与导图、流程、家谱
│   ├── verify.py          # 在线重抓并逐字比对
│   ├── qa.py linkcheck.py # 375／768／1280 与深色；站内链接
│   ├── fetch/             # 重新抓取信条与和合本
│   └── deploy_surge.sh    # 部署到 surge（用本机已登录账号，不存密码）
└── reports/               # verify 与 qa 的结果（截图不入库）
```

## 如何修改内容

1. 编辑 `content/*.html`。开头是 front-matter（`title` `h1` `lead` `badges`，以 `---` 结束）。
2. **信经与信条不要手打**，用宏注入。构建时会断言引句是来源原文的子串：

| 宏 | 作用 |
|---|---|
| `{{bible:何1:1-11\|hl=2,10}}` / `{{bq:何1:2}}` | 和合本经文块 / 行内引句 |
| `{{hc:95}}` `{{hcm:21}}` `{{hcq:95\|片段}}` | 海德堡问答 |
| `{{bc:17}}` `{{bcq:17\|片段}}` | 比利时信条 |
| `{{cd:2.9}}` `{{cdq:2.9\|片段}}` | 多特信经（`34` 表示第三、四项） |
| `{{crq:apostles\|片段}}` | 三大信经引句 |
| `{{ccq:源键\|片段}}` | 已存档页面的引句 |
| `{{map:region}}` | `region` `jezreel` `family` `mindmap` `paths` `loop-redemptive` `triad` |

3. 生成：`python3 tools/build.py`（Python 3.10+，`beautifulsoup4`）。
4. 检查：

   ```bash
   python3 tools/verify.py
   python3 tools/build.py
   python3 tools/linkcheck.py
   python3 tools/qa.py
   ```

5. 重新抓取（可选）：在 `_src` 中运行 `tools/fetch/` 下的脚本。`_src/` 已列入 `.gitignore`，原始抓取缓存不入库。

## 部署

本仓库按 GitHub Pages 从 `main` 的根目录发布（已含 `.nojekyll`）。本页列出的 Pages 与 Surge 地址是预定发布位置；本次提交不执行部署。

**GitHub Pages**（仓库根目录）：

```bash
gh api -X POST repos/08-Ser-Grok-Je-Personal-20261003/hosea-marriage-unfaithful-israel-20261114-v1-GROKser/pages \
  -f 'source[branch]=main' -f 'source[path]=/'
```

**Surge**（使用本机已经登录的账号，仓库里不写密码或令牌）：

```bash
npx surge whoami
tools/deploy_surge.sh
```

默认域名：`hosea-marriage-unfaithful-israel-20261114-v1-grokser.surge.sh`。

## 资料来源与诚实说明

- 三大信经、海德堡要理问答、比利时信条、多特信经的中文全部来自 [ccifellowship.org](https://ccifellowship.org)，由 `tools/verify.py` 在线核对（见 `sources.html`）。
- 信经对比页若引用站内简介或恩约教会「我们的信仰」中的句子，同样只引用已抓取页面里的原句。
- 经文：和合本（getbible.net `cus`）。
- 地图是手绘示意图，不是比例图，也不是考古测绘图。亚述（尼尼微）与埃及在图外，用方向表示。
- **未抓取、只作转述的内容**都在 `sources.html` 标明：威斯敏斯特标准（仅意译）、年代、巴力崇拜、断奶年龄、歌篾婚史的释经争议、加尔文注释（仅释义）、希伯来词义。不把未打开的注释页写成引文。
- 诗歌只列编号。韵诗篇号对应诗篇是假定，不代表已核对某一教会的诗本。

## 许可

站点自写内容供教会与个人学习。信经和信条文本的版权与使用条件以 ccifellowship.org 为准；和合本为公有领域。
