# 学习资料库：总计划（v2）

## 0. 背景与目标

- **使用者**：Monash University Malaysia 计算机系学生，用 macOS 和 VS Code，已有 LaTeX 工作流和一份成型的离散数学笔记 `1058note`（FIT1058，LaTeX 写成，有定理环境、`\label`/`\ref`）。
- **目标**：把所有学习资料整理成一个按知识主题组织的大型资料库，覆盖算法、编程、数学（微积分、线性代数、分析、离散、概率、优化）。资料来源包括 Monash 课程、公开课（MIT、UCB 等）和参考书（如 Rosen、Stewart）。**不以任何一个来源的顺序为准。**
- **核心功能**：
  1. 笔记以 Markdown 为主，每个知识点一个文件夹。
  2. 可以勾选/指定内容，生成类似 1058note 风格的 LaTeX/PDF。
  3. 可以从习题中筛选，生成练习卷 PDF。
  4. 仓库同时发布为公开网站（GitHub Pages）。
- **第一批范围**：只做离散数学，只含 FIT1058 课程范围。验证流程跑通后，再扩展 Rosen 的超纲内容和其他领域。

## 1. 已确定的决策

| 项目 | 决定 |
|---|---|
| 组织方式 | 只按知识主题分目录；来源（课程/书/公开课）只做 YAML 元数据和 `sources/` 映射 |
| 笔记格式 | Markdown + YAML 头；`:::` fenced div 表示定义、定理等 |
| 笔记语言 | 全英文（id、标题、正文、标签） |
| 工具链 | Quarto（网站和 PDF 同源）+ Pandoc Lua filter + Python 脚本 |
| 输出 | 笔记 PDF（按清单）、练习卷 PDF（按筛选）、公开网站 |
| 公开程度 | 完全公开 |
| 习题 | 公开仓库放完整题干（原文，不改写），使用者接受版权风险；解答放单独 `solution.md` |
| FIT1058 tutorial/workshop 题与解答 | 可公开（课程协调人 CN 已同意，使用者不商用） |
| 作业、测验、考试、课件原文、教材 PDF | **永不进仓库** |
| 许可 | 笔记内容 CC BY-NC-SA 4.0；脚本 MIT |
| 迁移旧笔记 | 先试点一章，再决定机械转换还是重写 |
| 投入时间 | 每周 3–8 小时 |
| Git | Claude Code 不执行任何 commit/add/push，全部由使用者手动操作 |

## 2. 本阶段不做

- 勾选式交互界面（积累 30 个以上知识点后再做，v1 用手写清单文件）
- `level: extra` 的超纲内容（第二批 Rosen 扩展时才启用）
- 离散数学以外的领域
- 来源索引的手工维护（用脚本从 YAML 反向生成）
- 追求网站外观，PDF 版式只要求与旧 1058note 相近

## 3. 环境与依赖

- macOS，VS Code
- Quarto（自带 Pandoc）
- TeX 发行版（xelatex，`latexmk`）
- Python 3（PyYAML 等）
- `make`
- 现有旧资料位于使用者家目录：`Monash`、`discrete_mathematic`、`Algorithm`、`Advanced_math`、`UECnote`（内容未盘点）、`cpp_workplace` 等

## 4. 仓库结构

```
study-repo/
├── CLAUDE.md                  # Claude Code 守则（使用者先手写）
├── .claude/settings.json      # 权限护栏（使用者先手写）
├── README.md                  # 含来源声明与版权说明
├── LICENSE                    # CC BY-NC-SA 4.0（内容）
├── LICENSE-CODE               # MIT（build/ 脚本）
├── _quarto.yml
├── Makefile
├── .gitignore
├── meta/
│   ├── PLAN.md                # 本文件
│   ├── SPEC.md                # 规范，冻结后少改
│   ├── taxonomy.md            # 主题骨架
│   ├── notation.md            # 符号标准
│   ├── PROVENANCE.md          # 外部材料来源与 CN 同意概述
│   ├── ideas.md               # 冻结期间想改的地方
│   └── preamble.tex           # 沿用 1058note 样式
├── notes/
│   └── math/discrete/<branch>/<topic>/
│       ├── note.md
│       ├── example.md
│       ├── exercise.md
│       └── solution.md
├── sources/
│   └── monash/fit1058.md      # 由脚本反向生成
├── views/                     # 笔记导出清单
├── papers/                    # 练习卷规格
├── build/
│   ├── filters/               # Lua filter
│   ├── check.py
│   ├── make_note.py
│   ├── make_paper.py
│   └── gen_sources.py
├── code/                      # 课程项目、LeetCode（不拆成原子笔记）
├── legacy/                    # 旧 .tex 笔记，迁完清空
├── raw/                       # 版权与作业考试材料（gitignore，Claude Code 不可读）
└── out/                       # 生成的 PDF（gitignore）
```

