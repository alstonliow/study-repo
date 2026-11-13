# 学习资料库完整计划 v2

整合了此前所有讨论和你的全部决策，并加入 Claude Code 协作方式。

## 0. 已确定的决策

| 项目 | 决定 |
|---|---|
| 组织方式 | 只按知识主题；来源（Monash/MIT/UCB/教材）只做元数据和映射 |
| 笔记格式 | Markdown + YAML 头，每个知识点一个文件夹 |
| 语言 | 全英文（`id`、标题、正文、标签） |
| 工具链 | Quarto（网站和 PDF 同源），Lua filter 处理自定义块 |
| 输出 | 勾选/清单生成 PDF、公开网站、练习卷 PDF |
| 公开程度 | 完全公开（GitHub Pages） |
| 习题 | 公开仓库放完整题干；解答放单独 `solution.md` |
| 1058 tutorial/workshop | 题干和解答可公开（CN 已同意，你不商用） |
| 作业、测验、考试 | 永不进仓库 |
| 许可 | 笔记 CC BY-NC-SA 4.0；脚本代码另用 MIT |
| 第一批范围 | 离散数学，仅 1058 课程范围 |
| 迁移方式 | 先试点一章再定 |
| 时间 | 每周 3–8 小时 |
| Git | Claude Code 不执行任何 commit，全部由你手动 |

## 1. 仓库结构

```
study-repo/
├── CLAUDE.md                 # Claude Code 的项目规则（你先手写）
├── .claude/settings.json     # 权限护栏（你先手写）
├── README.md                 # 含来源声明和版权说明
├── LICENSE                   # CC BY-NC-SA 4.0（内容）
├── LICENSE-CODE              # MIT（build/ 下的脚本）
├── _quarto.yml
├── Makefile
├── .gitignore
├── meta/
│   ├── SPEC.md               # 规范（目录/id/YAML/块类型/粒度），冻结后少改
│   ├── taxonomy.md           # 主题骨架
│   ├── notation.md           # 符号标准
│   ├── PROVENANCE.md         # 外部材料来源与 CN 同意说明
│   └── preamble.tex          # 沿用 1058note 样式
├── notes/
│   └── math/discrete/<branch>/<topic>/
│       ├── note.md
│       ├── example.md
│       ├── exercise.md
│       └── solution.md
├── sources/                  # 来源 → 笔记映射
│   └── monash/fit1058.md
├── views/                    # 笔记导出清单（manifest）
├── papers/                   # 练习卷规格
├── build/
│   ├── filters/              # Lua filter
│   ├── check.py              # 检查脚本
│   ├── make_note.py          # 按 manifest 拼接并渲染 PDF
│   └── make_paper.py         # 练习卷生成
├── code/                     # 课程项目、LeetCode
├── legacy/                   # 旧 .tex 笔记，迁完即清空
├── raw/                      # 版权资料、作业考试（gitignore）
└── out/                      # 生成的 PDF（gitignore）
```

`out/` 不提交，避免把外部题干汇编成的练习卷直接放到公开仓库里。

## 2. SPEC 核心规则

**2.1 路径与 id**：`id` 等于路径（去掉 `notes/`），如 `math/discrete/logic/propositional/truth-values`，不单独维护。目录名小写英文加连字符，最多 3–4 层。

**2.2 YAML 头**（每个 `note.md`）：

```yaml
---
title: Truth Values
sources: [fit1058-w4, rosen-1.1]
requires: [math/discrete/logic/propositional/statements]
level: core          # core | extra（第一批不用 extra）
status: draft        # draft | done
---
```

**2.3 块类型**：`definition`、`theorem`、`lemma`、`corollary`、`proof`、`example`、`remark`、`problem`、`solution`、`extra`。带编号、会被引用的块用 Quarto 的 id 前缀（`def-`、`thm-`、`lem-` 等）。P3 需核实这些自定义块在网站和 PDF 两边都能正常渲染。

**2.4 题目属性**（`exercise.md`，完整题干原文照录，不改写）：

