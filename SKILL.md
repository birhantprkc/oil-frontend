---
name: oil-frontend
description: 当任务需要实现、修改、重构或评审产品前端的可见界面、交互行为、前端状态与数据流、组件或样式组织时主动使用，无需用户点名；也用于这些前端行为的测试与验证策略。适用于页面、表单、列表、弹窗、响应式、视觉、动效和前端代码归属调整。不用于纯后端、构建部署、依赖升级、只修导入路径的机械改动、仅操作现有网站、仅生成设计图片或讨论本 Skill；用户明确要求不使用时不触发。
---

# Oil Frontend

从用户任务和完成结果出发，修复真正出错的信息、交互、数据流、布局或共享实现。

## 核心原则

- 沿用用户对浏览、选择、编辑和提交的已有认知；可见内容服务于识别、判断、操作和结果反馈。
- 同一业务数据有明确的权威来源，一个用户意图只执行一次；失败时保留对象、位置和已输入内容。
- 优先使用项目已有的设计变量、组件和成熟能力；既有模式错误时修复源头。简单逻辑直接实现，不为少量代码引入依赖。

## 按需读取

1. 先只读本文件，确定用户要改变的结果。仅修导入路径等机械错误时停止，不读取参考文件。
2. 默认选择一个主要规则。按目标或已知根因路由，不按文件扩展名、CSS、动画关键词或参考文件中的链接追加读取。
3. 出现当前规则无法处理的独立问题时，才补充对应规则；复杂任务按阶段读取，不预先加载全套，也不因固定数量上限遗漏必要规则。

| 当前任务 | 主要规则 | 仅在这些情况补充 |
| --- | --- | --- |
| “看起来不对”、视觉精修、层级、间距、排版、颜色、圆角、边框、阴影或图标的尺寸、颜色与对齐 | [视觉工程](references/visual-engineering-contract.md) | 需要修改共享 Token、组件默认样式或变体时读 [组件与代码组织](references/component-contract.md)；改变分栏、滚动或响应式结构时改读 [视口与弹窗](references/viewport-and-dialog-contract.md) 为主要规则；同时改变图标或动作含义时读 [信息与动作](references/information-and-action-contract.md) |
| 动画、过渡、微交互、展开收起、拖拽反馈、滚动动效或卡顿 | [动效与性能](references/motion-performance-contract.md) | 动效承担动作反馈或视觉层级时读 [视觉工程](references/visual-engineering-contract.md)；根因是异步状态时改读 [状态与加载](references/state-and-loading-contract.md) 为主要规则 |
| 前端测试策略、端到端方案设计、测试清理或检查规则调整 | [自动化](references/automation-contract.md) | 只有检查确实发现需要修复的业务问题时，才补充对应规则；仅运行已有检查不额外读取 |
| 模块边界、组件、Hook、函数、类型、样式归属、共享样式、CSS 组织或共享实现 | [组件与代码组织](references/component-contract.md) | 需要为未覆盖风险设计检查，或清理脆弱、重复、失效检查时读 [自动化](references/automation-contract.md) |
| 文案、动作层级、图标含义与必要性、点击反馈或强调含义 | [信息与动作](references/information-and-action-contract.md) | 涉及对象身份、图片或选择器时读 [资源识别](references/resource-recognition-contract.md)；同时改变颜色、尺寸或对齐时读 [视觉工程](references/visual-engineering-contract.md) |

数据、交互与空间：

