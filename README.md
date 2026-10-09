<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/wisteria-blush-theme/main/assets/icon.png" alt="Wisteria Blush Theme logo" width="128">
</p>

<h1 align="center">Wisteria Blush Theme</h1>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=lilinhuang.wisteria-blush-theme"><img src="https://img.shields.io/badge/VS%20Code-Theme-A05C8B?logo=visual-studio-code" alt="VS Code Theme"></a>
  <img src="https://img.shields.io/badge/version-1.0.0-514458?logo=visual-studio-code" alt="version 1.0.0">
  <img src="https://img.shields.io/badge/Variants-Light%20%26%20Dark-957DAD?logo=visual-studio-code" alt="Light and Dark variants">
  <a href="https://github.com/vaxicy/wisteria-blush-theme/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Non--Commercial-lightgrey" alt="License: Non-Commercial"></a>
</p>

A wisteria arbor for VS Code: **soft wisteria violet**, **dusty blush** and **warm peach** over a **porcelain lavender** editor in the light variant and over a **charcoal violet** editor in the dark one. Both variants are cut from one palette, so switching changes the light level rather than the character of the workspace.

一套紫藤花架配色的 VS Code 主题：浅色版是**瓷感淡紫**的纸面，深色版是**炭紫夜色**的底子，两者都用**柔和的紫藤紫**、**灰粉**与**暖桃色**点缀。明暗两套变体共享同一套色板，切换时改变的是明暗而非气质，工作区始终保持春末紫藤般的安静与柔和。

## Preview / 预览