```markdown
::: {.problem #prob-induction-03 origin="external" source="fit1058-tut6-q3" difficulty="2" tags="induction,divisibility"}
……完整题干……
:::
```

`solution.md` 里用同 id 配对：

```markdown
::: {.solution for="prob-induction-03"}
1. ……

2. ……
:::
```

`origin` 取 `self` 或 `external`。以后要下架外部题，脚本批量把 `external` 的题干替换成引用即可。

**2.5 写作规范**：证明分步（编号列表）；重要公式用 display 块；交叉引用用标签，不写"§1.6"；符号以 `notation.md` 为准。

**2.6 知识点粒度**：约等于 1058note 的一个 `\subsection`，`note.md` 30–150 行；超过 200 行才拆，少于 10 行并入邻居。起步偏粗，之后拆分时原 id 保留作总览。

**2.7 SPEC 冻结规则**：P3 试点后修订一次，冻结 v0.2。迁移前 20 个知识点期间不改结构，想改的记在 `meta/ideas.md`，之后一次性调整。

## 3. 构建与输出

三种输出共用同一批 md 和同一套 Lua filter：

| 输出 | 入口 | 过程 |
|---|---|---|
| 笔记 PDF | `views/xxx.yml`（手写 manifest，v1 不做勾选界面） | `make_note.py` 按目录深度生成 `\section` 层级，拼成临时 `.qmd`，`quarto render` 到 PDF，引用 `meta/preamble.tex` |
| 练习卷 PDF | `papers/xxx.yml` | `make_paper.py` 扫描 `exercise.md` 的 `problem` 块，按路径/难度/标签/origin 筛选，选项含是否附 `solution.md` |
| 网站 | `quarto render` | 侧边栏由脚本从目录生成，GitHub Actions 发布到 Pages |

manifest 示例：

```yaml
title: FIT1058 Review
include:
  - path: math/discrete/logic/propositional
    files: [note, example]
  - path: math/discrete/proof/induction
    files: [note, example, exercise]
options: {include_extra: true, order: manifest}
```

练习卷规格示例：

```yaml
title: Induction Practice
select: {path: math/discrete/proof/induction, difficulty: [1, 2], tags: [divisibility]}
options: {count: 10, solutions: false}
```

`check.py` 检查项：重复 id、断开的引用、缺 YAML、`problem` 缺 `source`/`origin`、题与解答配对缺失、`requires` 指向不存在的节点、是否误含 `raw/` 内容。

## 4. 合规与许可

- **CN 同意**：保留原始记录（邮件或消息截图，放私有位置），确认两点：是否覆盖公开网站，是否同时覆盖题干和解答。`PROVENANCE.md` 只写一句概述，不放截图。
- **README 声明**：第三方题目版权归原作者，仅作学习引用；CC BY-NC-SA 仅覆盖作者自己的内容。
- **教材题（Rosen、Stewart）**：你已接受风险；`origin="external"` 属性保证随时可批量下架。
- **永不进仓库**：作业、测验、考试、课件原文、教材 PDF。
- **Claude Code 的约束**：见下节，写进 CLAUDE.md。

## 5. Claude Code 协作方式

### 5.1 分工

| 你 | Claude Code |
|---|---|
| 审 SPEC、定粒度和分类 | 起草 SPEC/taxonomy、建骨架 |
| 逐项审查每个转换后的笔记（对照原 PDF） | Pandoc 转换、拆分、加 YAML 和块标记 |
| 所有 `git add` / `git commit` / `git push` | 写 Lua filter、构建脚本、check.py、CI 配置 |
| GitHub 网页上的设置（Pages、仓库可见性） | 只读检查（`git status`、`git diff`、`find`） |

### 5.2 先建护栏，再启动 Claude Code

在第一次启动前，由你手写这两个文件。

`.claude/settings.json`：

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

依据官方文档的权限说明：规则按 deny、ask、allow 顺序判定，先匹配者生效；权限由 Claude Code 强制执行，而 CLAUDE.md 里的说明只影响 Claude 的倾向，不改变它被允许做什么。 所以"不 commit"必须靠 deny 规则，CLAUDE.md 只作补充。Bash 规则支持把通配符放在命令中间，如 `git * main` 这类写法，上面的 `git * commit *` 用来拦截 `git -C . commit` 之类的变体。

