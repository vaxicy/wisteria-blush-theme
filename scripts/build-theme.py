import json, colorsys
from pathlib import Path
base=Path(__file__).resolve().parents[1];source=base.parent/'iris-cloud-theme'
for d in ['themes','assets','store-assets']: (base/d).mkdir(exist_ok=True)
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def recolor(x):
    if isinstance(x,dict):return {k:recolor(v) for k,v in x.items()}
    if isinstance(x,list):return [recolor(v) for v in x]
    if isinstance(x,str) and x.startswith('#'):
        rgb=[int(x[i:i+2],16)/255 for i in [1,3,5]];h,l,s=colorsys.rgb_to_hls(*rgb)
        if .48<h<.85:
            rgb=colorsys.hls_to_rgb(.79,l,min(s,.45));return '#'+''.join(f'{round(c*255):02X}' for c in rgb)+x[7:]
    return x
m=json.loads((source/'package.json').read_text());m.update(name='wisteria-blush-theme',displayName='Wisteria Blush Theme',description='Soft wisteria violet, dusty blush and peach in coordinated light and dark themes.',keywords=['theme','light','dark','wisteria','purple','pink','pastel']);m['galleryBanner']['color']='#302735'
for t in m['contributes']['themes']:t['label']=t['label'].replace('Iris Cloud','Wisteria Blush');t['path']=t['path'].replace('iris-cloud','wisteria-blush')
write(base/'package.json',m)
rows='''
editor.background tab.activeBackground|FCF9FD|302735
foreground editor.foreground terminal.foreground|514458|EADFEB
titleBar.activeBackground|EFE8F2|241F2A
titleBar.activeForeground|57485F|D6C6DC
titleBar.inactiveBackground|F4EFF5|201C25
titleBar.inactiveForeground|95869B|918099
activityBar.background|E7DDEA|201B26
activityBar.foreground|816395|E0BBE4
activityBar.activeBorder|A477AD|D291BC
activityBar.inactiveForeground|9B87A4|927E9E
sideBar.background|F3EDF5|292230
sideBar.foreground|615068|CFBDD6
sideBarSectionHeader.background|EDE3EF|342A3C
sideBarSectionHeader.foreground|72597C|E0CBE6
editorGroupHeader.tabsBackground tab.inactiveBackground|EEE5F0|241E2A
tab.inactiveForeground|94829B|A18AAB
tab.activeForeground|785687|FEC8D8
tab.activeBorderTop|B580B0|D291BC
panel.background terminal.background|F7F0F6|29222F
statusBar.background statusBar.noFolderBackground|E6D5E9|49344E
statusBar.foreground statusBar.noFolderForeground|674C72|F0D5EB
panel.border sideBar.border editorGroup.border tab.border titleBar.border|DFD2E3|4B3B55
editor.lineHighlightBackground|F4EBF5|3A2E40
editor.lineHighlightBorder|EADCEC|493750
editorLineNumber.foreground|AC98B3|846B90
editorLineNumber.activeForeground|856293|E0BBE4
editorCursor.foreground|A26394|FEC8D8
selection.background editor.selectionBackground terminal.selectionBackground|E7CFEA|62476D
editor.inactiveSelectionBackground|EAE0ED|4A3853
editor.wordHighlightBackground editor.wordHighlightStrongBackground editor.selectionHighlightBackground|EFE2F080|49374F99
list.activeSelectionBackground|E0BBE4|563C62
list.activeSelectionForeground list.inactiveSelectionForeground|5E416A|F3DCEC
list.inactiveSelectionBackground|EAE0ED|4A3853
list.hoverBackground|EFE3EF|3B2E43
editor.findMatchHighlightBackground|FFDFD3|684940
editor.findMatchBackground|F2C3B5|896252
editor.findMatchBorder|B78676|FFDFD3
editorBracketMatch.background|F3D9E8|563D59
editorBracketMatch.border|B58AAE|C394BE
editorIndentGuide.background1|E8DDEA|493650
editorIndentGuide.activeBackground1|B49ABE|916FA0
quickInput.background editorWidget.background editorHoverWidget.background editorSuggestWidget.background notifications.background|FBF5FB|3A2C42
input.background dropdown.background|FFFCFF|251E2B
input.border dropdown.border|D8C3DE|705479
focusBorder|A477AD|C798CF
editorSuggestWidget.selectedBackground|E7CFEA|563C62
editorSuggestWidget.selectedForeground|5E416A|F3DCEC
button.background|E0BBE4|E0BBE4
button.foreground|5E416A|402B49
button.hoverBackground|D4A9DC|F0CDEB
button.secondaryBackground|EEE2F0|503B58
button.secondaryForeground|72597C|EADFEB
badge.background activityBarBadge.background|957DAD|E0BBE4
badge.foreground activityBarBadge.foreground|FFFFFF|402B49
errorForeground editorError.foreground problemsErrorIcon.foreground|B45469|EE9BAE
editorWarning.foreground problemsWarningIcon.foreground|A17B3D|E8CB91
editorInfo.foreground problemsInfoIcon.foreground|587F96|B1CEDF
gitDecoration.addedResourceForeground gitDecoration.untrackedResourceForeground editorGutter.addedBackground|6B8B64|B6D5A9
gitDecoration.modifiedResourceForeground editorGutter.modifiedBackground|A17B3D|E8CB91
gitDecoration.deletedResourceForeground editorGutter.deletedBackground|B46C7E|E7A4B5
diffEditor.insertedTextBackground diffEditor.insertedLineBackground|E9F1E499|30402F99
diffEditor.removedTextBackground diffEditor.removedLineBackground|F7E4EB99|4B303E99
'''
palette={'comment':('A18FA6','A58BAE'),'keyword,storage':('A05C8B','E2A5CA'),'string':('657D65','BCD5B7'),'entity.name.function,support.function':('78609F','D6BCEB'),'entity.name.type,support.type,support.class':('926A9D','E0BBE4'),'constant.numeric,constant.language,variable.other.constant':('AE735D','FFDFD3'),'variable':('514458','EADFEB'),'variable.parameter':('8B708A','D5BED4'),'variable.other.property,support.variable.property':('527E83','AED1D2'),'keyword.operator':('88708F','CBB1D2'),'punctuation':('A18AA8','B298BB'),'entity.name.tag':('A05C8B','FEC8D8'),'entity.other.attribute-name':('92785A','E8C9A8')}
for i,v in enumerate(['light','dark']):
    t=recolor(json.loads((source/'themes'/f'iris-cloud-{v}-color-theme.json').read_text()));t['name']=f'Wisteria Blush Theme {v.title()}'
    for row in rows.strip().splitlines():
        keys,l,d=row.split('|')
        for k in keys.split():t['colors'][k]='#'+[l,d][i]
    for rule in t['tokenColors']:
        key=','.join(rule['scope'])
        if key in palette:rule['settings']['foreground']='#'+palette[key][i]
    for key,scope in {'variable':'variable','parameter':'variable.parameter','property':'variable.other.property,support.variable.property','function':'entity.name.function,support.function','method':'entity.name.function,support.function','class':'entity.name.type,support.type,support.class','type':'entity.name.type,support.type,support.class','interface':'entity.name.type,support.type,support.class','variable.readonly':'constant.numeric,constant.language,variable.other.constant'}.items():t['semanticTokenColors'][key]='#'+palette[scope][i]
    write(base/'themes'/f'wisteria-blush-{v}-color-theme.json',t)