| 当前任务 | 主要规则 | 仅在这些情况补充 |
| --- | --- | --- |
| 列表、卡片、详情、表格或批量操作 | [集合与详情](references/collection-and-detail-contract.md) | 涉及资源身份时读 [资源识别](references/resource-recognition-contract.md)；涉及编辑时读 [交互与编辑](references/interaction-and-editing-contract.md) |
| 表单、选择、编辑或多步工作流 | [交互与编辑](references/interaction-and-editing-contract.md) | 涉及保存范围和流程连续性时读 [数据与操作范围](references/scope-and-state-integrity-contract.md) |
| 查询结果、分页、候选集合、保存范围、批量范围或请求结果归属 | [数据与操作范围](references/scope-and-state-integrity-contract.md) | 同时改变 loading、refreshing、empty、error 或 processing 呈现时读 [状态与加载](references/state-and-loading-contract.md) |
| loading、refreshing、empty、filtered-empty、error、queued、processing 或骨架 | [状态与加载](references/state-and-loading-contract.md) | 同时涉及查询快照、操作范围或保存结果归属时读 [数据与操作范围](references/scope-and-state-integrity-contract.md) |
| 改变页面尺寸、分栏、滚动、弹窗结构或响应式行为 | [视口与弹窗](references/viewport-and-dialog-contract.md) | 涉及下拉、菜单、提示等依附触发器的浮层时读 [弹层](references/overlay-contract.md) |
| 对象身份、图片或相邻资源区分 | [资源识别](references/resource-recognition-contract.md) | 需要改变集合结构或编辑流程时，补充对应规则 |
| 下拉、菜单、日期面板、提示或依附触发器的浮层 | [弹层](references/overlay-contract.md) | 需要改变承载方式时读 [视口与弹窗](references/viewport-and-dialog-contract.md) |

## 执行流程

只处理与当前目标有关的步骤，不为局部改动补齐全套问题。评审请求只给证据和建议；要求实现或修复时才修改。

### 1. 还原任务与范围

- 明确原问题、操作入口和预期结果；检查相关实现、数据来源与项目既有约定。
- 涉及数据或交互时，确认对象、字段归属、查询集合、操作范围和提交边界；涉及布局时，确认父容器、滚动与视口边界。
- 修改共享实现前查找受影响的使用位置。只有缺失信息会改变实施方向且无法从项目确认时才提问，不为无关信息中断任务。

### 2. 确定结构与修改落点

- 根据识别、比较、选择或编辑任务确定必要内容和承载方式；删除重复信息与操作，不为完整感增加字段、步骤或装饰。
- 沿用项目已有的 Token、组件和相邻同类模式；视觉差异须能落实到具体元素、属性和依据，缺少标准时按视觉规则采用有限兜底。
- 区分数据流、父布局、共享组件与调用方式的责任，修改真正出错的位置；按业务归属组织代码，只有职责和行为稳定复用时才抽象。
- 必要动作缺少真实结果时补齐行为；无法提供的动作不伪装成可用。新实现接管后清理失效代码和引用，仍有真实兼容对象时明确保留原因与删除条件。
- 完成受影响使用位置的迁移；超出当前授权范围时说明剩余项，不扩大旧模式或修改无关区域。

### 3. 验证实际结果

- 优先从真实入口完成受影响的操作链，检查必要中间反馈与最终结果；保存类修改要重新读取，不能只确认回调或请求发出。
- 复用项目现有且相关的检查与必需门禁；简单样式、文案或排列直接检查实际结果，不默认新增测试、快照或完整状态矩阵。
- 视觉与动效使用真实内容、受影响状态和代表性视口验证；静态检查与截图生成本身不能证明实际表现正确。
- 需要设计、补充或清理长期检查时，按路由读取自动化规则；只保留能发现独立行为错误的验证。目标风险已有充分证据时停止，有新改动、失败或未解疑点才扩大或重跑。

## 独立自检

评审涉及多个页面、共享实现的多种使用场景，或大范围规则调整时，派发无历史上下文的独立自检；局部差异由主 Agent 检查。没有隔离执行能力时直接自检并说明限制。

独立自检只接收检查对象、范围和 `oil-frontend`，不接收对话历史、既有结论、问题猜测或修复方案。

## 输出

按当前任务报告具体问题或已完成改动、依据、实际验证结果与未验证项。只在确有删除、迁移或遗留工作时说明，不强制填满固定栏目，不用测试数量或“更现代”等空泛评价代替证据。区分源码检查、本地运行和目标环境生效。

不主动扩展为无障碍专项审计；实现时使用原生交互元素，保留项目已有的焦点、键盘、标签和 ARIA 行为。当前改动直接造成任务不可完成时检查相应问题。