| Light 浅色 | Dark 深色 |
| --- | --- |
| ![Wisteria Blush Theme Light](https://raw.githubusercontent.com/vaxicy/wisteria-blush-theme/main/store-assets/screenshots/en/screenshot-light.png) | ![Wisteria Blush Theme Dark](https://raw.githubusercontent.com/vaxicy/wisteria-blush-theme/main/store-assets/screenshots/en/screenshot-dark.png) |

> Both previews are captured from a real VS Code window running the theme — no mockups.
>
> 上方预览图取自真实运行该主题的 VS Code 窗口截图，非模拟图。

## Palette / 色板

| Role | Light | Dark |
| --- | --- | --- |
| Editor background | `#FCF9FD` porcelain lavender | `#302735` charcoal violet |
| Foreground | `#514458` wisteria ink | `#EADFEB` pale petal |
| Muted text / placeholders | `#827288` | `#947F9B` |
| Side bar | `#F3EDF5` with `#615068` text | `#292230` with `#CFBDD6` text |
| Panel / terminal | `#F7F0F6` | `#29222F` |
| Title bar | `#EFE8F2` with `#57485F` text | `#241F2A` with `#D6C6DC` text |
| Tab bar / inactive tab | `#EEE5F0` | `#241E2A` |
| Active tab indicator | `#B580B0` | `#D291BC` |
| Activity bar | `#E7DDEA` with `#816395` icons | `#201B26` with `#E0BBE4` icons |
| Status bar | `#E6D5E9` with `#674C72` text | `#49344E` with `#F0D5EB` text |
| Selection | `#E7CFEA` blush wash | `#62476D` deep plum |
| Current line | `#F4EBF5` | `#3A2E40` |
| Borders / indent guides | `#DFD2E3` / `#E8DDEA` | `#4B3B55` / `#493650` |
| Button | `#E0BBE4` with `#5E416A` text (hover `#D4A9DC`) | `#E0BBE4` with `#402B49` text (hover `#F0CDEB`) |
| Badge | `#957DAD` with white text | `#E0BBE4` with `#402B49` text |
| Cursor | `#A26394` | `#FEC8D8` |
| Links | `#87479D` | `#D8B7E3` |
| Errors / warnings | `#B45469` / `#A17B3D` | `#EE9BAE` / `#E8CB91` |
| Git added / modified / deleted | `#6B8B64` / `#A17B3D` / `#B46C7E` | `#B6D5A9` / `#E8CB91` / `#E7A4B5` |

Wisteria `#E0BBE4`, dusty blush `#D291BC`, petal pink `#FEC8D8` and wisteria ink `#514458` carry both variants, so a file still reads as "wisteria blush" after switching.

紫藤紫 `#E0BBE4`、灰粉 `#D291BC`、花瓣粉 `#FEC8D8` 与紫藤墨 `#514458` 贯穿明暗两版，切换后整个文件依然是同一份「紫藤浅绯」气质。

## Syntax mapping / 语法映射

| Syntax | Light | Dark |
| --- | --- | --- |
| Comments | `#A18FA6` italic | `#A58BAE` italic |
| Keywords / storage | `#A05C8B` wisteria | `#E2A5CA` orchid |
| Strings | `#657D65` sage | `#BCD5B7` soft sage |
| Regexp | `#936AA2` | `#DABBE5` |
| Escapes | `#9B7954` | `#E8C79B` |
| Numbers / constants | `#AE735D` terracotta | `#FFDFD3` peach |
| Types / classes | `#926A9D` | `#E0BBE4` |
| Functions / methods | `#78609F` | `#D6BCEB` |
| Properties | `#527E83` | `#AED1D2` |
| Variables | `#514458` | `#EADFEB` |
| Parameters | `#8B708A` | `#D5BED4` |
| Operators | `#88708F` | `#CBB1D2` |
| Punctuation | `#A18AA8` | `#B298BB` |
| Tags / headings | `#A05C8B` | `#FEC8D8` |
| Attributes | `#92785A` | `#E8C9A8` |
| Invalid | `#B65353` | `#E99B91` |

Keywords stay wisteria violet, strings stay sage green and numbers stay terracotta and peach in both variants, so the syntax keeps its identity whichever variant you use.

关键字在浅色下是紫藤紫、深色下是淡兰紫，字符串始终保持鼠尾草绿，数字始终保持陶土与蜜桃，两套变体的语法读感一致。

## Coverage / 覆盖范围

Every surface below is themed in both variants (144 UI colors each):

- **Editor** — background, foreground, selection and inactive selection, current-line highlight, word and selection highlights, find match and find highlight, bracket-match background and border, cursor, line numbers (plus the active line number), indent guides, whitespace, ruler, errors, warnings and info.
- **Workbench chrome** — activity bar, badge and active border, title bar (active and inactive), side bar with section headers and border, status bar (normal, no-folder and debugging states), editor group header and tabs (active, inactive, hover, modified border and active top border).
- **Panels and overlays** — panel, editor widgets, hover widget, suggest widget, dropdowns, inputs and placeholder text, notifications, quick input, and the focus border.
- **Lists** — active, inactive and hover selection backgrounds, plus the highlight and focus-highlight colors, and tree indent guides.
- **Terminal** — background, foreground and the full 16-color ANSI palette, matched to the theme.
- **Details** — workbench borders, scrollbar sliders, git decoration colors (added / modified / deleted) with their gutter markers, buttons, badges, diff editor backgrounds, and semantic token colors for variable, parameter, property, function, method, type, class and interface.

以下区域在两套变体中均已配色（每套 144 个 UI 颜色）：编辑器本体（选区与失焦选区、当前行、词/选区高亮、查找匹配与高亮、括号匹配、光标、行号、标尺、缩进线、空白符、错误/警告/提示）；活动栏与角标、标题栏、侧边栏（含分节标题）、状态栏（含无文件夹与调试态）、标签栏；面板与各类浮窗（悬停、建议、通知、快速输入）、下拉与输入框、列表选中/悬停/高亮、树缩进线；终端 ANSI 全色；全部边框与滚动条、Git 装饰色与 gutter 标记、按钮与角标、差异编辑器底色，以及变量/参数/属性/函数/方法/类型/类/接口的语义高亮。完整的颜色清单见 `COLOR-SPEC.md`。

## Features / 功能

- **Two coordinated variants** — `Wisteria Blush Theme Light` and `Wisteria Blush Theme Dark` ship in one extension.
- **One flower palette** — porcelain lavender and charcoal violet surfaces with wisteria violet, dusty blush and peach accents.
- **Readable syntax colors** — wisteria keywords, sage strings, terracotta and peach numbers, tuned for contrast on both backgrounds.
- **Semantic highlighting** enabled, so language-aware tokens are colored beyond the classic TextMate scopes.
- **Terminal ANSI colors** taken from the same palette, so the integrated terminal sits inside the theme.

- **明暗两套协调变体**——同一扩展内含 `Wisteria Blush Theme Light` 与 `Wisteria Blush Theme Dark`。
- **一套花系色板**——瓷感淡紫与炭紫底色，配紫藤紫、灰粉与蜜桃点缀。
- **可读的语法配色**——紫藤紫关键字、鼠尾草绿字符串、陶土与蜜桃数字，在明暗底色上均保持对比。
- **启用语义高亮**，在传统 TextMate scope 之外为语言感知的 token 着色。
- **终端 ANSI 配色**取自同一色板，集成终端与主题融为一体。

## Installation / 安装

Requires VS Code 1.80 or newer.

1. Search for **Wisteria Blush Theme** in the Extensions view (`Ctrl+Shift+X` / `Cmd+Shift+X`), or open the [Marketplace page](https://marketplace.visualstudio.com/items?itemName=lilinhuang.wisteria-blush-theme).
2. Or install from a VSIX: download `wisteria-blush-theme-1.0.0.vsix`, open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run **Extensions: Install from VSIX...**.

需要 VS Code 1.80 或更高版本。

1. 在扩展面板（`Ctrl+Shift+X` / `Cmd+Shift+X`）搜索 **Wisteria Blush Theme**，或打开 [Marketplace 页面](https://marketplace.visualstudio.com/items?itemName=lilinhuang.wisteria-blush-theme)。
2. 也可以从 VSIX 安装：下载 `wisteria-blush-theme-1.0.0.vsix`，打开命令面板（`Ctrl+Shift+P` / `Cmd+Shift+P`），运行 **Extensions: Install from VSIX...** 并选择该文件。

Or from the command line:

或使用命令行：

```
ext install lilinhuang.wisteria-blush-theme
```

## Activation / 启用

Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`), run **Preferences: Color Theme**, and choose **Wisteria Blush Theme Light** or **Wisteria Blush Theme Dark**.

To switch between the two variants quickly, use the keyboard shortcut `Ctrl+K Ctrl+T` at any time.

打开命令面板（`Ctrl+Shift+P` / `Cmd+Shift+P`），运行 **Preferences: Color Theme**，选择 **Wisteria Blush Theme Light** 或 **Wisteria Blush Theme Dark**。

随时可用快捷键 `Ctrl+K Ctrl+T` 在两套变体之间快速切换。

## Development / 开发

Open this folder in VS Code and press `F5` to launch an Extension Development Host with the theme loaded. Regenerate the real-window preview screenshots with:

在 VS Code 中打开本文件夹并按 `F5`，在扩展开发宿主中预览主题。重新生成真实窗口预览图：

```bash
python3 scripts/capture-real-screenshots.py
```

The script builds a throwaway VS Code profile, installs this theme into it, opens the sample project under `scripts/demo-project` and captures the window for both variants into `store-assets/screenshots/en/`.

脚本会临时创建一个独立的 VS Code 配置目录，把本主题装进去，打开 `scripts/demo-project` 示例工程，并把两套变体的窗口截图输出到 `store-assets/screenshots/en/`。

Check a build before publishing:

发布前自查：

```bash
python3 scripts/validate.py
```

It refreshes `COLOR-SPEC.md` from the theme JSON files, verifies that every color value is a valid hex code, checks that the screenshot edges match `titleBar.activeBackground`, and — when a `.vsix` is present — verifies the manifest publisher, version and theme entries.

脚本会依据主题 JSON 重新生成 `COLOR-SPEC.md`，校验所有颜色值均为合法十六进制，检查截图首行/首列与 `titleBar.activeBackground` 一致，并在存在 `.vsix` 时校验清单里的发布者、版本与主题条目。

Package the extension with:

打包扩展：

```bash
vsce package
```

## License / 许可

Released under the **Non-Commercial License** — licensed for personal, educational and non-commercial use. See [LICENSE](LICENSE) for details.

基于 **Non-Commercial License（非商业使用许可）** 发布，可用于个人、教育及非商业用途，详见 [LICENSE](LICENSE)。

## Feedback / 反馈

Found an unthemed area or want a tweak? Open an issue at [github.com/vaxicy/wisteria-blush-theme/issues](https://github.com/vaxicy/wisteria-blush-theme/issues).

发现没有配色的区域或想调整某处颜色，欢迎在 [GitHub Issues](https://github.com/vaxicy/wisteria-blush-theme/issues) 反馈。

## Publisher / 发布者

Published by **lilinhuang** on the Visual Studio Code Marketplace.

由 **lilinhuang** 发布于 Visual Studio Code Marketplace。