`.gitignore` 至少包含：

```
*.aux
*.log
*.out
*.toc
*.synctex.gz
*.fls
*.fdb_latexmk
.DS_Store
main.pdf
out/
raw/
_site/
.quarto/
.claude/settings.local.json
```

## 5. SPEC 规则

### 5.1 id 与命名

- `id` 等于路径去掉 `notes/`，如 `math/discrete/logic/propositional/truth-values`，不单独维护。
- 目录名：小写英文加连字符，最多 3–4 层。
- 顶层 taxonomy 只定前两层，叶子在需要时才创建，不预建空目录。
- 离散数学的暂定分支（以 1058note 的实际目录为准，P1 修订）：`logic/propositional`、`logic/predicate`、`proof`（direct、contradiction、induction）、`sets-functions`、`relations`、`counting`、`graph`、`number-theory`。

### 5.2 YAML 头（`note.md`）

```yaml
---
title: Truth Values
sources: [fit1058-w4, rosen-1.1]
requires: [math/discrete/logic/propositional/statements]
level: core          # core | extra（第一批不用 extra）
status: draft        # draft | done
---
```

### 5.3 块类型

`definition`、`theorem`、`lemma`、`corollary`、`proof`、`example`、`remark`、`problem`、`solution`、`extra`。

- 需要编号和被引用的块，用 Quarto 的 id 前缀（`def-`、`thm-`、`lem-`、`cor-` 等）。
- 示例：

```markdown
::: {#def-tautology .definition}
A compound proposition is a *tautology* if
$$ p \equiv \mathrm{T} $$
for every assignment of truth values.
:::

::: {.proof}
1. First step.

2. Second step.
:::
```

### 5.4 习题与解答

`exercise.md`（完整题干原文，不改写）：

```markdown
::: {.problem #prob-induction-03 origin="external" source="fit1058-tut6-q3" difficulty="2" tags="induction,divisibility"}
……完整题干……
:::
```

`solution.md`，与题按 id 配对：

```markdown
::: {.solution for="prob-induction-03"}
1. ……

2. ……
:::
```

- `origin`：`self`（自己写的题）或 `external`（教材、课程、公开课）。
- 以后若需下架外部题，用脚本批量把 `origin="external"` 的题干替换成引用。
- `difficulty`：1–3，由使用者填，Claude Code 不猜；不知道就留空。

### 5.5 写作规范

- 定义和定理中的主要公式用 display 数学，不压缩成行内。
- 证明分步（编号列表或分段），不写成一大段。
- 交叉引用只用标签（编译后变成 `\label`/`\ref`/`\eqref`），不写“§1.6”“Theorem X”这类纯文本。
- 符号以 `meta/notation.md` 为准，来源间的符号差异在 `sources/` 映射里注明。
- 标题层级不写死，由构建脚本按目录深度决定 `\section`/`\subsection`。

### 5.6 知识点粒度

- 一个知识点约等于 1058note 的一个 `\subsection`，`note.md` 约 30–150 行。
- 超过约 200 行才拆；少于约 10 行的孤立定义并入邻居。
- 判断标准：会被别处单独引用的最小概念簇才独立成文件夹。
- 起步偏粗：拆分比合并容易，拆分时原 id 保留作总览，已有引用不会断。
- 例题、习题不是独立知识点，放该知识点的 `example.md` / `exercise.md`。

### 5.7 SPEC 冻结

P3 试点后修订一次，冻结为 v0.2。迁移前 20 个知识点期间不改结构，想改的记入 `meta/ideas.md`，之后一次性调整。

## 6. 构建与输出

三种输出共用同一批 md 和同一套 Lua filter：

| 输出 | 入口 | 过程 |
|---|---|---|
| 笔记 PDF | `views/xxx.yml`（手写清单） | `make_note.py` 读清单，按目录深度生成标题层级，拼成临时 `.qmd`，`quarto render` 到 PDF，引用 `meta/preamble.tex` |
| 练习卷 PDF | `papers/xxx.yml` | `make_paper.py` 扫描 `exercise.md` 的 `problem` 块，按路径/难度/标签/origin 筛选，可选附带 `solution.md` |
| 网站 | `quarto render` | 侧边栏由 Quarto 的目录自动列表或脚本生成；GitHub Actions 构建并发布到 Pages |