启动后用 `/permissions` 确认规则已生效。另外两点：

- Makefile 和脚本里不要写 `git commit`，因为脚本内部的调用不在 Bash 规则的视线内。
- 可以同时把同样的 deny 规则放进用户级 `~/.claude/settings.json`，防止别的项目漏配。

`CLAUDE.md`（英文，简短）：

```markdown
# Study repo — rules for Claude Code

## Hard rules
- NEVER run git add/commit/push/reset/checkout/restore/stash. The owner does all git operations.
- At the end of every task: list changed files and propose ONE commit message (conventional prefix: feat/migrate/fix/build/docs/chore). Do not commit.
- NEVER read, write or reference anything in raw/. Never add assignments, quizzes, exams, slides or textbook text.
- Follow meta/SPEC.md. Do not invent new taxonomy nodes, rename ids, or change YAML fields without asking.

## Content rules
- Notes are in English. Problem statements are copied verbatim; never paraphrase.
- Never fabricate sources. If a source is unknown, leave `source` empty and add a TODO comment.
- Mechanical migration = convert and tag only. Do not rewrite or "improve" the author's wording. Set `status: draft`.
- Proofs: numbered steps, separated paragraphs. Cross-references via labels, not plain-text section numbers.

## Workflow
- One task per session. Keep changes small and reviewable.
- Run `make check` before reporting a task done.
```

### 5.3 你的提交流程（每个任务一次）

```bash
git status
git diff --stat
git diff                      # 逐处审查，笔记内容对照原 PDF
make check
git add <具体路径>            # 不用 git add -A，防止带入 raw/ 或 PDF
git commit -m "migrate(discrete): logic/propositional truth-values"
# 一批任务完成后
git push
```

| 前缀 | 用途 |
|---|---|
| `migrate` | 旧笔记转入 notes/ |
| `feat` | 新笔记或新功能 |
| `build` | filter、脚本、CI |
| `docs` | SPEC、README、taxonomy |
| `fix` | 修正笔记或脚本错误 |
| `chore` | 骨架、ignore、配置 |

提交粒度：一个知识点或一章为一次提交，一次提交只做一类事。可选：自己配一个 `.git/hooks/pre-commit`（由你自己的提交触发），拒绝包含 `raw/`、`*.pdf`、`.env` 的暂存内容。

### 5.4 每个会话的提示词模板

```
Task: <一句话>
Context: read CLAUDE.md and meta/SPEC.md first.
Input: <文件或目录>
Output: <要产出的文件>
Constraints: no rewriting of wording; verbatim problem statements; do not touch git.
Done when: make check passes; list changed files and propose a commit message.
```

## 6. 分阶段计划

以每周 3–8 小时估算，每个阶段设时间盒，到期无论是否完美都进入下一步。

