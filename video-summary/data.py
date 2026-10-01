# -*- coding: utf-8 -*-
# 视频《Build & Sell with Claude Code (10+ Hour Course)》（Nate Herk）的中文讲解内容。
# 依据：视频英文自动字幕通读整理；截图时间点对应 img/t<秒>.jpg。

META = {"duration": 36005}

PARTS = [
    {"name": "入门与基础概念", "range": "00:00 – 58:57",
     "blurb": "为什么要学、在哪里用 Claude Code、怎么跟它说话，以及 token、上下文窗口和 CLAUDE.md 这些贯穿全课的基础概念。"},
    {"name": "动手做自动化并部署上线", "range": "58:57 – 3:05:46",
     "blurb": "用 WAT 框架（工作流 + 智能体 + 工具）亲手做出几个自动化，再把它们放到 Modal、trigger.dev 或定时任务里 24 小时运行。"},
    {"name": "进阶概念：项目架构与 RAG", "range": "3:05:46 – 3:32:59",
     "blurb": "CLAUDE.md 的最佳实践、.claude 目录与设置层级、常用斜杠命令，以及用多模态 embedding 做 RAG 知识库。"},
    {"name": "做网站和 Web 应用", "range": "3:32:59 – 5:00:02",
     "blurb": "把 n8n 工作流变成带前端的应用；做出不像“AI 生成”的网站；用视频帧做滚动驱动的 3D 动画网站；GitHub + Vercel 上线。"},
    {"name": "接入外部工具，打造个人助理", "range": "5:00:02 – 6:08:03",
     "blurb": "通过 MCP、API 和 CLI 接入 Firecrawl、Blotato、Google Workspace，最后把一切组合成一个了解你业务的执行助理。"},
    {"name": "高阶能力：Skills、子代理、团队、浏览器", "range": "6:08:03 – 7:42:30",
     "blurb": "把重复流程固化成 Skills，用子代理和 Agent Teams 并行分工，再让 Claude 直接操作浏览器。"},
    {"name": "工程化与效率技巧", "range": "7:42:30 – 8:25:06",
     "blurb": "上下文管理策略、Git/GitHub 与 worktree 并行开发，以及 32 个从入门到高阶的使用技巧。"},
    {"name": "商业化：从技能到收入", "range": "8:25:06 – 10:00:05",
     "blurb": "卖结果而不是卖技术；怎么找客户、7 天拿下第一个客户、怎么定价、怎么交付和收尾。"},
]