清单示例（`views/fit1058-review.yml`）：

```yaml
title: FIT1058 Review
include:
  - path: math/discrete/logic/propositional
    files: [note, example]
  - path: math/discrete/proof/induction
    files: [note, example, exercise]
options:
  include_extra: true
  order: manifest      # manifest | tree | requires
```

练习卷规格示例（`papers/induction-practice.yml`）：

```yaml
title: Induction Practice
select:
  path: math/discrete/proof/induction
  difficulty: [1, 2]
  tags: [divisibility]
options:
  count: 10
  solutions: false
```

`make` 目标：`make check`、`make note VIEW=views/x.yml`、`make paper SPEC=papers/x.yml`、`make site`。

`check.py` 检查项：

- 重复 id、断开的引用
- 缺 YAML 字段
- `problem` 缺 `origin` 或 `source`
- 题与解答配对缺失
- `requires` 指向不存在的节点
- 误含 `raw/`、PDF 或 `.aux` 等不应入库的文件

## 7. 版权、合规与许可

- **CN 同意**：保留原始记录（邮件或消息截图，存放在私有位置，不进仓库）。需要确认两点：是否覆盖公开网站，是否同时覆盖题干和解答。`PROVENANCE.md` 只写一句概述。
- **README 声明**：第三方题目版权归原作者，仅作学习引用；CC BY-NC-SA 只覆盖作者自己写的内容。
- **教材题（Rosen、Stewart 等）**：使用者已接受风险；`origin="external"` 保证可批量下架。
- **永不进仓库**：作业、测验、考试、课件原文、教材 PDF。这些还涉及学术诚信政策，不只是版权问题。
- **`out/` 不提交**：避免把外部题干汇编的练习卷直接公开。

## 8. 使用 Claude Code 的方式

### 8.1 分工

| 使用者 | Claude Code |
|---|---|
| 审 SPEC，定 taxonomy 和粒度 | 起草 SPEC/taxonomy、建骨架 |
| 对照原 PDF 逐项审查每个转换后的笔记 | Pandoc 转换、拆分、加 YAML 和块标记 |
| 所有 `git add` / `commit` / `push` | 写 Lua filter、构建脚本、`check.py`、CI 配置 |
| GitHub 网页设置（Pages、可见性） | 只读检查（`git status`、`git diff`、`find`） |
| 填 `difficulty`、核对 `source` | 不猜、不编造 |

### 8.2 先建护栏，再启动 Claude Code

由使用者手写 `.claude/settings.json`：

```json
{
  "permissions": {
    "allow": [
      "Bash(git status *)",
      "Bash(git diff *)",
      "Bash(git log *)"
    ],
    "deny": [
      "Bash(git add *)",
      "Bash(git commit *)",
      "Bash(git push *)",
      "Bash(git * commit *)",
      "Bash(git * push *)",
      "Bash(git reset *)",
      "Bash(git rebase *)",
      "Bash(git merge *)",
      "Bash(git checkout *)",
      "Bash(git restore *)",
      "Bash(git clean *)",
      "Bash(git stash *)",
      "Bash(git config *)",
      "Read(./raw/**)"
    ]
  }
}
```

- 权限规则由 Claude Code 强制执行，判定顺序是 deny、ask、allow；CLAUDE.md 里的说明只影响 Claude 倾向于做什么，不能改变它被允许做什么。 所以“不 commit”靠 deny 规则硬拦截，CLAUDE.md 只作补充。
- 启动后用 `/permissions` 确认规则生效。
- Makefile 和脚本里不写任何 git 写命令，因为脚本内部的调用不经过 Bash 规则。
- 可把同样的 deny 规则放进用户级 `~/.claude/settings.json`，防止别的项目漏配。

### 8.3 CLAUDE.md（英文，由使用者手写进仓库根目录）