for name in ['LICENSE','CHANGELOG.md','.vscodeignore']:(base/name).write_text((source/name).read_text(encoding='utf-8').replace('Iris Cloud','Wisteria Blush'),encoding='utf-8')
for name in ['capture-real-screenshots.py','validate.py']:(base/'scripts'/name).write_text((source/'scripts'/name).read_text(encoding='utf-8').replace('Iris Cloud','Wisteria Blush').replace('iris-cloud','wisteria-blush'),encoding='utf-8')
demo=base/'scripts/demo-project';demo.mkdir(exist_ok=True)
for p in (source/'scripts/demo-project').iterdir():
    if p.is_file():
        text=p.read_text(encoding='utf-8').replace('Iris Cloud','Wisteria Blush').replace('IrisCloud','WisteriaBlush').replace('ice blue, periwinkle and lavender','wisteria violet, dusty blush and peach').replace('cloud-inspired','flower-inspired').replace('CLOUD_PALETTE','FLOWER_PALETTE')
        for a,b in [('CCEDFC','E0BBE4'),('D1E2FD','957DAD'),('D6D9FD','D291BC'),('E2DAFE','FEC8D8'),('EFDFFE','FFDFD3')]:text=text.replace(a,b).replace(a.lower(),b.lower())
        for a,b in [('ice:','wisteria:'),('sky:','violet:'),('iris:','blush:'),('lavender:','pink:'),('lilac:','peach:'),('.ice','.wisteria'),('.lilac','.peach')]:text=text.replace(a,b)
        (demo/p.name).write_text(text,encoding='utf-8')
(base/'README.md').write_text('''# Wisteria Blush Theme

Soft wisteria violet, dusty blush and peach in coordinated light and dark themes.

紫藤浅绯：淡紫信纸般的浅色界面，搭配夜色紫藤般的深色界面。

## Variants

- **Wisteria Blush Theme Light** — porcelain lavender editor, violet panels and dusty rose accents.
- **Wisteria Blush Theme Dark** — charcoal violet editor, petal-pink keywords and soft sage strings.

| Region | Light | Dark |
| --- | --- | --- |
| Editor | `#FCF9FD` | `#302735` |
| Text | `#514458` | `#EADFEB` |
| Sidebar | `#F3EDF5` | `#292230` |
| Title bar | `#EFE8F2` | `#241F2A` |
| Status bar | `#E6D5E9` | `#49344E` |

Brand palette: `#E0BBE4`, `#957DAD`, `#D291BC`, `#FEC8D8`, `#FFDFD3`.

## Installation

Use **Extensions: Install from VSIX**, then select either appearance with **Preferences: Color Theme**.

Includes semantic highlighting, coordinated terminal colors, Git decorations, search and selection colors. Full UI colors are listed in `COLOR-SPEC.md`; real VS Code previews are included in `store-assets/screenshots/en/`.

Publisher: **lilinhuang** · Version: **1.0.0**

[Marketplace](https://marketplace.visualstudio.com/items?itemName=lilinhuang.wisteria-blush-theme)
''',encoding='utf-8')
print('Created',base)