| 阶段 | 内容 | 你 | Claude Code | 验收 | 时间盒 |
|---|---|---|---|---|---|
| **P0 盘点** | 逐个看 `Monash`、`discrete_mathematic`、`Algorithm`、`Advanced_math`、`UECnote`，分成"自己的源文件 / 版权与作业考试 / 编译产物"；找出 CN 同意的记录；发 1058note 目录给我 | 分类、找记录 | 可选：只读扫描，生成清单、检查嵌套 `.git` | 一份分类清单 | 2 小时 |
| **P1 骨架与 SPEC** | 建仓库；手写 `.claude/settings.json` 和 `CLAUDE.md`；让 Claude Code 起草 SPEC v0.1、taxonomy、notation、目录、`.gitignore`、README、许可 | 审 SPEC，定 taxonomy 前两层 | 起草文件 | SPEC v0.1 你已批准 | 第 1 周 |
| **P2 搬运** | 旧文件 `cp` 进 `legacy/` 和 `code/`，原文件夹保留；提交前核对 `git status` 无 PDF、`raw/` | 搬运、首次提交 | 无 | 干净的首次提交 | 第 1 周末，1–2 小时 |
| **P3 试点** | 选 1058note 的一章（建议较小的一章），Pandoc 转 md，按 SPEC 拆 3–5 个知识点，加 YAML、块标记、题目属性、solution | 逐行对照原 PDF 审查 | 转换、拆分、标记 | 试点章节通过 `check.py`；**决策点**：机械转换改动小则其余章节全部机械迁移，否则改重写；SPEC 修订为 v0.2 并冻结 | 第 2 周，4–6 小时 |
| **P4 PDF 构建 v1** | 从 1058note 提取 preamble；写 Lua filter；`make_note.py` 读手写 manifest 渲染 | 并排对比新旧 PDF | 写代码 | 试点章节 PDF 版式与旧版相近，环境、编号、引用正常（不要求逐页一致） | 第 3–4 周，限 2 周 |
| **P5 练习卷** | `make_paper.py` 按筛选条件抽题，可选附解答 | 验收输出 | 写代码 | 从试点章节生成一份练习卷 PDF | 第 5 周 |
| **P6 网站** | `_quarto.yml`、侧边栏脚本、GitHub Actions、Pages | 在 GitHub 上开启 Pages、核对公开内容 | 写配置和脚本 | 线上站点可访问，数学和引用正常，无 `raw/` 内容 | 第 6 周 |
| **P7 批量迁移** | 按 1058 章节顺序，每章一个循环：转换 → 审查 → `check.py` → 提交 → 删除 `legacy/` 对应部分 | 审查、提交 | 转换 | `legacy/` 清空，全部章节在 `notes/` | 持续，每周 1–2 章 |
| **P8 来源索引** | 脚本从 YAML `sources` 反向生成 `sources/monash/fit1058.md` | 抽查 | 写脚本 | 索引与笔记一致 | P7 过半后 |
| **以后** | 勾选界面（积累 30 个以上知识点后再做）；第二批：Rosen 扩展（用 `level: extra`）、MIT 6.042、微积分 | | | | 另议 |

**第一批完成标准**：1058 全部章节在 `notes/` 中、`make check` 通过、网站已发布、可生成至少 3 份练习卷。

## 7. 日常工作流

1. 学到或复习某个知识点，打开 `taxonomy.md` 找位置，缺则先补
2. 新建知识点文件夹，写 `note.md`（可让 Claude Code 起草，你改写成自己的话）
3. 例题、习题、解答放对应文件
4. `make check` → 按 5.3 的流程你自己提交
5. 需要复习材料时写一个 manifest，或写一个 papers 规格出练习卷
6. 每批提交后 `git push`，网站自动更新

## 8. 风险与对策

| 风险 | 对策 |
|---|---|
| 作业、考题、课件误入公开仓库 | `raw/` 加入 `.gitignore` 和 `Read` deny；只用 `git add <具体路径>`；可选 pre-commit hook |
| Claude Code 擅自提交 | deny 规则硬拦截；启动后用 `/permissions` 核对；脚本不含 git 写操作 |
| Claude Code 改写题干或编造来源 | CLAUDE.md 明确禁止；你对照原件审查 `source` 和题干 |
| 外部题被要求下架 | `origin="external"` + 批量替换脚本；`out/` 不提交 |
| 完美主义拖延 | 时间盒；P4 只要求"相近"；SPEC 冻结；迁移先机械后润色 |
| Quarto 对自定义块支持不足 | P3 先验证，必要时用 Lua filter 兜底，不影响 md 本体 |
| 分类反复调整 | 目录最多 3–4 层，想改的记入 `meta/ideas.md`，批量调整一次 |

## 9. 下一步

1. 把 1058note 的 `main.pdf` 目录页（章节列表）发给我，我起草 `taxonomy.md` 的离散数学部分和 SPEC v0.1
2. 确认 CN 同意的范围（是否覆盖公开网站、题干和解答）
3. 开工当天先做 P0，再手写 `.claude/settings.json` 和 `CLAUDE.md`，最后才启动 Claude Code

这份计划可以存为 `meta/PLAN.md`，Claude Code 的每个会话都能引用它。