```markdown
# Study repo: rules for Claude Code

Public study-notes repo. Notes are Markdown + YAML, built with Quarto and Pandoc Lua filters.
Read meta/PLAN.md and meta/SPEC.md before any task.

## Hard rules
- NEVER run git add, commit, push, reset, checkout, restore, stash, or config. The owner does all git operations.
- At the end of every task, list the changed files and propose ONE commit message (prefix: feat, migrate, fix, build, docs, chore). Do not commit.
- NEVER read, write, or reference raw/. Never add assignments, quizzes, exams, lecture slides, or textbook text.
- Do not invent taxonomy nodes, rename ids, or change YAML fields without asking.
- Never put git write commands in scripts or the Makefile.

## Content rules
- Notes are in English.
- Copy problem statements verbatim. Never paraphrase or shorten them.
- Never fabricate sources. If a source is unknown, leave `source` empty and add a TODO comment.
- Mechanical migration means convert and tag only. Do not rewrite or improve the author's wording. Set `status: draft`.
- Every `problem` block needs `origin` and `source`. Each solution is paired by id in solution.md.
- Proofs: numbered steps, separate paragraphs, no dense blocks.
- Display math for definitions and theorems. Cross-references use labels, never plain text like "Section 1.6".
- Follow meta/notation.md for symbols.

## Structure
- One knowledge point per folder under notes/: note.md, example.md, exercise.md, solution.md (only note.md is required).
- id equals the path without the notes/ prefix. Folder names are lowercase English with hyphens.
- Granularity: about one subsection, 30-150 lines. Split above 200 lines, merge below 10.

## Workflow
- One task per session. Keep changes small and reviewable.
- Run `make check` before reporting a task done.
- If a request conflicts with these rules or SPEC, stop and ask.
```

### 8.4 使用者的提交流程（每个任务一次）

```bash
git status
git diff --stat
git diff                       # 逐处审查，笔记内容对照原 PDF
make check
git add <具体路径>             # 不用 git add -A，防止带入 raw/ 或 PDF
git commit -m "migrate(discrete): logic/propositional truth-values"
git push                       # 一批任务完成后
```

提交前缀：`migrate`（旧笔记转入）、`feat`（新笔记/新功能）、`build`（filter/脚本/CI）、`docs`（SPEC/README/taxonomy）、`fix`、`chore`（骨架/ignore/配置）。粒度：一个知识点或一章一次提交，一次只做一类事。可选：自配 `.git/hooks/pre-commit`，拒绝暂存 `raw/`、`*.pdf`、`.env`。

### 8.5 会话提示词模板

```
Task: <一句话>
Context: read CLAUDE.md and meta/PLAN.md first.
Input: <文件或目录>
Output: <要产出的文件>
Constraints: no rewriting of wording; verbatim problem statements; do not touch git.
Done when: make check passes; list changed files and propose a commit message.
```

## 9. 分阶段计划

以每周 3–8 小时估算。每个阶段有时间盒，到期无论是否完美都进入下一步。

| 阶段 | 内容 | 使用者 | Claude Code | 验收 | 时间盒 |
|---|---|---|---|---|---|
| **P0 盘点** | 逐个看旧文件夹，分三类：自己的源文件 / 版权与作业考试 / 编译产物；检查嵌套 `.git`；找到 CN 同意的记录 | 分类、找记录 | 可选：只读扫描 | 分类清单 | 约 2 小时 |
| **P1 骨架与 SPEC** | `git init`；手写 `.claude/settings.json` 和 `CLAUDE.md`；起草 SPEC v0.1、taxonomy（离散数学前两层）、notation、`.gitignore`、README、许可 | 审 SPEC，定 taxonomy | 起草文件，需使用者粘贴 1058note 目录 | SPEC v0.1 获批准 | 第 1 周 |
| **P2 搬运** | 旧 `.tex` 笔记 `cp` 进 `legacy/`，项目代码进 `code/`；原文件夹保留；提交前核对 `git status` 无 PDF 和 `raw/` | 搬运，首次提交 | 无 | 干净的首次提交 | 第 1 周末，1–2 小时 |
| **P3 试点** | 选 1058note 一章（建议较小的），Pandoc 转 md，拆 3–5 个知识点，加 YAML、块标记、题目属性、解答 | 对照原 PDF 逐行审查 | 转换、拆分、标记 | 试点章节通过 `check.py`；**决策点**：改动小则其余章节全部机械迁移，改动大则改重写；SPEC 修订为 v0.2 并冻结 | 第 2 周，4–6 小时 |
| **P4 PDF 构建 v1** | 从 1058note 提取 `preamble.tex`；写 Lua filter；`make_note.py` 读手写清单渲染 | 并排对比新旧 PDF | 写代码 | 试点章节 PDF 版式与旧版相近，环境、编号、引用正常（不要求逐页一致） | 第 3–4 周，限 2 周 |
| **P5 练习卷** | `make_paper.py` 按条件抽题，可选附解答 | 验收输出 | 写代码 | 从试点章节生成一份练习卷 PDF | 第 5 周 |
| **P6 网站** | `_quarto.yml`、侧边栏、GitHub Actions、Pages | 开启 Pages，核对公开内容 | 写配置与脚本 | 站点可访问，数学和引用正常，无 `raw/` 内容 | 第 6 周 |
| **P7 批量迁移** | 按 1058 章节顺序，每章一个循环（见 10） | 审查、提交 | 转换 | `legacy/` 清空，全部章节在 `notes/` | 持续，每周 1–2 章 |
| **P8 来源索引** | `gen_sources.py` 从 YAML `sources` 反向生成 `sources/monash/fit1058.md` | 抽查 | 写脚本 | 索引与笔记一致 | P7 过半后 |