CHAPTERS = [
    # ---------------- 第 1 部分 ----------------
    {"part": 0, "start": "0:00", "cn": "课程大纲", "en": "Course Outline",
     "lede": "作者承诺带零基础学员成为 Claude Code 熟练用户：能做自动化、网站、应用，甚至拥有自己的 AI 执行助理。章节顺序按“如果重新学一遍，我会怎么学”来排，最后一部分讲怎么用这些技能赚钱。",
     "imgs": [("0:00:40", "课程章节总览")],
     "sections": [
         ("课程会讲什么", [
             "智能体（agentic）AI 市场的变化，以及为什么现在要学 Claude Code。",
             "环境搭建、基本操作、token 与上下文、<code>CLAUDE.md</code>。",
             "亲手做工作流并部署成 24/7 运行的自动化；项目架构、内置命令、RAG、网站、API 与 MCP、Google CLI。",
             "执行助理、Skills、子代理（sub-agents）、Agent Teams、浏览器自动化、权限与上下文管理、GitHub 与 worktree、趣味技巧。",
             "最后：如何把这些能力变现。",
         ]),
     ]},
    {"part": 0, "start": "1:14", "cn": "为什么要学", "en": "Why Learn This",
     "lede": "企业正在从“手工搭节点”的传统自动化转向智能体工作流。作者先讲清楚“自愈”的真实边界，再现场用 Claude Code 做了一个自动写 newsletter 的工作流，最后预告怎么把它卖出去。",
     "imgs": [("0:02:15", "智能体 AI 市场规模增长"), ("0:19:40", "一句话生成的品牌 newsletter"), ("0:23:40", "做“医生”，不做“药剂师”")],
     "sections": [
         ("市场与趋势", [
             "智能体 AI 市场约 70–80 亿美元，预计几年内涨到 400–930 亿美元；约 25% 的企业今年已在试点，2027 年预计达到 50%。",
             "n8n、Zapier 这类传统自动化要你画好每一步、自己处理边界情况，遇到意外就会坏，需要人工维护。",
             "能做到这些是因为：大模型已经足够稳定、能多步推理；有 Skills、MCP 等能力扩展；有 trigger.dev、Modal、Vercel 这类简单的部署平台；还有 Claude Code 让非程序员也能用。",
         ]),
         ("“自愈”的真实边界", [
             "你在 Claude Code 里亲自触发时，智能体就在旁边，出错能当场修、还能更新工具，这部分自愈能力是真实的。",
             "一旦部署成定时或 webhook 触发，部署出去的是<b>工作流和工具（代码）</b>，不是智能体本身，这时它更像确定性的传统自动化。作者认为这是好事：可预测的自动化才可靠。",
             "真正的优势在<b>构建过程</b>：传统方式是自己铺每一根铁轨，智能体方式是告诉施工队“从这里修到那里”；上线前再用各种“火车”反复压测。",
             "基础知识仍然重要：懂 webhook 和 API，才能看出智能体哪里做错了，也才能把需求说清楚。",
         ]),
         ("现场演示：newsletter 工作流", [
             "VS Code 安装 Claude Code 扩展 → 打开一个空文件夹（一个文件夹就是一个项目）→ 放入作者提供的 WAT 框架 <code>CLAUDE.md</code>，让 Claude 初始化项目结构。",
             "切到<b>计划模式</b>，用一段很模糊的需求描述：研究主题、生成好看的 HTML、配几张信息图。Claude 反问：要不要接 Perplexity 搜索？用 Beehiiv 还是 Gmail 发？有没有品牌素材？",
             "看过计划后改成用 Nano Banana（通过 key.ai）生图；拖入 logo 和品牌规范，用 <code>@</code> 直接引用文件。",
             "确认后切到 bypass 权限执行：生成 2 个配置文件、5 个 Python 工具（研究、生图、拼 HTML、Gmail 发送、归档到表格）和 1 个 Markdown 工作流，再把 API key 填进 <code>.env</code>。",
             "运行中它自己修好了 Unicode 编码错误，还查文档发现生图接口的地址变了，顺手改好工具；中途停下让人挑主题行。第一封邮件 HTML 是乱的，一句话反馈后就修好了。",
         ]),
         ("Skills 与变现预告", [
             "Skills 就是需要时才加载的系统提示，比如 frontend-design skill 能明显提升网页设计质量；跑顺的流程也可以沉淀成自己的 skill。",
             "要做诊断问题的“医生”，而不是照方抓药的“药剂师”。和老板沟通时讲“每月帮你省多少时间、减少多少错误”，不讲“我用 Claude Code 做智能体工作流”。",
             "不要按小时收费：30 分钟做出来、每周帮企业省 20 小时的东西，一年值几万美元。例：每月帮客户省 1 万美元，收 5000 美元，客户两周回本。",
             "一个 3000 美元的项目可以发展成每年 5 万美元的长期合作，前提是你主动追踪并展示指标。路径是：自由职业者 → 顾问 → 可信赖的合作伙伴。",
         ]),
     ],
     "terms": ["Agentic workflow", "Self-healing", "WAT framework", "Plan mode", "Value-based pricing"]},
    {"part": 0, "start": "26:08", "cn": "环境搭建：五种使用方式", "en": "Getting Set Up",
     "lede": "Claude Code 可以在终端、桌面应用、网页、IDE 扩展和 VPS 上跑。它们背后是同一个引擎，只是外壳不同。作者逐一讲了每种方式的样子、优缺点、怎么装、适合谁。",
     "imgs": [("0:27:00", "五种运行方式"), ("0:34:40", "IDE 集成"), ("0:38:20", "VPS 托管")],
     "sections": [
         ("1. 终端（CLI）", [
             "所有其他界面都是包在这个引擎外面的壳。控制力最强、命令最全、新功能往往先上终端；可以自定义 <code>/statusline</code>，也可以用 <code>ultrathink</code>。",
             "缺点：纯文本，看不到文件全貌，对不熟悉终端的人学习曲线陡。",
             "安装：照官方 Quick Start 运行一条命令，需要付费订阅（Pro / Max / Teams / Enterprise）；<code>cd</code> 进项目文件夹后输入 <code>claude</code> 就能开始。",
         ]),
         ("2. 桌面应用", [
             "Chat / Cowork / Code 三个入口，图形界面优先：逐行查看并接受或拒绝修改、内置应用预览、多会话各自隔离在不同分支，还有原生的<b>定时任务</b>。",
             "缺点：可定制性低、版本可能落后 CLI、只支持 Mac 和 Windows；有些命令（例如 <code>/agents</code>）要切到终端才能用。",
         ]),
         ("3. 网页版（claude.ai/code）", [
             "研究预览阶段。连接 GitHub 仓库后在 Anthropic 云端克隆运行，关掉电脑也会继续跑，手机或 iPad 都能用，可以直接提 PR。",
             "Claude Code 作者 Boris Cherny 的用法：终端里并行 5 个，网页上再并行 5–10 个。不必只选一种。",
         ]),
         ("4. IDE 扩展（作者每天用的方式）", [
             "VS Code、Cursor、Antigravity 都是 IDE（集成开发环境）。装上 Claude Code 扩展后，Claude 能看到你打开和选中的内容，左边看文件、右边聊天。",
             "Git 颜色提示：绿色是新文件，黄色是已修改。可以在计划上逐条加评论；标签上的蓝点表示 Claude 在等你回复，橙点表示已完成；可以分屏同时跟多个智能体对话。",
             "遇到只有 CLI 能用的命令，就在 IDE 内置终端里运行，两边兼顾。",
         ]),
         ("5. VPS（虚拟专用服务器）", [
             "在自己租的服务器上跑（作者用 Hostinger，约 6 美元/月起），一直在线，并且靠近你的 Docker、数据库和自动化服务。",
             "作者接了一个 Telegram 桥，在手机上就能跟服务器上的 Claude Code 聊天；本地终端、VS Code、桌面应用也都能 SSH 连进去。",
             "缺点：需要一点服务器知识，配置更麻烦；Claude 能看到整台服务器，所以要格外注意权限。",
         ]),
     ],
     "terms": ["CLI", "GUI", "IDE", "VPS", "SSH", "Research preview"]},
    {"part": 0, "start": "41:25", "cn": "基本操作", "en": "Operations",
     "lede": "Claude Code 几乎什么都能做。作者希望你带着好奇心去用它：看它的思考过程，不懂就问。这一章讲了费用、提示词、权限模式和模型选择。",
     "imgs": [("0:41:40", "Claude Code 能做什么"), ("0:48:20", "三种权限模式"), ("0:49:20", "Haiku / Sonnet / Opus 对比")],
     "sections": [
         ("能做什么、该带什么心态", [
             "应用、网站、自动化、游戏、个人工作流、调试/重构/测试、API 集成、文档、Git、数据分析、内容流水线；配合浏览器工具还能截图、点击、填表。",
             "核心心态是<b>真正的好奇心</b>：读它在想什么、运行了什么命令；不懂就追问，甚至让它出练习题帮你理解概念。",
         ]),
         ("费用", [
             "必须付费。Pro 约 17 美元/月（按年付），但很容易撞到用量上限，作者建议直接上 Max（100 或 200 美元/月）。",
             "换个角度算：软件工程师月薪约 1.1 万美元，这相当于把一个工程师装进笔记本电脑。Anthropic 内部只用 2–3 人、大约 10 天就用 Claude Code 做出了 Cowork。",
         ]),
         ("提示词（Prompting）", [
             "垃圾进，垃圾出。把 Claude 想成刚雇来的聪明承包商：能力很强，但从没见过你的项目。",
             "差的提示：“给我的遛狗生意做个网站”。好的提示：给 Happy Paws 做一个简单落地页，有标题区（hero）、三项服务及价格、底部联系表单，蓝白配色、简洁现代。",
             "把提示放进计划模式，再加一句“有 95% 把握之前继续问我问题”。作者大量使用语音输入，说话比打字快，想法也更完整。",
         ]),
         ("权限模式", [
             "<b>Plan</b>（计划）：能读、能搜网页、能思考，不会动手改任何东西。",
             "<b>Accept edits / Edit automatically</b>：可以直接读写文件，但执行 bash 命令要先问你。另有 Ask before edits 模式，改文件前也要问。",
             "<b>Bypass permissions</b>：完全自主。需要在设置里开启 “allow dangerously skip permissions”。常用做法是先在计划模式把方案定好，再切到 bypass 让它一口气执行。",
         ]),
         ("模型", [
             "Haiku 最快、最便宜；Sonnet 均衡，适合日常编码；Opus 推理最强，也最慢最贵。用 <code>/model</code> 切换。",
             "常见建议是 80% 的工作用 Sonnet，遇到架构决策或棘手 bug 再切 Opus。作者自己几乎全程用 Opus，只在子代理或大量 token 处理时用 Haiku。",
         ]),
     ],
     "terms": ["Prompting", "Plan mode", "Accept edits", "Bypass permissions", "Haiku / Sonnet / Opus"]},
    {"part": 0, "start": "50:53", "cn": "Token 与上下文窗口", "en": "Tokens and Context Windows",
     "lede": "AI 按 token 读写，也按 token 计费。上下文窗口是 Claude 的“工作记忆”，塞得越满效果越差。这是后面所有上下文管理技巧的基础。",
     "imgs": [("0:51:10", "什么是 token"), ("0:53:20", "上下文腐化示意曲线")],
     "sections": [
         ("Token", [
             "一个 token 大约 3–4 个字符，约等于 0.75 个英文单词；逗号、句号这些标点也各算一个，所以并不完全一致。",
             "token 就是钱：订阅额度按 token 消耗，用得越多越快撞上限。",
         ]),
         ("上下文窗口（Context window）", [
             "可以想象成 Claude 的记事本，里面记着系统提示、工具定义、<code>CLAUDE.md</code>、MCP 服务器、所有对话历史和读过的文件。录制时标准大小约 20 万 token。",
             "<b>Lost in the middle</b>：对话开头和结尾的信息会被优先关注，中间的容易被忽略。",
             "<b>Context rot（上下文腐化）</b>：token 越多，准确率下降越明显，所有模型都这样。如果 Claude 突然开始胡编，就压缩一下或开新会话。",
         ]),
         ("相关命令", [
             "<code>/context</code>：查看当前 token 占用明细。演示里一个新会话就已经用了 2.2 万 / 20 万（11%），大头是系统提示、工具、MCP、skills 和 agent 文件。",
             "<code>/compact</code>：压缩对话、保留关键信息继续干活；<code>/clear</code>：清空重来；<code>/rewind</code>：回退到之前的某一步。",
             "Claude Code 还会在接近上限时 auto-compact。刚开始不必太焦虑，但要有这个意识，后面的课程会细讲。",
         ]),
     ],
     "terms": ["Token", "Context window", "Lost in the middle", "Context rot", "/context", "/compact", "Auto-compact"]},
    {"part": 0, "start": "55:10", "cn": "CLAUDE.md 与内置工具", "en": "Claude.md",
     "lede": "<code>CLAUDE.md</code> 就是项目的系统提示：你每发一条消息，Claude 都会先读它。因为每次都要读，所以要写得精简。章节开头还快速认识了 Claude Code 的内置工具。",
     "imgs": [("0:57:30", "CLAUDE.md 的三层：What / Why / How"), ("0:58:40", "示例：执行助理的 CLAUDE.md 开头")],
     "sections": [
         ("内置工具：认得就行，不用背", [
             "<b>Read / Write / Edit</b>：读、写、改文件；<b>Bash</b>：在终端执行命令；<b>Glob / Grep</b>：按文件名或内容查找；<b>LS</b>：列文件；<b>WebFetch</b>：抓取网址内容；<b>WebSearch</b>：网页搜索。",
             "看到这些词就知道它在找文件还是在跑命令。演示里生成图片时，先用 skill，再 Glob 找到 logo，最后用 Bash 跑脚本。",
         ]),
         ("怎么写 CLAUDE.md", [
             "MD 是 Markdown：用 # 表示标题、* 表示强调，不是代码，任何人都能读懂。",
             "三层内容：<b>What</b>（技术栈、项目结构、关键包或 skills）、<b>Why</b>（每个部分的用途）、<b>How</b>（你希望 Claude 怎么工作）。",
             "示例：“你是 Nate Herk 的执行助理，目标是让他少花时间在运营和行政上，专心学 AI 工具、做 YouTube 视频。”然后指向关于“我、工作、团队、优先级”的单独文件，而不是全写在里面。",
             "Claude 本身就很擅长写 <code>CLAUDE.md</code>。已有代码的项目可以运行 <code>/init</code>，它会扫描代码库自动生成一份。",
         ]),
     ],
     "terms": ["CLAUDE.md", "System prompt", "Markdown", "/init", "Bash", "Glob / Grep"]},

    # ---------------- 第 2 部分 ----------------
    {"part": 1, "start": "58:57", "cn": "第一个工作流", "en": "Building Your First Workflow",
     "lede": "传统自动化是“告诉系统每一步怎么做”，智能体工作流是“告诉它你要什么结果，剩下的它自己想办法”。本章介绍 WAT 框架，并从零做出一个生成品牌化 PDF 的竞品分析工作流。",
     "imgs": [("1:03:10", "W：Workflows（工作流）"), ("1:14:30", "计划模式产出的实施方案"), ("1:24:10", "最终的竞品分析 PDF 报告")],
     "sections": [
         ("确定性与非确定性", [
             "<b>确定性（deterministic）</b>：每次结果可预测，作者说“无聊就是美”；<b>非确定性（non-deterministic）</b>：同样的输入不一定得到同样的输出，AI 天生如此。",
             "AI 自动化从业者的工作，就是把非确定性的流程尽量做成确定性的，因为大部分业务流程本来就应该是确定的。",
             "比喻：传统自动化像拿纸质地图和指南针自己找路；智能体工作流像打开手机导航，走错了它会自动重新规划。",
         ]),
         ("WAT 框架", [
             "<b>W = Workflows（工作流）</b>：用 Markdown 写的 SOP，写明目标、需要的输入、用哪些工具、期望输出和边界情况，可以把它想成岗位说明或菜谱。",
             "<b>A = Agent（智能体）</b>：就是 Claude Code 本身，像项目经理，读工作流、决定调用哪个工具、出错时排查并调整。",
             "<b>T = Tools（工具）</b>：Python 脚本，每个只做一件事（抓网页、生成 PDF……），由 Claude 自动编写和修复，可以被不同工作流复用；API key 放在 <code>.env</code> 里，不写进代码。",
             "为什么需要结构：就像储物柜要有隔板和文件夹。<code>CLAUDE.md</code> 里还写了：先找现成工具；失败时读报错 → 修脚本 → 重测 → 更新工作流（自我改进循环）。如果每一步准确率 90%，五步串起来只剩 59%，这就是要靠工具保证确定性的原因。",
         ]),
         ("演示：竞品分析工作流", [
             "设置：下载 VS Code → 安装扩展 → 打开空文件夹 → 拖入 <code>CLAUDE.md</code> → 让它建好 <code>tools/</code>、<code>workflows/</code>、<code>.tmp/</code> 目录，然后 <code>/clear</code>。",
             "计划模式里用大白话描述需求，Claude 先探索项目再提问：竞品怎么找（自动发现）、要收集哪些业务信息、分析哪些维度、品牌素材从哪来、多久跑一次、预算多少。",
             "最终方案：Claude Sonnet + Firecrawl + Perplexity 做研究，ReportLab 生成 PDF，Matplotlib 画图；5 个工具加 1 个工作流；预先考虑反爬、限流、竞品不足等边界情况；首轮成本估计约 1.5 美元，之后有缓存会更便宜。",
             "拖入 logo 和品牌规范图后，它会自动提取颜色和字体。在 <code>.env</code> 里填好 Anthropic 和 Firecrawl 的 key。",
             "运行：它发现缺少业务信息，就主动提问，并把答案存成 <code>business_profile.json</code>；自己修好 Windows 下的 Unicode 报错；找到 Apollo、Outreach、Clay、Instantly、Lemlist 等竞品，每家建一个文件。",
             "第一版 PDF 的白色 logo 和图表看不见，一句“看不到图表和 logo，排查并修复”之后，第二版正常，还多了定价对比图。这次运行花了约 1.43 美元。",
         ]),
         ("小习惯", [
             "上下文用到 60% 左右就清空或压缩，避免上下文腐化。",
             "学习方法：每次都把它的每一行输出读一遍，看到不懂的（比如 glob pattern）就直接问。",
         ]),
     ],
     "terms": ["Deterministic", "Non-deterministic", "Workflows / Agent / Tools", "SOP", ".env", "Self-improvement loop"]},
    {"part": 1, "start": "1:25:05", "cn": "第二个工作流", "en": "Building Second Workflow",
     "lede": "换一个场景再练一遍，重点是 MCP：把 Firecrawl 的 MCP 服务器接给 Claude，让它自己决定用哪种抓取方式。作者连做三个抓取任务，最后一个是完全没准备过的需求。",
     "imgs": [("1:27:30", "WAT 框架示意"), ("1:33:30", "MCP：模型上下文协议"), ("1:39:40", "抓取的 209 条职位 Excel"), ("1:44:40", "牙医线索表")],
     "sections": [
         ("复习与补充", [
             "比喻：智能体是厨师，工作流是菜谱，工具是鸡蛋、面粉这些原料。工作流是 Markdown，工具是 <code>.py</code> 文件，那些“难看的代码”你不需要读。",
             "作者只有坐在旁边盯着的时候才开 bypass 权限，跑偏了随时拉回来。",
         ]),
         ("MCP（Model Context Protocol）", [
             "像超市：不用分别去蛋店、面粉店、糖果店，接入一次，智能体自己决定拿哪个工具、填什么参数。",
             "安装 Firecrawl MCP：把官方文档里“在 Claude Code 中运行”的命令交给 Claude；API key 不直接贴进对话，而是让它在 <code>.env</code> 放占位符，你自己填。",
             "注意：Claude 执行安装命令时仍可能把 key 写进对话历史。风险高的 key 应该让 Claude 教你在自己的终端里运行。",
         ]),
         ("三个演示", [
             "<b>职位抓取</b>：dailyremote 上 622 个社媒岗位分布在 21 页，先只抓 200 条验证可行性。生成 <code>scrape_daily_remote_jobs</code> 工具和 <code>scrape_job_listings</code> 工作流，得到 209 条、自带筛选的 Excel。",
             "<b>模糊需求</b>：“欧洲销售岗，要 500 条”。它发现欧洲只有 52 条，就主动问是否扩大范围；加上美国后得到 372 条，还多了地区列。",
             "<b>全新需求</b>：“帮我找美国牙医的联系方式”。ADA 官网是 JS 动态加载，就改用 Yellow Pages；正则只抓到 2 个，它自己修好；最后得到 4 个城市 120 条（电话、地址、网站、专长），并沉淀成可复用工具。",
             "上下文剩 45% 时点击压缩，摘要后继续，重要信息仍然保留。",
         ]),
         ("两大常见错误", [
             "<b>目标不清</b>：“我要一个 LinkedIn 线索抓取器”太模糊。应该在计划模式说“这是我的粗略想法，帮我写成完整的 PRD（需求文档）”。",
             "<b>没定义“完成”</b>：不说终点，它可能过度复杂、一直循环。要说“恰好 75 个科技公司 CEO 的 LinkedIn，放进表格，凑够 75 个就停”。",
         ]),
         ("智能体工作流的三大好处", [
             "不用再陷入调试循环（它会自愈）；用自然语言控制，不用学每个节点和 API；每次出错都会学习并更新，越用越聪明。",
             "但要记住：定时或事件触发的部署只上线了工作流和工具，没有智能体在场，也就没有实时自愈。",
         ]),
     ],
     "terms": ["MCP (Model Context Protocol)", "PRD", "Definition of done", "Context compaction"]},
    {"part": 1, "start": "1:50:43", "cn": "部署自动化", "en": "Deploying Automations",
     "lede": "这是全课最长的一章（约 75 分钟）：先做一个 YouTube 赛道周报工作流，接着讲 MCP 和 Skills 的区别，然后分别部署到 Modal 和 trigger.dev，最后介绍桌面版原生定时任务和 <code>/loop</code> 循环。",
     "imgs": [("1:56:25", "n8n 工作流与 WAT 对照"), ("2:10:20", "MCP 架构示意"), ("2:19:20", "使用 skill 后的品牌化 PDF"), ("2:29:30", "trigger.dev"), ("2:48:40", "桌面应用里的定时任务"), ("2:58:20", "/loop 循环示意"), ("3:04:00", "loop 与定时任务对比")],
     "sections": [
         ("演示：YouTube AI 赛道周报", [
             "计划模式描述需求后，它边规划边上网调研怎么拿 YouTube 数据。问答：自动发现热门频道、每周一次、导出 Google Sheets、Gmail 发送。",
             "生成 7 个 Python 工具：拉数据、分析、画图、生成幻灯片、发邮件、导出表格、发现频道。安装依赖、配置 YouTube API key 和 Google OAuth 后首跑：30 个频道、187 个视频、6 张图、9 页 PPT，还自动建好了三个 Sheets 标签页（频道统计、热门视频、周汇总）。",
         ]),
         ("MCP 与 Skills 的区别", [
             "<b>MCP</b>：拿数据、执行动作，像“万能 USB 接口”，连一次就能用到整个服务的所有端点。",
             "<b>Skills</b>：知识和自定义说明，按需加载。Claude 先看所有 skill 的简介，只有相关的才读全文，所以省 token、更稳定。",
             "Skills 可以全局安装（所有项目都能用）或只装在当前项目。从 Claude Code Templates 网站安装了 canvas-design skill，把输出从 PPT 换成带 logo 的 PDF；第一版只有 2 页，反馈后变成 9 页完整报告。",
         ]),
         ("部署到 Modal", [
             "Modal 是按运行次数计费的云端算力，注册送 5 美元，绑卡再送 30 美元。可以直接说“帮我把这个工作流推到 Modal”。",
             "上线前先让 Claude 做<b>安全审查</b>：API key 有没有暴露、webhook 有没有保护。key 和 OAuth token 都存成 Modal secrets，不进任何仓库。",
             "设置为每周一早上 6 点（芝加哥时间）运行。手动跑失败了，把日志复制给 Claude，原来是测试太多，用完了 YouTube Data API 每天 1 万的配额。另外演示了 webhook 触发：用 Postman 发请求 → Perplexity 调研公司 → 发邮件通知。",
             "跑通后让它把部署流程写成 skill 或记进 <code>CLAUDE.md</code>，下次直接复用。",
         ]),
         ("部署到 trigger.dev", [
             "相比 Modal 更灵活：定时运行、自动重试、队列、任务编排，界面也更清爽。还能把非确定性的“智能体”放到云端：ClickUp 里新建一个公司任务 → 研究智能体搜索并阅读网页 → 写评论回复；在评论里追问，它还会继续回答。",
             "演示：每周一 8 点找全美牙科诊所线索写进 ClickUp。Yelp 已取消免费 API，它自动改用 SerpAPI。先在 dev 环境测试：<code>.env</code> 不会被推送，所以环境变量要在 trigger.dev 后台再配一遍；配好 trigger.dev MCP 后，25 条线索 9 秒建完。",
             "发现有重复线索：改成先按 place ID 查询再创建（幂等 idempotency）。连接 GitHub 仓库后，每次推送到 master 就自动部署到生产环境。",
         ]),
         ("原生定时任务（Scheduled tasks）", [
             "桌面应用的 Schedule 标签或 <code>/schedule</code>：填名称、提示词、模型、模式、文件夹和频率。到点后启动一个会话，智能体读提示、在项目里干活，干完停止。",
             "这是真正的 Claude Code 智能体在跑，能读整个项目、能自修；如果想要确定性，也可以让任务只执行一个脚本。作者把每天手动跑的 morning coffee skill 一句话改成了每天 6 点自动跑。",
             "限制：电脑要开着、桌面应用要打开；错过的任务会在 7 天内补跑。无人值守要提前配好权限（比如禁止删除类命令），缺 key 或权限时任务会卡住，所以新建后先手动跑一遍。",
             "每次运行都是全新会话（无状态）。可以“每个任务一个状态文件，开始前先读，结束后覆盖”，让下一次运行知道上次发生了什么。通知方式可以用 hook 播放提示音，或在提示词末尾让它发一条 ClickUp 消息。",
         ]),
         ("/loop 与 cron", [
             "<code>/loop 每 5 分钟检查部署状态</code>，或一次性提醒“10:40 提醒我倒垃圾”。CLI、桌面、IDE 都能用，底层是 CronCreate / CronList / CronDelete 三个工具。",
             "按会话隔离，另一个会话看不到；3 天后自动过期；关闭会话就失效，也不会补跑。好处是同一会话能连续看到上一次的结果，代价是上下文会越积越多。",
             "怎么选：今天盯着这个项目 → <code>/loop</code>；每天、每周长期跑 → 定时任务。",
         ]),
     ],
     "terms": ["Modal", "trigger.dev", "Cron", "Webhook", "Idempotency", "Dev / Prod", "Scheduled tasks", "/loop"]},

    # ---------------- 第 3 部分 ----------------
    {"part": 2, "start": "3:05:46", "cn": "项目架构与命令", "en": "Project Architecture & Commands",
     "lede": "作者说这是自己刚入门时最困惑的部分：<code>CLAUDE.md</code> 怎么写才好、全局和项目级配置有什么区别、哪些斜杠命令值得记、设置文件的优先级是怎样的。",
     "imgs": [("3:06:30", "好的 CLAUDE.md 包含什么"), ("3:14:10", ".claude 目录结构"), ("3:15:20", "各文件用途与是否共享")],
     "sections": [
         ("CLAUDE.md 最佳实践", [
             "一份好的 <code>CLAUDE.md</code> 包含：项目概述、技术栈、架构概览、代码规范、常用命令、约束条件，以及去哪里找更多上下文。",
             "控制在 200 行以内（作者自己约 100 行），越短越省 token。要具体：“用两个空格缩进”比“格式整齐点”好得多。",
             "当成活文档，作者几乎每天都在改。偶尔才用到的规则（比如写邮件的口吻）放进 <code>rules/</code>，在 <code>CLAUDE.md</code> 里写一句“需要时去那里看”，这叫<b>路由（routing）</b>。<code>CLAUDE.md</code> 是目录，不是百科全书。",
         ]),
         ("全局与项目级、自动记忆", [
             "<code>~/.claude</code>（带波浪号）是全局配置，对你所有项目生效；项目里的 <code>.claude/</code> 只对当前项目生效。某个设置每个项目都要用，就放全局。",
             "Auto memory：你说“总是用 pnpm，不要用 npm”，Claude 会把它记进全局记忆文件，跨会话生效，可以用 <code>/memory</code> 随时编辑，类似网页版的记忆功能。",
         ]),
         ("值得知道的斜杠命令", [
             "会话管理：<code>/init</code>、<code>/clear</code>、<code>/compact</code>（可以带说明，例如“/compact 只保留网站设计相关的信息”）、<code>/rewind</code>（撤销）、<code>/resume</code>（恢复几天前的会话）。",
             "信息诊断：<code>/context</code>、<code>/cost</code>、<code>/model</code>、<code>/help</code>、<code>/doctor</code>（检查安装状态）、<code>/status</code>（版本、模型、账号）。",
             "配置：<code>/memory</code>、<code>/config</code>、<code>/permissions</code>、<code>/mcp</code>、<code>/agents</code>。不用背，直接问它“有没有命令能做 X”就行。",
         ]),
         ("设置文件层级", [
             "<code>~/.claude/settings.json</code>：个人默认；<code>.claude/settings.json</code>：团队共享的标准；<code>.claude/settings.local.json</code>：只属于你的覆盖设置。",
             "检查顺序是 local → project → global，任何一层说“不允许”就会停下。",
             "项目级 <code>.claude/</code> 里可能有 settings、<code>CLAUDE.md</code>、rules、skills、agents、commands；外面还可能有 MCP 配置文件。",
         ]),
         (".gitignore 与颜色提示", [
             "<code>.gitignore</code> 列出不推到 GitHub 的文件：<code>.env</code>、密钥、私人照片等。在 VS Code 里这些文件显示为灰色。",
             "绿色是 Git 从没见过的新文件，黄色是已修改未提交。全部推送后都会变回白色，一眼就知道该不该保存进度。",
         ]),
     ],
     "terms": ["Routing", "~/.claude", "settings.local.json", "Auto memory", ".gitignore", "/resume", "/doctor"]},
    {"part": 2, "start": "3:17:39", "cn": "RAG：多模态知识库", "en": "RAG",
     "lede": "Google 推出了首个原生多模态 embedding 模型 Gemini Embedding 2，文本、图片、视频、音频和文档可以放进同一个向量空间。作者用 Claude Code 在 30 分钟内做出两个可用的演示，并现场从零搭了一个。",
     "imgs": [("3:18:20", "单模态与多模态 embedding"), ("3:21:00", "屋顶图片相似项目检索"), ("3:23:20", "向量数据库 RAG 流程"), ("3:24:10", "多模态向量的 2D 分布图")],
     "sections": [
         ("两个演示", [
             "<b>说明书问答</b>：一份 68 页的吸尘器说明书 PDF，一句话让 Claude Code 建好 Pinecone 库和聊天应用。问“怎么清洗滤网”，返回步骤、对应的原图（还有多语言版本），以及来源页码和匹配度。",
             "<b>屋顶相似项目</b>：13 张屋顶照片，每张带造价、工期、人数等元数据。上传新照片就能找到 5 个相似的历史项目，给出报价区间和团队规模。作者承认数据是编的，真实使用需要行业知识。",
             "在 n8n 里做多模态知识库很脆弱，要处理分块、图片存储和描述；这里两个演示加起来不到 30 分钟。",
         ]),
         ("RAG 原理", [
             "RAG = 检索增强生成（Retrieval-Augmented Generation）：模型训练数据里没有的信息，先<b>检索</b>出来，<b>增强</b>上下文，再<b>生成</b>回答。",
             "把文档切成块（chunk）→ 送进 embedding 模型 → 得到一组数字（向量），按语义落在多维空间里，例如公司概况、财务、营销各聚一处。",
             "作者的测试图：狗弹吉他的视频落在“娱乐/视频”，笑脸薯条的图片落在“食物/图片”，教程文本落在“技术/文本”。换成全是屋顶照片，就会按“水损”“老化”等含义分开。",
         ]),
         ("从零搭建", [
             "计划模式贴入 Google 文档的 embedding API 页面地址，要求建一个装视频、图片和文本的 Pinecone 库，并在 <code>.env</code> 放占位符。",
             "需要三把 key：Pinecone（免费 starter 够用）、Google AI Studio（Gemini）、OpenRouter（一个 key 调各家模型）。",
             "把 9 个混合文件直接丢进 <code>data/</code>，不用分类。构建用 Opus，网页聊天模型用 Sonnet；发现它理解错了就直接打断纠正，上下文不会丢。前端用 frontend-design skill。",
         ]),
         ("踩坑与限制", [
             "库里只存了文字描述，所以要能“把狗弹吉他的视频给我”，需要补元数据并改应用，让它直接展示媒体。重新入库时要 upsert，否则会有重复数据。",
             "限制：视频不超过 120 秒，只支持 MP4/MOV；图片每次最多 6 张，PNG/JPEG。长文档要自己切分并保持上下文，Claude Code 会自己处理。",
             "结论：价值正在从“会配置节点、会拼 JSON”转向“能把事说清楚、真正懂业务流程”。",
         ]),
     ],
     "terms": ["RAG", "Embedding", "Vector database", "Chunking", "Multimodal", "Upsert", "Pinecone", "OpenRouter"]},

    # ---------------- 第 4 部分 ----------------
    {"part": 3, "start": "3:32:59", "cn": "把 n8n 工作流变成应用", "en": "Turning n8n Workflow into App",
     "lede": "不只是给 n8n 套一个前端：Claude Code 先审计并改造你的 n8n 后端，让它能正确接收前端数据、返回可展示的结果，然后再做前端，最后通过 GitHub 和 Vercel 上线。",
     "imgs": [("3:34:20", "Claude 改造后的 n8n 工作流"), ("3:36:10", "UGC 广告生成应用"), ("3:43:30", "架构：Claude Code → GitHub → Vercel"), ("3:56:20", "Fit Coach AI 界面")],
     "sections": [
         ("改造后端：UGC 广告示例", [
             "表单触发换成 webhook；上传的图片以 Base64 字符串传入，需要转换；结尾返回成功或失败以及视频 URL，方便嵌入页面。",
             "所有 HTTP 请求改成“出错时继续”，错误走单独分支并通知前端；输入来源变了，它把下游所有变量引用一起改好。作者说自己看到时很震撼。",
         ]),
         ("整体架构与准备", [
             "Claude Code 配上 n8n MCP（节点、配置、模板，能直接读写你的实例）、n8n skills（表达式、用法）、frontend-design skill 和 GitHub MCP。",
             "流程：本地 localhost 测试 → 推到 GitHub 仓库 → Vercel 自动部署。改个颜色再推送，约 20 秒线上就变了。",
             "计划模式让它写 <code>CLAUDE.md</code>（回答：触发方式多样、每个应用一个仓库、用 Tailwind CSS）。连接 MCP 和 skills 时只给原始 URL，并告诉它“你来装，别让我装”。",
             "GitHub 细粒度个人访问令牌（fine-grained token）：Settings → Developer settings。注意 <code>.mcp.json</code> 里是明文凭据，放在本地没问题，但不要外传。改完配置要重启 VS Code。",
         ]),
         ("演示：Fit Coach AI", [
             "原工作流用的是 chat trigger，不适合自定义前端。Claude 换成 webhook，加上窗口缓冲记忆（会话记忆），修正了嵌套的 session ID。",
             "前端要求：专业、极简、不像 AI 拼出来的；深色模式；右侧做游戏化，按消息数升级。",
             "逐个修问题：页面显示整个 JSON → 只取 output 字段；积分不涨 → 修 localStorage；页面打不开 → 截图给它，它重写成更简单的实现；回复带 Markdown 加粗 → 让它直接改 n8n 里智能体的系统提示。",
         ]),
         ("上线与安全", [
             "在 GitHub 建空仓库，把地址给 Claude，它推送代码；Vercel 导入仓库后点 Deploy。",
             "线上报 server configuration error：n8n webhook 地址是环境变量，Vercel 里没配。正确做法是在 Vercel 设置环境变量，并给 webhook 加认证；演示里为了简单直接写死在代码里，不推荐，公开的 webhook 可能被刷爆账单。",
             "让 Claude 对推到 GitHub 的内容做一次安全审查。要用自定义域名，在 Vercel 购买或添加域名，再改 DNS 的 A 记录。",
             "订阅建议：先用 Pro，撞到上限再升到 100 美元档，还不够再升 200 美元档，不合适随时降级。",
         ]),
     ],
     "terms": ["n8n MCP", "Webhook", "Base64", "GitHub repo", "Vercel", "Environment variable", "DNS A record"]},
    {"part": 3, "start": "4:12:42", "cn": "建站技巧", "en": "Website Building Hacks",
     "lede": "五个让 Claude Code 做出“不像 AI 生成、有专业感和品牌感”网站的技巧：从 <code>CLAUDE.md</code>、frontend-design skill，到截图自检、克隆参考网站和单独引入精美组件。",
     "imgs": [("4:17:20", "有无 frontend-design skill 的区别"), ("4:20:10", "一句话生成的品牌落地页"), ("4:30:40", "21st.dev 组件库"), ("4:33:40", "替换品牌后的最终页面")],
     "sections": [
         ("技巧 0：CLAUDE.md", [
             "作者提供一份 web design 版 <code>CLAUDE.md</code>（免费社区下载），第一条就是：每次写前端代码前必须先调用 frontend-design skill，不允许例外。",
             "这份文件会在项目过程中反复修改。",
         ]),
         ("技巧 1：frontend-design skill", [
             "Anthropic 官方 skill，教 Claude 好字体、配色、背景元素和布局。全局安装一次，所有项目都能用。",
             "新建 <code>brand_assets/</code> 放 logo 和品牌规范，用 <code>@</code> 直接引用文件。只说一句“为 AI Automation Society 做一个现代专业的落地页”，就得到导航、hero、滚动 logo 墙、数据、评价、CTA 和浮动 logo 动画。",
         ]),
         ("技巧 2：截图循环", [
             "AI 一般只能做到 40–60%，剩下要靠人一点点调。让它用 Puppeteer 截图，看看自己做得怎样再改，至少两轮，它会自己补上大部分差距。",
             "截图多了容易分不清，可以在 <code>CLAUDE.md</code> 里规定截图命名，或在开始新任务前清空临时截图。",
             "做动画背景时要关闭截图对比，否则它会一直觉得“还不够好”，陷入过度修改。",
         ]),
         ("技巧 3：参考整站", [
             "灵感来源：Dribbble、Godly、Awwwards。按 F12 → Ctrl+Shift+P → “Capture full size screenshot” 截整页，再从 Elements 面板复制样式代码。",
             "把截图和样式一起交给它“克隆这个网站”，它会逐段对照参考图截图比对。得到模板后，再换成自己的颜色、logo 和文案（演示里还顺手把法语翻成了英语）。",
         ]),
         ("技巧 4：单个组件", [
             "在 21st.dev 找着色器、背景、按钮、悬停效果等，复制它的 prompt 代码，告诉 Claude 放到 hero 文字后面。",
             "用口述反馈迭代：背景太糊、太花、文字对比度不够、“Earn more”换成蓝色。第二版就干净多了。",
         ]),
         ("上线流程", [
             "GitHub 建仓库 → Claude 用 CLI 登录 GitHub 并推送 → Vercel 用 GitHub 账号登录并导入仓库 → 部署。之后每次推送都会自动更新线上站点。",
             "在 <code>CLAUDE.md</code> 写明：改动先在 localhost 测，我明确说了才推送。演示给“加入社区”按钮加发光效果：本地确认 → 推送 → Vercel 出现第二次部署 → 线上更新。",
         ]),
     ],
     "terms": ["frontend-design skill", "Screenshot loop", "Puppeteer", "Hero section", "CTA", "21st.dev", "Vercel"]},
    {"part": 3, "start": "4:40:07", "cn": "3D 动画网站", "en": "3D Animated Websites",
     "lede": "像苹果官网那样滚动时产品拆解、文字浮现的网站，其实就是把一段产品视频拆成上百帧图片，再跟滚动位置绑定。作者用两个 skill 加一段 AI 生成的视频，30 分钟做出一个。",
     "imgs": [("4:40:20", "仿苹果手表的滚动拆解页面"), ("4:42:00", "相机 X 光动画网站"), ("4:50:10", "Obsidian Vortex 搅拌机页面"), ("4:52:10", "从 localhost 到线上的流程")],
     "sections": [
         ("原理与准备", [
             "滚动驱动的帧动画：用 FFmpeg 把视频拆成约 100 多张 WebP 图，每张对应一个滚动位置，像定格动画。往下滚就播放，往回滚就倒放。",
             "两个 skill（免费）：作者改过的 frontend-design，以及 video-to-website，放在 <code>.claude/skills/</code> 下。",
         ]),
         ("用 AI 生成产品视频", [
             "在 key.ai 上用 Nano Banana 2 生成 16:9 首帧：纯黑背景的影棚级搅拌机，无阴影、无手、无反光。再以首帧为输入生成尾帧：装满水果和果汁。",
             "把首尾帧交给 Claude，让它写一段视频提示（盖子飘起、水果落入、盖子盖回），再用 Kling 3.0 的首尾帧模式生成视频。",
         ]),
         ("构建网站", [
             "计划模式：“为这个视频做一个单页产品落地页，现代专业、动画流畅、文字易读、纯黑背景与视频融为一体”。它会问品牌名（让它虚构）和内容板块（选完整高端版）。",
             "产出品牌 Obsidian Vortex，口号 “annihilate everything”，血红色强调色。追加要求“视频占右侧 2/3，文字左对齐”，说明布局完全可控。",
             "上下文到 53% 时清空，再用计划模式修复第 2 个卖点出现太晚的问题。改完后让它把经验写回 <code>SKILL.md</code>，skill 会越用越好。",
         ]),
         ("上线时的坑", [
             "让 Claude 用 GitHub CLI 登录、建仓库、推送，Vercel 导入后部署。线上文字动画都在，但没有搅拌机，原因是帧文件夹被 <code>.gitignore</code> 排除了。告诉它把帧加进仓库再推送，然后在 Vercel 重新部署。手机上也能动，下一步是做移动端优化。",
             "localhost 只在你自己的电脑上能访问；推到云端后别人才能看到。本地相当于测试环境，GitHub 加 Vercel 才是生产环境。",
         ]),
         ("生意机会", [
             "很多本地商家的网站很差，又不想花几万美元、等几个月。可以先做一个 demo 发过去，2 天交付，收 5000–10000 美元，再加上托管和维护的月费。",
             "不只是产品旋转，文字、走路等任何视频都能这样做。可以去 Awwwards 找动画灵感。",
         ]),
     ],
     "terms": ["Scroll-driven animation", "FFmpeg", "WebP frames", "Nano Banana 2", "Kling 3.0", "Start / end frame"]},

    # ---------------- 第 5 部分 ----------------
    {"part": 4, "start": "5:00:02", "cn": "API 与 MCP", "en": "APIs and MCPs",
     "lede": "Opus 很聪明，但没有实时数据和你的专属数据时，输出会很泛。本章用 Firecrawl（网页转 LLM 可用数据）和 Blotato（内容再分发与发布）两个工具，演示怎么通过 MCP 和 API 给 Claude 接上“手脚”。",
     "imgs": [("5:01:50", "Firecrawl 抓取演练场"), ("5:08:40", "抓到的 200 条职位"), ("5:12:40", "Blotato 能做什么"), ("5:24:30", "推文风格的 Instagram 轮播图")],
     "sections": [
         ("Firecrawl 能做什么", [
             "<b>scrape</b>：整页 Markdown、AI 摘要、链接、HTML、整页截图、品牌信息（logo、配色、字体）；<b>map</b>：列出全站 URL 和结构；<b>crawl</b>：逐页爬取；<b>search</b>：先搜索再抓取；<b>extract</b>：结构化提取；还有 <b>agent</b> 模式。",
             "端点很多，所以用 MCP：Claude 根据你的自然语言决定调哪个、按什么顺序调。",
         ]),
         ("搭建步骤", [
             "把官方文档里“在 Claude Code 中运行”的一行命令交给 Claude，key 放 <code>.env</code>；Ctrl+Shift+P → Developer: Reload Window 后生效。",
             "让它写一份 <code>firecrawl-cheatsheet.md</code>（每个工具怎么用、什么场景用），再写一份精简的 <code>CLAUDE.md</code> 指向这份速查表。速查表不必塞进 <code>CLAUDE.md</code>，知道在哪就行。",
         ]),
         ("三个用例", [
             "<b>结构化抓取</b>：1782 个职位只要 200 条。它先 scrape 理解页面，再 map 全站；extract 返回空结果就自动换 agent 模式。最终得到标题、公司、类型、地点、薪资、经验、链接、标签等字段的表格。",
             "<b>两个智能体并行</b>：一个给 Moltbot 文档页截图并分析品牌（配色、字体、间距、组件），另一个 map 一家咖啡网站的分类、系列和冲泡指南。",
             "总共约 30 credits（免费 500）。付费档的主要区别是并发数（免费 2 个、Hobby 5 个），不够时 Claude 会排队重试。",
         ]),
         ("Blotato：一条视频变多平台内容", [
             "让 Claude 新建 skill “repurpose YouTube video”：输入 YouTube 链接，输出 LinkedIn、X、Instagram 帖子，每个平台配一张合适的图。提示末尾加一句“一次只问一个澄清问题，直到你有 95% 把握”。",
             "它问并确认了：用 Python；发布前必须人工审核；用 Claude 改写文案（用 OpenRouter 替代 Anthropic key）；LinkedIn 专业、X 轻松幽默；Instagram 做推文风格的教育轮播；草稿存 <code>drafts/</code>，可以手动改后再发。",
             "YouTube 被 WebFetch 拦截，它自己换了方法；生图失败就写进 skill 的“已知问题”再重试。头像放进 <code>brand_assets/</code> 后，轮播图带上名字和蓝 V；图片太大，它自动压缩后再上传。",
             "验证能发到 X 之后，运行 <code>/init</code> 生成 <code>CLAUDE.md</code>（建议 150 行内），再把散落的脚本归到 <code>scripts/</code>，并更新所有引用。",
         ]),
     ],
     "terms": ["Scrape / Map / Crawl / Extract", "Credits", "Concurrency", "Repurposing", "Cheat sheet"]},
    {"part": 4, "start": "5:28:16", "cn": "Google Workspace CLI", "en": "Google CLI",
     "lede": "Google 开源的 Workspace CLI（gws）让任何 Claude Code 项目都能操作 Drive、Gmail、Calendar、Docs、Sheets 和 Slides，而且是用 bash 命令，不是 API 调用或 MCP。",
     "imgs": [("5:31:00", "GWS CLI 覆盖的服务"), ("5:31:10", "什么是 CLI"), ("5:38:00", "自动生成的品牌幻灯片")],
     "sections": [
         ("能做什么", [
             "在 Drive 里搜索、上传、下载、移动、分享；Gmail、日历、Docs、Sheets、Slides、Admin 也都能操作。",
             "内置 100 多个多步骤“recipes”（类似 skills），例如用模板生成文档、读表格数据写报告、找空闲时间约会议。",
             "对比：以前用 API 写 Google Doc，经常是一堆原始 Markdown；现在丢一个 YouTube 链接，就能得到带头图、频道链接和格式化排版的资源指南。",
         ]),
         ("为什么好用", [
             "一个接口管所有服务；默认输出 JSON，智能体处理起来很顺；Google 新增 API 时会自动发现，几乎不用维护；比一堆 MCP 工具定义更省上下文。",
             "CLI 是命令行界面。我们习惯的是图形界面（GUI），而计算机更擅长用文字命令来操作。",
             "注意：这不是 Google 官方支持的产品，处于开源测试阶段，还没到 v1.0，可能有破坏性变更；也有人反馈需要反复重新认证。",
         ]),
         ("安装（手动方案）", [
             "把 GitHub 地址交给 Claude，让它读文档并安装 CLI。",
             "Google Cloud Console 新建项目 → APIs &amp; Services → OAuth 同意屏幕（内部使用；外部使用要加测试用户）→ 创建“桌面应用”类型的 OAuth Client → 下载 JSON 放到 <code>~/.config/gws</code>。",
             "运行 <code>gws auth login</code> 授权，再在 Cloud 项目里逐个启用需要的 API（Gmail、Drive、Docs……）。遇到问题就把看到的情况告诉 Claude，它能读完整文档。",
         ]),
         ("执行助理里的用法", [
             "取当天的未读邮件，结合业务和优先级打 1–10 分，低于 5 分的自动处理。",
             "用 Google Slides 生成带品牌色、logo 和 Nano Banana 2 配图的幻灯片。Claude 说它“看不见”幻灯片，于是接上 Chrome DevTools，让它逐页截图检查，把这个视觉校验步骤写进 skill，并让它再审一遍给出改进建议。",
         ]),
     ],
     "terms": ["GWS CLI", "OAuth client", "Recipes", "Google Cloud Console", "JSON-first"]},
    {"part": 4, "start": "5:39:42", "cn": "打造你的执行助理", "en": "Building Your Own Executive Assistant",
     "lede": "把前面学的串起来，做一个了解你本人、你的业务、团队和当前优先级的 Claude Code 执行助理，也就是“第二大脑”。作者展示了自己的版本 Herk 2，然后分四个阶段带你从零搭建。",
     "imgs": [("5:43:30", "只有你 vs 你 + Claude"), ("5:46:00", "搭建执行助理的四个阶段"), ("5:48:40", "项目文件夹结构"), ("5:55:00", "生成的上下文与项目文件")],
     "sections": [
         ("先澄清一点", [
             "Skills 本质上就是前面讲的 workflows：Markdown 写的 SOP，可以调用 Python 脚本（相当于 tools）。先叫它们工作流和工具，只是因为更直观。",
         ]),
         ("演示：四件事并行", [
             "同时开 4 个会话：morning coffee（读日历、ClickUp 和季度目标，排好当天日程，确认后直接写进日历）；子代理调研 Claude Code 语音功能并写 LinkedIn 帖子和 7 页轮播图；团队进度检查（pulse check）；生成一张视频用的可视化图。",
             "这 4 件事总共花 1–2 分钟，手动做至少 25 分钟。不用纠结“接下来 15 分钟干什么”，决策疲劳少了很多。",
         ]),
         ("阶段 1：给它一个家", [
             "新建文件夹（例如 <code>EA-demo</code>）在 VS Code 打开，新建 <code>CLAUDE.md</code> 作为大脑。",
             "<code>CLAUDE.md</code> 只负责告诉 Claude 东西放在哪：关于我、业务、团队、当前优先级、规则（说话风格、格式）。",
         ]),
         ("阶段 2：赋予生命", [
             "粘贴作者提供的引导提示词（免费），Claude 会建好目录结构、初始化 git，然后采访你：姓名角色时区、业务、关键人员、优先级与目标、沟通偏好、最想交出去的事。认真回答，不知道的可以跳过。",
             "生成 <code>context/</code>（me、work、team、current-priorities、goals）、<code>projects/</code>（每个项目一个 README）、<code>decisions/</code>（决策日志）、<code>references/</code>、<code>templates/</code>、<code>archives/</code>，以及 <code>.claude/rules/communication-style</code>。",
             "<code>CLAUDE.md</code> 约 87 行，用路由指向这些文件。之后可以自己加 <code>brand_assets/</code> 等文件夹，再告诉 Claude 更新 <code>CLAUDE.md</code>。",
             "建议推到 GitHub：云端备份、可回滚、换设备也能用。说一句“记住我总是喜欢 X”，它就会永久记住。",
         ]),
         ("阶段 3：给它双手", [
             "第一件事通常是连上你的项目管理工具（ClickUp、Notion、Asana）。方法：用自然语言描述需求 → 让它调研 API 或 MCP → 你把 key 填进 <code>.env</code>。",
             "演示 research skill：调用 Perplexity（sonar 模型），先读你的背景、业务、项目和优先级再拆解查询。研究波特兰冰淇淋活动时做了 3 次搜索，完整报告存进 <code>research/</code>，以后清空上下文也能接着用。",
             "再做一个功能相同、用 Haiku 的研究子代理，需要省钱时用。子代理有独立上下文，也可以用不同模型。",
             "skill 和 agent 文件都应该带 YAML front matter（name、description），Claude 更容易判断什么时候用，也省 token。最好让 Claude 先读官方文档，再按最佳实践生成。",
         ]),
         ("阶段 4：让它成长", [
             "接下来一周只用它：把 Custom GPT、Claude Projects、Gems 里的指令都搬进来，变成 skills；每次用完都告诉它哪里好、哪里不好，让它更新。",
             "第一天和一个月后会完全不同：文档、决策和 skills 越来越多，它也越来越懂你。下一步就是深入学 Skills。",
         ]),
     ],
     "terms": ["Second brain", "Context files", "Decision log", "YAML front matter", "Sub-agent", "Perplexity sonar"]},

    # ---------------- 第 6 部分 ----------------
    {"part": 5, "start": "6:08:03", "cn": "Skills（技能）", "en": "Skills",
     "lede": "作者说自己从没这么高效过，原因就是 Skills。它们是可复用的指令，相当于给 AI 的 SOP。本章讲清楚 skill 是什么、怎么被触发、怎么保持轻量，现场搭了一个，最后介绍官方 skill-creator 的评估和调优功能。",
     "imgs": [("6:11:30", "Skills = 可复用的指令"), ("6:20:50", "渐进式加载的三个层级"), ("6:25:50", "六步构建框架"), ("6:31:20", "现场生成的品牌信息图"), ("6:37:00", "两类 skill"), ("6:41:40", "Skill 触发调优"), ("6:50:00", "YouTube 周报 PDF")],
     "sections": [
         ("是什么、为什么重要", [
             "可复用的指令：写一次存成 skill，随时触发，因为每次走同一个流程，结果更一致。它们不只是生成文字，还能跑脚本、调 API、调用子代理。",
             "三个价值：<b>个人效率</b>（演示 4 个智能体并行：morning coffee、pulse check、Excalidraw 图、YouTube 评论分析）；<b>团队杠杆</b>（一个人摸索出最佳做法，全公司复用）；<b>变现</b>（卖 skill 有机会，但不宜当长期商业模式）。",
             "作者的团队已要求所有员工使用 Claude Code：一天能产出过去一周的量，做不到这个速度的人会显得太慢、太贵。",
         ]),
         ("结构", [
             "<code>.claude/skills/&lt;名称&gt;/SKILL.md</code>：顶部是 YAML front matter（<code>name</code>、<code>description</code>），下面是分步说明。",
             "参考资料（品牌语气、目标客户画像、logo）和脚本可以放在 skill 文件夹里，也可以放在项目其他位置，只要 <code>SKILL.md</code> 里路径写对。",
             "和 WAT 一一对应：SKILL.md 就是 workflow，脚本就是 tools。",
         ]),
         ("如何触发、如何保持轻量", [
             "显式触发：<code>/skill-name</code>；或者用自然语言，比如“帮我写一篇关于 X 的 Skool 帖子”。Claude 先读 <code>CLAUDE.md</code> → 分析请求 → 匹配 skill，匹配不到就用通用知识。",
             "<b>渐进式加载（progressive disclosure）</b>：第 1 层只读所有 skill 的 name 和 description（各约 100 token）；第 2 层选中后读完整 <code>SKILL.md</code>（约 1–2 千 token）；第 3 层真正需要时才读参考文件和脚本。官方建议 <code>SKILL.md</code> 不超过 500 行。",
         ]),
         ("越用越好：反馈循环", [
             "第一次不可能写完美。作者的做法：先陪 Claude 手动做一遍，从 A 走到 B，然后说“这件事我每天都做，把它变成 skill，缺什么信息就问我”。",
             "调用 → 看它干活 → 给反馈 → 改 skill → 再来一次。前几次一定要盯着看，才能发现提速和省 token 的机会。",
             "例：pulse check 每次都通过 MCP 查一遍 ClickUp 列表 ID，又慢又费 token，那就把 ID 写死在 skill 里，搜索交给专门的 ClickUp searcher 子代理。skill-builder 每次都上网搜文档，那就把文档抓下来存成 <code>reference.md</code>。",
             "什么时候该建 skill：发现自己在重复同一个流程，或反复说同一句话（例如“别用破折号”）。skill 不必复杂，50 行也可以。",
         ]),
         ("六步构建框架与现场演示", [
             "① 名称和触发词 ② 一句话目标 ③ 分步流程（你手动做时的顺序和判断）④ 参考文件 ⑤ 规则与护栏 ⑥ 自我改进循环。",
             "用免费的 skill-builder 问答式生成“品牌信息图” skill：key.ai 的 Nano Banana API 生图 → 读品牌规范 → 在左上角叠加原始 logo（比让 AI 画 logo 稳定得多）→ PNG 存进 <code>projects/</code>。第一版 logo 背景不透明，要求透明叠加并固定 1:1 比例后，第二版就好了。",
         ]),
         ("调试对照表", [
             "步骤错或顺序错 → 改 <code>SKILL.md</code>；缺少语气、风格或上下文 → 加参考文件；同一个错反复出现 → 加规则；工具或 MCP 反复搜索 → 写参考文档；不够好 → 多跑几次，持续挑毛病。",
             "不触发 → 让 YAML 描述更具体；误触发 → 设置 <code>disable-model-invocation</code>。front matter 还能设置 <code>allowed-tools</code>、<code>argument-hint</code>、<code>model</code>、<code>context</code>、<code>hooks</code>、<code>agent</code>。",
             "存放位置：项目级只在当前项目可用；装在 <code>~</code> 下就是全局可用（例如 frontend-design、公司语气）。",
         ]),
         ("官方 skill-creator 的升级", [
             "两类 skill：<b>能力提升型</b>（capability uplift，例如 frontend-design，教模型做它原本做不好的事；模型变强后可能该退役）和<b>编码偏好型</b>（encoded preference，例如作者的 idea mining：评论 + 同行视频 + X 趋势，两个子代理并行，再打分汇总；是你特有的流程，更持久）。",
             "<b>Evals</b>：给它一批好的样例，让它自测并改进 skill；用来发现模型更新后的退化（regression），或发现模型已经不需要这个 skill 了。<b>Benchmark</b>：对比有无 skill 时的通过率、耗时和 token。<b>触发调优</b>：测试各种说法，改写描述，减少漏触发和误触发。",
             "安装：<code>/plugins</code> → 搜 skill-creator → 安装。演示 YouTube 每周回顾 skill：第一版排版好看但数据不对；要求真实的评论、竞品和趋势数据后，3 个智能体并行，生成多页品牌 PDF（每个视频的数据、SWOT、热门评论、竞品、AI 热点），整个过程约 20 分钟。",
             "Anthropic 原话的意思是：将来可能只要用自然语言描述 skill 该做什么，模型会补全剩下的。",
         ]),
     ],
     "terms": ["SKILL.md", "YAML front matter", "Progressive disclosure", "Capability uplift", "Encoded preference", "Evals", "Benchmark", "Trigger tuning"]},
    {"part": 5, "start": "6:51:30", "cn": "子代理", "en": "Sub-agents",
     "lede": "主会话就像项目负责人，可以把专门的任务派给子代理：每个子代理醒来时上下文是全新的，可以用不同模型、有自己的工具。干完只把精简结果交回来，主会话的上下文保持干净。",
     "imgs": [("6:53:10", "子代理架构"), ("6:54:10", "子代理 vs Agent Teams"), ("6:56:40", "为什么用子代理"), ("7:00:30", "三个内置子代理")],
     "sections": [
         ("概念", [
             "演示：carousel skill 内部委派给 carousel planner 子代理；另一个会话同时派出两个调研子代理（中小企业与大企业的 AI 落地），并行完成后汇总给主会话。",
             "常见子代理：code reviewer、builder、debugger、test runner、architect、researcher。可以全部并行。",
             "比喻：办派对要好吃的纸杯蛋糕，不去超市买量产货，而是去专门的烘焙店定制。",
             "和 Agent Teams 的关键区别：子代理是单向关系，主会话下发任务、子代理交回结果，<b>子代理之间不能互相沟通</b>。",
         ]),
         ("五个使用理由", [
             "<b>保护上下文</b>：大量数据和调研都在子代理里处理，只回传主会话需要的部分。",
             "<b>施加约束</b>：高风险操作（例如 GitHub Actions）交给只开放少数工具的子代理。",
             "<b>复用配置</b>：跨项目、跨团队共享。<b>专精</b>：目标越具体，结果越好。<b>控制成本</b>：简单任务用 Haiku。",
             "不该委派的情况：需要来回讨论、需要共享对话历史、需要低延迟。适合委派的情况：任务独立、需要限制工具、只要摘要结果。",
         ]),
         ("文件与机制", [
             "调用机制和 skill 一样：主会话读各个子代理的 description 来决定派给谁，所以描述要清晰。子代理文件就是带 YAML（name、description、tools、model……）的 Markdown。",
             "位置：项目级、个人（全局）、临时（会话或插件）。Boris Cherny 常用的子代理：build validator、code architect、code simplifier、oncall guide、verify app。",
             "三个内置子代理：<b>Explore</b>（Haiku，只读，搜索分析代码库）、<b>Plan</b>（继承主模型，只读，计划模式下调研）、<b>General</b>（继承主模型，可用全部工具）。",
         ]),
         ("现场创建：AI Trend Hunter", [
             "官方推荐用 <code>/agents</code>（VS Code 扩展里要切到终端）→ Create new → 项目级 → 让 Claude 根据描述生成（它还会参考项目里关于你业务的信息）→ 选工具、模型（Sonnet）、颜色、启用 memory。",
             "运行后子代理用了约 4 万 token，主会话总共才 2.9 万，说明主会话没吃下那 4 万。生成的 <code>agent-memory</code> 文件会在下次醒来时读取。按 Ctrl+B 可以放到后台运行。",
             "如果提示 agents 文件夹已存在，把旧文件夹改名后再建，然后把文件移过去，作者认为这是个 bug。他还提供了一个 agent-builder skill，用来审计 agent 文件（例如工具没限制、没设最大轮次、描述过长）。",
         ]),
         ("进阶用法", [
             "在提示里明确要求委派；前台会阻塞主对话，后台不会；skill 可以调用子代理，子代理也可以调用（或预加载）skill。",
             "小而专的子代理更好（tiny agents win）；并行调研后由主会话汇总；可以按固定顺序串联（审查 → 优化 → ……），变成“确定性的顺序 + 非确定性的步骤”。",
             "按任务给子代理选模型；子代理默认约 95% 时 auto-compact，可以调到 50% 来避免上下文腐化。",
         ]),
     ],
     "terms": ["Sub-agent", "Orchestrator", "Explore / Plan / General", "/agents", "Agent memory", "Background agent"]},
    {"part": 5, "start": "7:11:20", "cn": "Agent Teams（代理团队）", "en": "Agent Teams",
     "lede": "Agent Teams 有一个团队负责人和一份共享任务列表，队员之间可以直接发消息、互相分配任务。这是作者认为最强的智能体功能之一，但更慢、更贵，要用在合适的地方。",
     "imgs": [("7:12:30", "团队一次做出的落地页"), ("7:13:20", "子代理与团队的结构对比"), ("7:16:30", "团队提示词模板"), ("7:23:30", "三条规则"), ("7:25:40", "什么时候用团队")],
     "sections": [
         ("演示与区别", [
             "创建 Neuroflow 团队：前端、后端、QA 三名队员，都用 Sonnet，通过 TeamCreate 工具并行生成。前后端把成果交给 QA，QA 发现 3 个严重问题打回，第二轮全部通过，一次做出一个带动画和文案的完整落地页。",
             "子代理各自干活再把结果交给主会话；团队有负责人和共享任务列表，队员能直接沟通、互相派活，QA 和开发之间会形成真正的反馈循环。",
         ]),
         ("启用", [
             "目前是实验功能，默认关闭。把官方文档里的环境变量配置交给 Claude，让它写进 <code>.claude/settings.local.json</code>。",
             "小技巧：让 Claude 先把 Agent Teams 官方文档整理成本地 <code>docs/</code> 参考文件，以后搭团队、回答问题都更快。对常用的大型 MCP 或文档也可以这样做。",
         ]),
         ("提示词怎么写", [
             "先讲<b>目标</b>：队员醒来时没有任何上下文，只能看到负责人给的提示（但能读项目文件）。",
             "“创建一个 N 人团队，用 X 模型”→ 每个队员：角色、做什么、产出什么、做完通知谁（例如“完成后给前端发消息”“等后端消息后交给 QA”）→ 最终交付物（能在 localhost 运行的应用、通过/失败测试报告、说明构建内容和关键决策的文档）。",
             "该做：每人负责自己的文件（避免互相覆盖）、明确产出、指名收件人、3–5 人、给足上下文。不该做：交付物模糊、让它们自己猜该找谁、上来就开 10 人以上（成本也是 10 倍）。",
         ]),
         ("运行机制", [
             "三条规则：各有领地、直接发消息、同时工作。如果只是一个接一个地交接，那就不需要团队。",
             "队员继承主会话的权限（bypass 也会继承），能用项目里的文件、MCP 和 skills。可以开启“计划审批模式”：队员先做计划，由负责人（或你）批准后才执行。",
             "在 tmux 终端里能分屏看到每个队员的思考过程（用颜色区分），还能单独和某个队员对话；在 VS Code 扩展里只能通过主会话沟通。结束时负责人会发 shutdown 请求，队员保存好工作后再关闭。",
         ]),
         ("常见问题与取舍", [
             "总是要权限 → 预先放行常用工具；交付物被覆盖 → 指定文件归属；有人闲着 → 明确分配任务或依赖；token 太多 → 减少人数；丢工作 → 让它们存临时文件；审批不对 → 先由你自己审批。",
             "适合：多个领域、需要并行、需要互相反应和沟通、对质量要求高。不适合：步骤有先后依赖、需要同一个上下文、都在改同一批文件、任务很简单，这些情况用子代理或主会话。",
             "成本大约按人数线性增长（3 人约 3 倍），作者通常用 2–5 人，发现跑偏就尽早关掉。",
         ]),
     ],
     "terms": ["Agent Teams", "Team lead", "Shared task list", "TeamCreate", "SendMessage", "Plan approval", "tmux"]},
    {"part": 5, "start": "7:27:30", "cn": "浏览器自动化", "en": "Browser Automation",
     "lede": "让 Claude Code 直接操作浏览器后，没有 API 的网站也能自动化：测试应用、下载报表、在需要登录的站点里操作。作者用 Playwright CLI 演示了三个场景，并展示了反复迭代的过程。",
     "imgs": [("7:34:00", "智能体在有头浏览器里填表测试"), ("7:37:10", "搜索牙医诊所并抓取电话"), ("7:41:20", "在已登录的 Skool 社区里点赞")],
     "sections": [
         ("为什么选 Playwright CLI", [
             "作者用过 Chrome DevTools MCP，但 <code>/context</code> 显示它的每个工具描述都占大量 token，于是改用 Playwright CLI，效果很好。",
             "安装：计划模式里说明用途，让它调研并安装，它会写一个脚本截图来验证，然后 <code>/init</code>。每个“机器人”其实是一段脚本，配上 skill 就能稳定复用。",
         ]),
         ("用例 1：自动 QA", [
             "先让它做一个 12 题、每页一题的引导表单（还带进度条），它在构建时就主动截图自查。",
             "再要求它用<b>有头浏览器</b>（headed，能看到窗口；headless 则在后台运行）填写并点完整个流程，记录 bug 并修复。它发现两个问题：多行文本框按回车不会前进、确认页加载不出来，还有遮罩层挡住了编辑按钮。修好后主动重测，第二次通过。",
             "可以同时开多个浏览器，分别测不同情况，做成“测试 → 修复 → 再测试”的 QA skill。",
         ]),
         ("用例 2：搜索并收集信息", [
             "在 Google 搜加州牙科诊所并抓电话：Google 拦截了自动化，它自己改用 DuckDuckGo。要求“拿不到 5 个电话不准停”后，它会进入官网、点联系页，最后成功拿到。",
         ]),
         ("用例 3：需要登录的网站", [
             "几种方案：使用持久化的浏览器配置（沿用 Chrome 的登录状态）、有头模式下手动登录后交给它、或连接一个正在运行的浏览器。",
             "作者第一次手动登录 Skool，会话被保存下来，之后自动进入 Wins 频道给帖子点赞。第一版每个赞连点 4 次等于没点；作者指出“先切到按最新排序，黄色的拇指表示已点赞”后，它能正确跳过已赞的帖子并翻页，大约 4–5 轮迭代。下一步是做成 skill。",
             "浏览器自动化一开始不完美很正常，脚本每跑一次都会更好。Skool 这种对自动化很不友好的平台也能处理大量重复操作。",
         ]),
     ],
     "terms": ["Playwright CLI", "Headed / Headless", "Persistent browser profile", "QA automation", "Chrome DevTools MCP"]},

    # ---------------- 第 7 部分 ----------------
    {"part": 6, "start": "7:42:30", "cn": "权限与上下文管理", "en": "Permissions & Context Management",
     "lede": "作者说这部分“有点无聊但非常重要”：如何避免上下文窗口很快被填满，让项目保持高质量输出。下面是一组具体策略。",
     "imgs": [("7:43:40", "保持 CLAUDE.md 精简专注"), ("7:46:20", "/context 查看谁在占用 token")],
     "sections": [
         ("八个上下文策略", [
             "<b>CLAUDE.md 精简</b>：它在每次对话开头都会被注入，从五六百行砍到 100 行效果立竿见影。只放“绝对不能忘”的规则，细节用路由指出去，例如“需要 GWS CLI 的其他操作，去看 <code>references/gws-cli-reference.md</code>”。skills 和规则也照此处理。",
             "<b>有策略地 /clear 和 /compact</b>：大任务完成或换话题时清空；清空前先让它写一份<b>交接文档</b>（handoff doc），新会话读一下就能接着做。",
             "<b>经常看 /context</b>：新会话就已占 2.4 万 token（系统提示、工具、MCP、自定义 agent、记忆文件、skills）。每个 MCP 工具都带描述，所以都占 token。像审订阅账单一样，用不上的就删。",
             "<b>先规划，分阶段做</b>：把计划存成文件，每个阶段开一个新会话读这份计划，不必一直待在同一个会话里。",
             "<b>限制并行会话</b>：作者不再同时开 10–15 个，建议最多 3–4 个，否则很难掌握每个会话的上下文情况，容易在腐化后还盲目相信输出。",
             "<b>子代理处理重数据</b>：例如读 15 分钟视频的完整字幕，交给子代理，只回传要点。",
             "<b>多个智能体共享记忆文件</b>：大家读写同一个计划或任务列表，但要防止并行时互相覆盖。",
             "<b>大代码库用本地语义搜索</b>代替 grep 关键词匹配，据基准测试最多省 97% token（作者自己还没用到这个规模）。",
         ]),
         ("权限（在趣味技巧一章展开）", [
             "比起 dangerously skip permissions，更聪明的做法是在 permissions 里显式 allow 安全命令、deny 删除类命令。deny 的优先级高于 allow，速度不打折，也安全得多。",
         ]),
     ],
     "terms": ["Handoff doc", "Context budget", "Semantic search", "Allow / Deny list"]},
    {"part": 6, "start": "7:50:09", "cn": "GitHub 与 Worktrees", "en": "GitHub & Worktrees",
     "lede": "Git 和 GitHub 管理版本和协作，worktree 让多个会话在同一个仓库里并行工作而互不干扰。作者的定心丸：AI 对 Git 的了解远超你，你只需要说清楚想保存、回滚还是分享。",
     "imgs": [("7:51:30", "什么是 Git"), ("7:55:10", "GitHub 基本工作流"), ("7:56:10", "什么是 Git worktree")],
     "sections": [
         ("Git 与 GitHub", [
             "<b>Git</b>：本地的版本控制系统，像项目的时光机，每次有意义的修改都可以存一个快照。<b>GitHub</b>：架在 Git 上的云服务，像放代码的云端车库，从任何地方都能访问。",
             "概念：<b>repo</b>（被 Git 跟踪的文件夹加完整历史）、<b>commit</b>（某一时刻的快照，附带改了什么、为什么改）、<b>branch</b>（在不影响 main 的副本上实验）、<b>push</b>（上传）、<b>pull</b>（下载最新）、<b>merge</b>（合并回主线）。",
             "GitHub 提供：云备份、多人协作、pull request（合并前先审查）、完整版本历史（谁在什么时候改了什么，可以回滚到任意一次 commit）。",
             "典型流程：建仓库 → clone 到本地 → 建分支 → 修改并 commit → push 分支 → 开 PR → 审查、批准、合并。Claude Code 在后台用的也是这套流程。",
             "例：把执行助理推到 GitHub，度假时带另一台笔记本，pull 下来就能接着用。",
         ]),
         ("Worktrees", [
             "问题：同一个文件夹同时只能在一个分支上工作，做到一半要切分支，就得先暂存或提交未完成的代码。",
             "解决：worktree 把同一个仓库的不同分支同时检出到不同文件夹，彼此隔离。",
             "Claude Code 原生支持 <code>claude --worktree &lt;名称&gt;</code>，可以开多个会话并行做不同任务，最后像普通分支一样合并回主项目。你也可以直接让 Claude 帮你建。",
         ]),
     ],
     "terms": ["Git", "Repository", "Commit", "Branch", "Pull request", "Merge", "Worktree"]},
    {"part": 6, "start": "7:56:45", "cn": "趣味技巧", "en": "Fun Hacks",
     "lede": "从入门到高阶的 32 个技巧，最后用 Pixel Agents 扩展把每个智能体显示成像素办公室里的小人。很多技巧前面已经出现过，这里集中梳理一遍。",
     "imgs": [("8:08:00", "用 worktree 开并行会话"), ("8:13:50", "Pixel Agents 像素办公室"), ("8:16:40", "Pixel Agents 的工作原理")],
     "sections": [
         ("入门（1–10）", [
             "每个已有项目先跑 <code>/init</code>；用 <code>/statusline</code> 在底部显示模型、上下文占比、费用；用语音输入（原生 <code>/voice</code> 正在推出）。",
             "保持上下文小，只给当前任务需要的；用 <code>/context</code> 找出膨胀来源；到 60% 就 <code>/compact</code>（可以指定保留什么），换任务就 <code>/clear</code>。",
             "永远从计划模式开始（Shift+Tab 切换）；把 Claude 当初级开发者，给它问题（“我们该怎么做增长追踪？”）而不是直接下命令，让它先推理。",
             "让它调用提问工具，问到有 95% 把握为止；在 to-do 列表里加入自检步骤（截图检查、浏览器测功能），并要求“当前这项没有 95% 把握就不进下一项”。",
         ]),
         ("中级（11–22）", [
             "复杂问题让它开并行子代理；在 <code>.claude/skills</code> 自建 skill（例如 tech-debt、code-review），提交到 GitHub 全队可用；简单的子代理任务用 Haiku。",
             "有新发现就更新 <code>CLAUDE.md</code>，但控制在 150–200 行，用路由指向其他文件。",
             "看到它跑偏就按 Esc 尽早纠正；对输出提高要求（“推翻重来，换一个更优雅的方案”），得到好结果后让它更新 skill 或 <code>CLAUDE.md</code>；用 <code>/rewind</code> 快速撤销。",
             "用 hooks 在完成时播放提示音；记住它能看图：截图报错、截图参考站、让它截图自查；用 Chrome DevTools 测试功能；克隆参考网站时要加上自己的风格。",
         ]),
         ("高阶（23–32）", [
             "git worktree 并行开发；如果只需要一两个端点，直接调 API，比加载整个 MCP 更省 token；用 <code>/loop</code> 做循环任务（3 天有效，长期任务用定时任务）。",
             "放到 VPS 上常驻；用 Remote Control 在手机或浏览器上遥控本地会话，代码不离开本机；接入 BigQuery 的 <code>bq</code> 等 CLI，用自然语言做数据分析，不用写 SQL。",
             "难题用 <code>ultrathink</code>（约 3.2 万 token 思考预算）；编辑权限实现安全的自主运行（allow 安全命令、deny 删除类命令）；Agent Teams；Context7 MCP 获取最新、带版本号的库文档，弥补训练数据过时。",
         ]),
         ("Pixel Agents 扩展", [
             "VS Code 扩展，读取 Claude Code 的活动日志，把每个终端智能体和子代理显示成像素办公室里的角色，可以自定义家具和地板，有提示音。当时只支持 Windows，项目文件夹名不能含空格或点。",
             "作者做过安全排查：认证发布者、GitHub 1300+ star、没有外发网络请求、不执行命令。",
             "评价：有娱乐价值，可视化也能吸引不熟悉终端的人；但它只显示“谁在工作”，作者真正想要的是看到智能体在做什么决定、能及时阻止。人类越来越像管理者，要让智能体一直走在正轨上，不让它们闲着。",
         ]),
     ],
     "terms": ["/statusline", "/voice", "Hooks", "ultrathink", "Remote Control", "Context7", "Pixel Agents"]},

    # ---------------- 第 8 部分 ----------------
    {"part": 7, "start": "8:25:06", "cn": "销售 AI 的心态", "en": "The Selling AI Mindset",
     "lede": "想靠 AI 赚钱，就别再卖“智能体”和“工作流”，要卖<b>解决方案</b>：诊断企业的问题，再用 AI 解决它。企业只关心三件事：时间、金钱、专注。",
     "imgs": [("8:26:20", "老餐馆挂上霓虹灯"), ("8:30:10", "讲结果，不讲工具"), ("8:38:00", "项目报价从 2000 到 3 万美元以上")],
     "sections": [
         ("为什么卖工具行不通", [
             "自动化早就有了（作者在高盛做商业智能时，自动化就是本职工作）；只是加上“AI”两个字后，老板们才开始关注，就像老餐馆挂上霓虹灯，菜还是那些菜。",
             "新手常被节点、HTTP 请求、多智能体架构这些技术吸引。作者最火的视频是最炫的那些，但最实用、回报最高的往往播放量最低。",
             "企业不在乎你用 AI、VA 还是胶带，就像打车不在乎是 Prius 还是马车，只在乎快、便宜、省心。卖模板库是在拼价格。LinkedIn 外联机器人说成“不投广告也能拿到合格线索的系统”，才有人买。",
         ]),
         ("框架：诊断 → 解决 → 价值 → 定价", [
             "<b>诊断</b>：找到企业在哪里漏掉时间、金钱或专注；<b>解决</b>：针对这个痛点做系统；<b>价值</b>：换算成节省的小时数和金额；<b>定价</b>：围绕价值报价。",
             "例：客户入职每周耗 5 小时 → 自动化 80% → 一年省 200 多小时，按每小时 50 美元算约 1 万美元 → 报 3000 美元，价格只是价值的一小部分。",
             "上门装修的比喻：没人在乎你的锤子多好，大家在乎的是房子增值 5 万美元、工期减半。通话时先问问题（时间最多耗在哪？哪些流程希望能自己跑？），不先展示工作流。",
         ]),
         ("五个步骤", [
             "① <b>选细分行业</b>，花 10 分钟：流程是否每周重复？对方能否快速拍板付款？你是否懂他们的语言？（例如代理商的线索筛选、房产团队的看房协调、电商的客服分流、教练的申请筛选。）",
             "② <b>和 5–10 家企业聊</b>，当作信息访谈。开场：“我在梳理 X 行业最耗时的环节，15 分钟帮你量化最大的瓶颈，你不问我就不推销。”用 <b>LRP</b>：Listen 听、Repeat 复述、Poke 追问量化（谁的时间？时薪多少？出错率？钱花在哪？上午最常被什么打断？）。",
             "③ <b>做一个简单原型（POC）</b>，约 90 分钟：15 分钟画流程（触发、步骤、数据源、输出、完成定义），60 分钟粗搭，15 分钟录 3 分钟露脸的 Loom（之前 → 方案 → 结果）。别幻想多智能体，能用现成平台或 CRM 自带功能就用。",
             "④ <b>换算成价格</b>：每周 10 小时 × 每小时 25 美元 ≈ 每月 1000、每年 1.2 万；只自动化 60% 也能每年省 7000 多；收 3000 美元，5 个月回本。价值不等于工时：作者第一个 1200 美元的项目只花了 2 小时。范围要写清楚（目标、包含、不包含、时间线、客户需配合什么、付款条件），作者早期最大的错误就是范围太模糊。",
             "⑤ <b>积累证明、建立信心、再扩张</b>：冒充者综合征很正常。前 3–5 个项目当作带薪练习，可以免费换证明，或者给退款保证。收集前后对比数据做案例，之后就能说“我已经帮三家同类企业做到了”。",
         ]),
     ],
     "terms": ["AI solution", "Diagnose / Solve / Value / Price", "Niche", "LRP (Listen, Repeat, Poke)", "POC", "Loom", "Scope creep"]},
    {"part": 7, "start": "8:39:41", "cn": "寻找客户", "en": "Finding Clients",
     "lede": "没有 YouTube 频道也能拿到客户。作者的前公司 True Horizon（月营收做到 10 万美元以上后退出）线索多来自 YouTube，但最好的客户来自推荐和合作。本章讲三种不靠内容的方法。",
     "imgs": [("8:41:40", "LinkedIn 私信与冷邮件的回复率"), ("8:49:20", "特洛伊木马法"), ("8:51:50", "四步路线图")],
     "sections": [
         ("方法 1：冷触达", [
             "先要有证明，哪怕免费、哪怕是给表亲的美发店做的，能说“我帮某家企业拿到了某个结果”就行。",
             "平台：LinkedIn、Facebook 群、邮件、Skool 社区、YouTube、Instagram、Reddit，只选 1–2 个。冷邮件平均回复率 1–5%，个性化邮件最多可高 17%；LinkedIn 私信 10–25%，但每条更费时间。",
             "找线索：细分社区、相关账号的关注者、抱怨浪费时间的老板、招聘帖（招的岗位如果能被自动化，就是信号）、本地商家。先问 ChatGPT 或 Perplexity 这个行业有哪些名录（例如美国建筑师协会），比直接上 Apollo 更省事。",
             "写法：讲问题和结果，不讲技术；消息要短；目标是引起好奇、开启对话，不是一条就成交；标题很关键。坦诚说自己刚起步，反而更像真人。降低风险：见效才付款、不签合同，只要求同意用作案例。不直接约 30 分钟会议，先问“能不能给你发一个 2 分钟的 Loom”。",
             "数量：每天至少 100 条，回复率超过 5% 就算很好。追踪回复率、正面回复、约到的会议和成交，正面和负面反馈都记下来，用来调整下一批名单。",
             "两个常见错误：先做再卖（应该先用外联做市场调研，有人感兴趣再做）；一开始就上大规模邮件基础设施（几个域名、每个每天约 30 封就够，成交后再投入）。",
         ]),
         ("方法 2：推荐", [
             "92% 的 B2B 买家信任熟人推荐。AI 领域还很新，很多人不知道去哪找靠谱的人。",
             "先超额交付（例如附送一个没要求的看板、写全文档），上线 1–2 个月后，在展示 KPI 结果的月度复盘时问一句：“你认识其他可能需要 AI 自动化的老板吗？”",
             "据 Dale Carnegie 的研究，只有 11% 的销售会主动要推荐，而 91% 的客户表示被问到会愿意推荐。不要太早问，也不要不敢问。",
         ]),
         ("方法 3：特洛伊木马（作者最推荐）", [
             "借别人的信任：营销代理、顾问、教练、律所早就有信任他们的客户，这些客户在想“我需要 AI”，而代理方也想“我得能给客户提供 AI”。",
             "话术：“我免费给你的客户做 AI 诊断，你和客户都不花钱，你在客户面前很有面子；如果有人后续找我做项目，给你 20% 分成。”合作来源的成交速度快 46%。",
             "诊断时，如果对方说“不知道从哪开始”，就问：“如果明天来了 300 个客户，哪个流程最先崩？”然后深挖那个流程。即使没成交，也是三方共赢。",
         ]),
         ("四步路线图", [
             "<b>先有报价（offer）</b>：选行业和问题，围绕你确定能做出来的结果设计，可以先做简单 demo，但别花几周去做。",
             "<b>用数量验证</b>：目标先拿 5 个客户；每天看数据，找出失败的原因并调整。成功的人和失败的人都会失败，区别在于是否知道为什么失败并做出改变。",
             "<b>交付并记录</b>：上线前记下基线指标，上线后再测一次，给客户看前后对比，然后请他推荐。",
             "<b>借势扩张</b>：有了结果之后，用特洛伊木马法批量接触合作方。",
         ]),
     ],
     "terms": ["Cold outreach", "Reply rate", "Referral", "Partnership", "Trojan horse method", "Rev share", "Market validation"]},
    {"part": 7, "start": "8:54:01", "cn": "7 天拿下第一个客户", "en": "First Client in 7 Days",
     "lede": "社区成员 Christian（21 岁，美国亚利桑那州）加入 5 天就签下第一个客户。前半段是他的访谈，后半段是作者给的 7 天行动计划，可以直接照做。",
     "imgs": [("8:54:50", "访谈 Christian"), ("9:05:10", "转变的关键：心态"), ("9:08:20", "7 天计划流程图")],
     "sections": [
         ("Christian 的故事", [
             "今年 3 月才接触 AI。之前用脚本抓 LinkedIn 线索、AI 写邮件、Instantly 每天发约 450 封冷邮件，打开率很高但没人买。",
             "最大的转变是<b>定位</b>：不当模板贩子，而是陪企业走 AI 之路的向导，讲“帮你扩张或把时间拿回来”。加入社区第 5 天签下 1500 美元的项目（后来涨到 2000），在社区发帖庆祝后，又被另一位成员找上门成了第二个客户，现在可以全职做。",
             "方案：给施工企业项目经理用的“PM 助理”，灵感来自作者的个人助理视频。项目经理在工地上跟机器人说话，它就能给客户发进度邮件、把更新记进 CRM，解决客户总打电话问进度和常见问题的痛点。每周开会持续迭代。",
             "成交原因：坦诚说明自己的阶段和目标，专注建立关系。他还没有网站。",
         ]),
         ("三个心理障碍", [
             "<b>冒充者综合征</b>：所有人都会有，作者现在偶尔也有。不要过度承诺，坦诚说“我刚起步，但很投入”；前一两个客户免费或低价，对方风险低，你也能积累经验。",
             "<b>定价</b>：信任先于 retainer（月度服务费）。还没交付价值就要求长期合同，就像还没合作就要推荐。",
             "<b>被拒</b>：是数据，不是失败。去想是不是消息不清楚、太长、太空泛、对方没有理由回复，然后改进。",
         ]),
         ("7 天计划", [
             "<b>第 1 天</b>：先定一个宽泛方向，例如“帮小企业用 AI 自动化重复、无聊的工作”，脑中准备几个示例（线索跟进、表单录入、CRM 同步）。建一张“信任地图”表格，列出 20 个人：做生意的亲友、前同事和前上司、社区里认识的人、朋友的朋友，并注明他们的行业、熟悉程度和可能的角色。",
             "<b>第 2–3 天</b>：进行 5–10 次低压力的暖关系聊天，不推销，只问“你的工作里哪里最手工、最烦？”并记下要点。如果身边没有老板，就问“你认识谁可能用得上？”，不必卖给朋友。Upwork 也可以，但本质上和冷触达差不多。",
             "<b>第 4–5 天</b>：从笔记里挑出最清楚、最痛、最重复的那个点，提一个免费的小试点：“我想帮你做一个小自动化解决 X，只想证明它真能省时间，作为回报，请给我真实反馈。”",
             "<b>第 5–6 天</b>：做极简 MVP，目的是证明省了时间，不是炫技。留意对方怎么描述问题和收获，这些原话以后写文案时很有用。",
             "<b>第 7 天</b>：一起决定下一步，不硬推。顺序是：维护（保持运行、出问题时修、小调整）或扩展（加一两个开发中发现的功能）→ 视频证言 → 推荐。顺便问“开发时我发现某个相关流程也能自动化”或“接下来你最想甩掉的是什么？”。试点不成功就别卖，带着反馈重新来过。",
             "这是一个要循环几轮的过程。每轮都会让你的数据、信心、措辞和定位更好，跑两三轮之后再把同样的框架用到冷触达上。",
         ]),
     ],
     "terms": ["Positioning", "Trust map", "Warm outreach", "Pilot", "MVP", "Retainer", "Testimonial"]},
    {"part": 7, "start": "9:14:56", "cn": "AI 工作流定价", "en": "Pricing AI Workflows",
     "lede": "多少算便宜、多少算贵、怎样收够钱又不吓跑客户？核心是<b>价值定价</b>：企业为结果付钱，不为你的工时付钱。作者把几乎所有定价方式都试过，最后推荐两种配合使用，并给出 PRICE 框架和一个真实案例。",
     "imgs": [("9:15:40", "价值定价"), ("9:17:40", "沙漠里的一瓶水"), ("9:31:10", "五步 PRICE 框架"), ("9:32:50", "案例：线索处理流程")],
     "sections": [
         ("心态", [
             "AI 工作流通常至少带来三者之一：省钱、省时间、减少人为错误。价格要和这些挂钩，问自己“每周能帮他们省多少时间和钱”，而不是“我要做多久”。",
             "谁先报价常常很尴尬，很多客户也不知道这类服务该多少钱。不管你报多少，都要能一步步讲清楚是怎么算出来的，这样就成了长期的 AI 思考伙伴。",
         ]),
         ("两种模型配合", [
             "<b>价值定价</b>：入门敲门砖，算法简单、建立信任。同一套系统卖给不同企业可以不同价，因为价值不同：刚在沙漠跑完 5 英里的人，愿意为一瓶水付更多钱。",
             "<b>月度 retainer</b>：交付一两个项目、建立信任后再谈。咨询行业通常每月 1500–15000 美元以上，期限 3、6、12 个月。客户得到可预测的成本和优先服务，你得到稳定收入。宁要 1 个每月 1.5 万的客户，也不要 5 个每月 3000 的。",
             "Retainer 可以按小时、按交付物或混合。作者推荐按里程碑：按小时像自由职业者，按里程碑像顾问。在 retainer 里的目标变成持续积累成果、随影响力提价，逐步走向“首席 AI 官”的角色；维护老系统、跟进新模型也是收费的理由。",
         ]),
         ("怎么算出具体数字", [
             "发现阶段要把手工流程画清楚：频率、触发条件、相关人员、每次耗时、每小时价值（薪资、人数、软件费），再对比自动化后的样子。只自动化一半，就只按一半算，别过度承诺。",
             "例：客服每天 1 小时 × 每小时 50 美元 ≈ 每年 1.2 万美元。经验法则是客户首年要看到约 <b>10 倍回报</b>，所以起步价约 1200 美元。还有机会成本：省下的时间可以去做更有价值的事，回报会逐月增加。",
             "Retainer 的算法：先估算交付成本（你自己、兼职或全职工程师、项目经理）。比如每月成本 5000 美元，毛利目标 50–70%（至少守住 50%），就报每月 1 万美元。开发者闲置会烧钱，所以建议先一个人或配一名开发者起步。",
         ]),
         ("怎么呈现报价", [
             "先讲转变，再报价格：让客户先想象系统上线后团队的日常是什么样、哪些问题消失了。",
             "讲清楚价格包含什么：搭建、托管、测试与 QA、优化、需要客户配合的事项、文档与培训、维护。配上截图、线框图或粗略流程图，有 demo 或案例就拿出来。",
             "明确“完成”的定义：在工作范围说明里逐条列出功能，范围外的新需求放进 backlog 留给 V2，这也为后续合作埋下伏笔。讲清楚 QA 流程：内部测 → 客户测并反馈 → 修复 → 再测 → 用真实数据评估 → 上线；客户拖延不是你的责任。",
         ]),
         ("异议、IP 与持续收入", [
             "客户压价时，缩小范围（去掉功能、分阶段），不降价。注意识别难缠的客户：低估你的价值、每一步都质疑，就算愿意先付 1 万美元，也可以放弃。",
             "知识产权：交付的东西归客户；你可以保留通用的内部组件和模板。真正的价值在客户自己的提示词、数据和流程里，对别人没用。",
             "经常性收入：维护费（每个系统每月 200–1500 美元）、优化与监控（适合 AI 较多的系统）、扩展项目（V2）。也可以按小时包（每月 5–20 小时），或按项目价的 10–25% 收月费。真正的目的是加深关系，你越懂客户的系统，对方越难换掉你。",
         ]),
         ("PRICE 框架与真实案例", [
             "<b>P</b>repare 用价值定价的心态；<b>R</b>esearch 在发现阶段梳理流程；<b>I</b>dentify 算出 ROI（10 倍原则）；<b>C</b>ommunicate 先讲结果、范围、QA 和客户职责；<b>E</b>xpand 上线后找维护、优化、V2、retainer 和绩效奖金的机会。",
             "案例：网站表单每周进来 20 条线索，每条需要员工花 1 小时联系、筛选、培育并约销售会议，员工时薪 40 美元，即每周 800、每月 3200、每年约 3.84 万美元。按年节省的 15% 报价 5500 美元；上线后签了每月 550 美元的维护优化（约项目价的 10%）。",
             "作者的反思：当时没有持续追踪上线后的指标（响应速度变成即时、每周线索量、总节省时间、销售团队的感受），如果按月展示，就很自然能谈 V2 和 retainer。",
         ]),
     ],
     "terms": ["Value-based pricing", "Retainer", "Milestone-based", "ROI (10x rule)", "Margin", "Backlog", "Definition of done", "PRICE framework"]},
    {"part": 7, "start": "9:35:36", "cn": "交付 AI 项目", "en": "Delivering AI Projects",
     "lede": "客户付款之后怎么交付：托管在哪里、怎么保证安全、API key 归谁、怎么测试、怎么交接、怎么收尾。视频以 n8n 为例，作者特别说明这套思路同样适用于 Claude Code 产出的代码。",
     "imgs": [("9:38:30", "方案一：客户自己托管"), ("9:40:20", "方案二：你自己托管"), ("9:47:20", "用真实样例测试"), ("9:58:10", "完整流程回顾")],
     "sections": [
         ("用到代码项目上", [
             "n8n 的问题是“账号归谁、托管在哪”；换成代码，问题变成：代码放在谁的 GitHub？跑在谁的 trigger.dev？用谁的域名或云项目？",
             "仍然是三层：账号归属、基础设施归属、访问控制。另外要留意具体服务商的许可和服务条款。自动化本质上就是代码，你只需要弄清楚代码放在哪里、每天运行需要什么（例如环境变量和 API key 由谁填）。",
         ]),
         ("托管：三选一（基于 n8n 许可）", [
             "<b>① 客户自己托管（作者几乎总是推荐）</b>：客户自己购买 n8n Cloud 或自建实例，邀请你作为成员在里面开发。你可以帮他们配置，但必须由客户拥有和付费，你不能加价转卖托管。这和 Zapier 的模式一样。",
             "<b>② 你只为自己的业务托管</b>：内部自动化，或者向客户交付报告、调研结果这类成品，客户不登录、不填自己的 key，这是允许的。",
             "<b>③ 把 n8n 当产品卖（SaaS）</b>：即使客户看不到界面，只要核心价值是“帮你在我的服务器上跑自动化”，就需要商业或企业许可，而且不便宜。",
         ]),
         ("安全与数据保护", [
             "n8n 的凭据加密存储，运行时才在内存中解密；节点只按名称引用凭据，没有权限的人看不到原始 key。",
             "Webhook 相当于一扇对外的门：必须用 HTTPS；支持签名的服务（Stripe、GitHub）要先校验签名；不在 URL 里放敏感数据；必要时加限流和额外认证。AI 智能体还要防止越狱和提示注入。",
             "隐私（不构成法律建议）：数据最小化；限制谁能看执行日志；客户要有合法依据收集数据；你代为处理时可能需要签数据处理协议（DPA）；系统要支持删除、更正和访问请求。自托管时还能用本地或自托管模型，实现数据主权。",
         ]),
         ("API key 与计费", [
             "客户自己注册、绑卡、生成 key、粘贴进系统。key 不经过你，费用透明，客户可以随时停用。可以录一个 Loom 教程，或者开会一起操作。",
             "如果客户坚持让你来填，就用 1Password 这类加密工具发一次性链接，不要用 Slack、ClickUp、短信或邮件传 key。作为附加服务，可以给客户做一个集中查看所有 key 和费用的看板。",
             "作者早期替客户垫付 API 费用再月底开票，结果用量难估、发票拖延、客户困惑。结论：一开始就让客户拥有账号和 key。",
         ]),
         ("测试与 QA", [
             "签约前就和客户约定提供真实样例数据（可以脱敏），因为数据延迟会拖慢整个项目；同时定义什么是好输出、什么绝对不能发生（打错标签、断链、泄露信息、发错人）。",
             "像为失败做规划的工程师那样测：坏数据、空数据、重复数据、意外输入。设计优雅超时、错误工作流告警、把失败写进表格，目的是出问题时安全、安静，并留下足够的排查信息。",
             "当作黑盒，用几十到上百条样例跑，记录每条的输入、过程和输出，对照成功标准，标出失败和边界情况。内部 QA 至少跑几天再给客户。",
             "AI 质量检查：相关且准确、语气得体且安全（不泄露系统提示）、一致性（同样 10 条输入结果是否接近）。可以对提示词和模型做 AB 测试（n8n 有内置 evaluation），日志就是你向客户解释决策的证据。",
             "客户测试时给一个简单的入口（聊天框、表单），不要让他们进 n8n。最后录一个更新视频，展示一两次完整运行，并指向日志。",
         ]),
         ("交接与法务财务", [
             "复制一份作为测试版，干净的一份上生产；n8n 或集成有更新时，先在测试版验证再更新生产版。把 JSON 备份到 GitHub 或 Drive，甚至可以用 n8n 定期自动导出。",
             "保持整洁：每个节点命名清楚，加便签说明逻辑，确认没有残留敏感 key，录 1–2 分钟 Loom 讲解思路。这样客户团队或以后接手的开发者都能看懂，你也不会成为瓶颈。",
             "对照最初的工作范围说明逐项验收，客户确认后开最终发票。维护 retainer 单独签：包括修 bug、小调整、依赖更新、监控和基本安全检查，不包括新功能；约定服务级别（严重故障几小时内响应，小需求几天内处理）、IP 归属和退出流程（导出工作流、文档、交接会，以及哪些另外收费）。",
             "真实案例：作者的第一个个人助理项目，在启动会上就帮客户开好 n8n 账号、拿到各个 key 并邀请自己进去，所以交接时只要换几个凭据，几乎是即时完成。QA 时对话型助理要反复调系统提示；客户提出的大功能放进 backlog 留给 V2，避免做大量无偿工作。",
         ]),
     ],
     "terms": ["Hosting", "Sustainable use license", "Webhook hardening", "GDPR / DPA", "Data sovereignty", "QA", "Handover", "SOW", "SLA"]},
    {"part": 7, "start": "9:58:55", "cn": "致谢", "en": "Thank You! Join AIS FREE",
     "lede": "作者感谢大家看完十个小时的课程，邀请加入免费社区 AI Automation Society（数十万成员）。社区会有每季度的线上活动和线下活动，此外还有付费的 Plus 社区和即将推出的高阶一对一辅导。",
     "imgs": [("9:59:20", "结束语")],
     "sections": []},
]