**第一批完成标准**：1058 全部章节在 `notes/` 中，`make check` 通过，网站已发布，能生成至少 3 份练习卷。

**之后**：勾选界面（30 个以上知识点后）；Rosen 扩展（启用 `level: extra`，每节含定义、标准例题、至少一道较难的延伸例题，超纲内容留在正文中并用 `.extra` 块标记，不单独隔离）；MIT 6.042、微积分、线性代数、算法等。

## 10. 单章迁移循环

1. Claude Code：Pandoc 转换该章 `.tex` 为 md，按 SPEC 拆成知识点文件夹，补 YAML，将环境转为 `:::` 块，题目补属性。
2. 使用者：对照原 PDF 逐项审查，修正；填 `difficulty`。
3. `make check` 通过。
4. 使用者手动 `git add` 具体路径并提交。
5. 删除 `legacy/` 里对应部分，单独提交（`chore`）。

## 11. 日常工作流

1. 学到或复习某个知识点：在 `taxonomy.md` 找位置，缺则先补。
2. 新建知识点文件夹，写 `note.md`（可让 Claude Code 起草，使用者改成自己的话）。
3. 例题、习题、解答放对应文件。
4. `make check`，按 8.4 自己提交。
5. 需要复习材料：写一个清单出笔记 PDF，或写一个 papers 规格出练习卷。
6. 每批提交后 `git push`，网站自动更新。

## 12. 风险与对策

| 风险 | 对策 |
|---|---|
| 作业、考题、课件误入公开仓库 | `raw/` 在 `.gitignore` 且被 `Read` deny；只用 `git add <具体路径>`；可选 pre-commit hook；`check.py` 检查 |
| Claude Code 擅自提交 | deny 规则硬拦截；启动后 `/permissions` 核对；脚本不含 git 写操作 |
| Claude Code 改写题干或编造来源 | CLAUDE.md 明确禁止；使用者对照原件审查 `source` 与题干 |
| 外部题被要求下架 | `origin="external"` + 批量替换脚本；`out/` 不提交 |
| 完美主义导致拖延 | 时间盒；P4 只要求“相近”；SPEC 冻结；先机械迁移后润色；工具优先级低于内容 |
| Quarto 对自定义块支持不足 | P3 先验证，必要时用 Lua filter 兜底；md 本体不受影响，可迁移到其他工具 |
| 分类反复调整 | 目录最多 3–4 层；想改的记入 `ideas.md`，批量调整一次 |
| 引用节点未被导出 | 脚本按 `requires` 提示或补入 |

## 13. 待验证事项

- Quarto 的 `thm-`/`def-` 等 id 前缀与自定义 `.problem`/`.solution` 块，在网站和 PDF 两边是否都能渲染并保持交叉引用（P3 验证）。
- 通过临时 `.qmd` 拼接再 `quarto render` 到 PDF，是否能完整套用 `preamble.tex` 的样式（P4 验证）。
- Quarto 侧边栏对大量目录的自动生成方式，及 GitHub Pages 的构建发布配置，以官方文档为准（P6 验证）。
- CN 同意的具体范围（公开网站？题干与解答？）。
- 1058note 的实际章节目录，用于确定 taxonomy 前两层（P1）。

## 14. 开工检查清单

1. 做 P0：盘点旧文件，找到 CN 同意的记录。
2. `git init`，手写 `.claude/settings.json` 和 `CLAUDE.md`，把本文件存为 `meta/PLAN.md`。
3. 启动 Claude Code，用 `/permissions` 确认 deny 规则。
4. 粘贴 1058note 的目录，开始 P1：起草 SPEC v0.1。
5. 审 SPEC，自己 `git add` 并提交第一个 commit。