TAKEAWAYS = [
    ("先计划，再放手执行", "需求先在计划模式里说清楚，让 Claude 反问到有 95% 把握，审完方案再切到 bypass 让它一口气做完。"),
    ("CLAUDE.md 是目录，不是百科", "控制在 150–200 行内，每次对话都会读它；细节放进单独文件，用“路由”告诉它去哪找。"),
    ("像管预算一样管上下文", "常看 /context，60% 左右就压缩，换任务就清空并写交接文档，大量数据交给子代理处理。"),
    ("WAT ≈ Skills + 脚本", "工作流（Markdown SOP）+ 智能体（Claude）+ 工具（Python 脚本），后来演变成 skill 调用脚本，本质相同。"),
    ("把重复劳动沉淀成 Skill", "跑通一次就让它写成 skill，每用一次都给反馈；渐进式加载让它们几乎不占上下文。"),
    ("部署的是代码，不是智能体", "上线到 Modal 或 trigger.dev 的是确定性的工作流和工具；想要智能体本身定时运行，就用桌面版定时任务或 /loop。"),
    ("做网站有一套组合拳", "frontend-design skill + 截图自检 + 参考网站 + 精选组件，再用 GitHub + Vercel 一键上线。"),
    ("子代理与团队各有分工", "子代理单向汇报、省上下文、省钱；Agent Teams 能互相沟通，适合多领域、高质量、可并行的任务，但成本按人数翻倍。"),
    ("安全是底线", "key 放 .env 或平台 secrets，上线前让 Claude 做安全审查，webhook 要加认证，用 allow/deny 规则代替危险的跳过权限。"),
    ("卖结果，不卖技术", "诊断 → 解决 → 价值 → 定价；先从暖关系和试点开始，拿到证明，再靠推荐和合作方扩张。"),
]

GLOSSARY = [
    ("Agentic workflow", "智能体工作流", "只描述目标，由 AI 推理、提问、选工具并自我修复的工作流。"),
    ("Deterministic / Non-deterministic", "确定性 / 非确定性", "同样输入是否总得到同样输出；业务自动化追求确定性。"),
    ("Token", "词元", "模型读写和计费的基本单位，约 3–4 个英文字符。"),
    ("Context window", "上下文窗口", "模型的“工作记忆”，包含系统提示、工具、对话和文件。"),
    ("Context rot", "上下文腐化", "上下文越长，模型准确度越下降的现象。"),
    ("CLAUDE.md", "项目说明文件", "每次对话前都会读取的项目级系统提示。"),
    ("Plan mode", "计划模式", "只读、只调研、只出方案，不改动任何东西。"),
    ("Bypass permissions", "跳过权限模式", "完全自主执行，不再逐步请求批准。"),
    ("MCP (Model Context Protocol)", "模型上下文协议", "让模型统一接入外部服务及其工具的协议。"),
    ("Skill", "技能", "带 YAML 元数据的 Markdown SOP，按需加载，可调用脚本。"),
    ("Progressive disclosure", "渐进式加载", "先读简介、选中再读全文、需要才读附件的加载方式。"),
    ("Sub-agent", "子代理", "由主会话派出、上下文独立、可用不同模型的专职智能体。"),
    ("Agent Teams", "代理团队", "共享任务列表、成员可互相通信的多智能体协作。"),
    ("Hook", "钩子", "在特定事件（如回复完成）时自动执行的动作。"),
    ("Worktree", "工作树", "同一仓库的不同分支同时检出到不同文件夹，便于并行开发。"),
    ("RAG", "检索增强生成", "先从知识库检索相关内容，再交给模型生成回答。"),
    ("Embedding", "嵌入向量", "把文本或图片等内容转换成表示语义的数字向量。"),
    ("Webhook", "网络钩子", "外部系统通过 HTTP 请求触发你的工作流。"),
    ("Idempotency", "幂等", "同一操作执行多次，结果和执行一次相同（如防重复创建）。"),
    ("Headed / Headless browser", "有头 / 无头浏览器", "是否显示浏览器窗口的自动化运行方式。"),
    ("Value-based pricing", "价值定价", "按客户获得的价值而不是工时来定价。"),
    ("Retainer", "月度服务费", "按月支付、持续提供服务的长期合作方式。"),
    ("SOW / Definition of done", "工作范围说明 / 完成定义", "写清楚做什么、不做什么、什么算完成。"),
    ("Scope creep", "范围蔓延", "项目中不断加入未约定的新需求。"),
    ("QA", "质量保证", "上线前后系统性的测试与检查流程。"),
]
