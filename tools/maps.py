"""示意图：北国以色列／南国犹大／撒马利亚／耶斯列谷／亚述方向。非比例，不画精确疆界。"""
import html
def esc(s): return html.escape(s)
def lines(txt,x,y,lh=16,anchor='middle',cls='svgt',extra=''):
    parts=txt.split('\n')
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" {extra}>'+''.join(
        f'<tspan x="{x}" dy="{0 if i==0 else lh}">{esc(p)}</tspan>' for i,p in enumerate(parts))+'</text>'
def card(x,y,w,h,title,body,fill,tc='#fff',fs=13,lh=16):
    y0=y+22
    t=f'<text x="{x+w/2}" y="{y+16}" text-anchor="middle" font-size="13" font-weight="800" fill="{tc}">{esc(title)}</text>'
    b=lines(body,x+w/2,y0+14,lh,'middle','',f'font-size="{fs}" font-weight="650" fill="{tc}"')
    return f'<g class="node"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="rgba(0,0,0,.12)"/>{t}{b}</g>'

def region():
    """区域框。坐标手排：色块上下左右留白，360 宽的 viewBox 缩到约 335px 时文字仍在各自色块内。"""
    W,H=360,1248
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="非比例示意图：北国以色列（撒马利亚、但、伯特利、耶斯列平原）、南国犹大（耶路撒冷），以及亚述与埃及的方向。不是历史疆界，也不是考古测绘图。">']
    o.append('<rect class="sea" width="360" height="1248" rx="12"/>')
    o.append('<rect x="10" y="10" width="340" height="34" rx="8" fill="#1d3d9e"/>')
    o.append(lines('非比例示意图 · 不是行政疆界 · 不是考古测点',180,32,16,'middle','','font-size="12.5" font-weight="800" fill="#fff"'))
    # panel 1 Israel
    o.append('<rect x="10" y="54" width="340" height="548" rx="12" fill="var(--glass-strong)" stroke="#0a9b6b" stroke-width="2"/>')
    o.append(lines('区域框 · 北在上 · 距离不按比例',180,78,16,'middle','svgt','font-size="14" font-weight="800"'))
    o.append(lines('北国以色列',180,98,16,'middle','svgt','font-size="13" font-weight="700"'))
    o.append(card(22,114,152,92,'但','金牛犊祭坛\n北境圣所\n王上12:29','#7a3ff2',fs=12.5,lh=16))
    o.append(card(186,114,152,92,'加利利','前733被攻取\n北方首当其冲\n王下15:29','#0a84c6',fs=12.5,lh=16))
    o.append(card(22,218,316,100,'耶斯列平原','米吉多至耶斯列谷\n何1:5 在此折断弓\n详见下方局部框','#e8590c',fs=13,lh=16))
    o.append(card(22,330,152,96,'撒马利亚','北国的首都\n先知称我们的王\n何7:5','#e0245e',fs=12.5,lh=16))
    o.append(card(186,330,152,96,'伯特利','金牛犊祭坛\n耶罗波安一世\n王上12:28','#7a3ff2',fs=12.5,lh=16))
    o.append(card(22,438,152,88,'基列','约旦河东\n北方的地名\n先知所熟悉','#0a9b6b',fs=12.5,lh=16))
    o.append(card(186,438,152,88,'亚述来向','自东北入侵\n前733与前722\n尼尼微在图外','#1d3d9e',fs=12.5,lh=16))
    o.append(lines('埃及在图外西南：北国曾投靠埃及与亚述（何7:11）。',180,548,16,'middle','svgm','font-size="11.5"'))
    o.append(lines('箭头只表方向，经文没有画出行军的精确路线。',180,568,16,'middle','svgm','font-size="11.5"'))
    # panel 2 Judah
    o.append('<rect x="10" y="616" width="340" height="236" rx="12" fill="var(--glass-strong)" stroke="#2d5be3" stroke-width="2"/>')
    o.append(lines('南国犹大 · 耶路撒冷',180,640,16,'middle','svgt','font-size="14" font-weight="800"'))
    o.append(card(22,656,316,112,'耶路撒冷','犹大的京城\n何1:7 要怜悯犹大家\n前701不靠弓刀蒙救\n王下19:35','#2d5be3',fs=13,lh=16))
    o.append(lines('怜悯是白白的恩典，不是犹大比以色列更配。',180,792,16,'middle','svgm','font-size="11.5"'))
    o.append(lines('北国灭亡成为南国的警钟（何4:15）。',180,814,16,'middle','svgm','font-size="11.5"'))
    # panel 3 arrows
    o.append('<rect x="10" y="866" width="340" height="352" rx="12" fill="var(--glass-strong)" stroke="#d99100" stroke-width="2"/>')
    o.append(lines('两次入侵与图外方向',180,890,16,'middle','svgt','font-size="14" font-weight="800"'))
    o.append('<path class="route dash" d="M36,918 L36,1168" stroke="#1d3d9e" style="stroke-width:2.5px"/>')
    o.append('<polygon points="30,1164 36,1178 42,1164" fill="#1d3d9e"/>')
    o.append(lines('北',36,912,16,'middle','svgt','font-size="12" font-weight="800"'))
    o.append(card(56,916,280,88,'前733','提革拉毗列色三世\n攻取加利利与北方\n耶斯列平原首当其冲','#e0245e',fs=12.5,lh=16))
    o.append(card(56,1016,280,88,'前722／721','撒缦以色与撒珥根\n攻陷撒马利亚\n北国灭亡 · 王下17:6','#7a3ff2',fs=12.5,lh=16))
    o.append(card(56,1116,280,78,'埃及 · 图外西南','政治上的投靠\n何7:11 鸽子无智\n不是本图的疆界','#0a9b6b',fs=12.5,lh=16))
    o.append('</svg>')
    return ''.join(o)

def jezreel():
    W,H=360,900
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="耶斯列谷局部示意图：耶斯列城、米吉多、基利波山、他泊山，以及拿伯、耶户、折弓三件相关的事。非比例。">']
    o.append('<rect class="sea" width="360" height="900" rx="12"/>')
    o.append('<rect x="10" y="10" width="340" height="34" rx="8" fill="#e8590c"/>')
    o.append(lines('局部框 · 耶斯列谷 · 非比例',180,32,16,'middle','','font-size="13" font-weight="800" fill="#fff"'))
    o.append('<rect x="10" y="54" width="340" height="826" rx="12" fill="var(--glass-strong)" stroke="#e8590c" stroke-width="2"/>')
    o.append(lines('北在上 · 山名只表通常方位',180,78,16,'middle','svgt','font-size="14" font-weight="800"'))
    o.append(card(22,96,152,100,'他泊山','谷的北缘\n地标\n不是测点','#0a84c6',fs=12.5,lh=16))
    o.append(card(186,96,152,100,'米吉多','谷地西端\n古代要道\n与平原并提','#2d5be3',fs=12.5,lh=16))
    o.append(card(22,208,152,100,'耶斯列城','城在谷中\n拿伯的葡萄园\n在其附近','#e0245e',fs=12.5,lh=16))
    o.append(card(186,208,152,100,'基利波山','谷的南缘\n扫罗战死之地\n撒上31','#7a3ff2',fs=12.5,lh=16))
    o.append(lines('同一条谷里的三件事',180,336,16,'middle','svgt','font-size="14" font-weight="800"'))
    o.append(card(22,352,316,112,'拿伯的葡萄园','亚哈夺园、耶洗别害命\n流血从这里被记住\n王上21','#e0245e',fs=13,lh=16))
    o.append(card(22,476,316,112,'耶户在耶斯列','杀约兰与耶洗别\n也波及犹大王室\n王下9至10章','#7a3ff2',fs=13,lh=16))
    o.append(card(22,600,316,112,'折断以色列的弓','何1:5 所指的平原\n前733与前722战败\n国在此被打断','#1d3d9e',fs=13,lh=16))
    o.append(lines('三件事放在同一框里，是为了听见名字的回声。',180,740,16,'middle','svgm','font-size="11.5"'))
    o.append(lines('城与山的圆点没有画出，避免和文字叠在一起。',180,762,16,'middle','svgm','font-size="11.5"'))
    o.append(lines('这不是海拔图，也不是考古平面图。',180,784,16,'middle','svgm','font-size="11.5"'))
    o.append('</svg>')
    return ''.join(o)

def _pills(x,y,w,judge,rev):
    gap=12
    pw=(w-gap)/2
    h=78
    a=card(x,y,pw,h,'审判',judge,'#e0245e',fs=12.5,lh=16)
    b=card(x+pw+gap,y,pw,h,'反转',rev,'#0a9b6b',fs=12.5,lh=16)
    return a+b

def family():
    W,H=360,980
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="何西阿与歌篾的家谱式图：儿子耶斯列、女儿罗路哈玛、儿子罗阿米。每个名字旁有审判与反转两色标签。">']
    o.append('<rect class="sea" width="360" height="980" rx="12"/>')
    o.append(card(20,12,320,72,'何西阿的家','三个孩子是三篇活的讲章','#1d3d9e',fs=13,lh=16))
    o.append(card(16,100,160,96,'何西阿','备利的儿子\n名字意为拯救\n与约书亚同根','#2d5be3',fs=12.5,lh=16))
    o.append(card(184,100,160,96,'歌篾','滴拉音的女儿\n何1:3 所娶\n不忠的妻子','#e0245e',fs=12.5,lh=16))
    o.append('<path d="M180,196 L180,228" stroke="#596277" stroke-width="2.4"/>')
    o.append(card(20,228,320,78,'耶斯列 · 儿子','神播种，也可指神播散','#e8590c',fs=13,lh=16))
    o.append(_pills(20,318,320,'讨耶户家的罪\n弓在平原折断','日后称为栽种\n耶斯列的大日'))
    o.append(card(20,412,320,78,'罗·路哈玛 · 女儿','不蒙怜悯','#7a3ff2',fs=13,lh=16))
    o.append(_pills(20,502,320,'收回母腹般的爱\n不再怜悯以色列家','后来仍要怜悯\n彼前2:10'))
    o.append(card(20,596,320,78,'罗·阿米 · 儿子','非我民','#e0245e',fs=13,lh=16))
    o.append(_pills(20,686,320,'圣约公式被倒转\n我也不是你们的神','永生神的儿子\n罗9:26'))
    o.append(lines('左红为审判，右绿为反转。第2、3个孩子是否亲生，经文没有断定。',180,792,16,'middle','svgm','font-size="11.5"'))
    o.append(lines('断奶的间隔表示宣告是渐进的（何1:8）。',180,814,16,'middle','svgm','font-size="11.5"'))
    o.append('</svg>')
    return ''.join(o)

def mindmap():
    W,H=360,760
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="思维导图：何西阿书1章，从背景到三个要点，再到新妇主线的闭环。">']
    o.append('<rect class="sea" width="360" height="760" rx="12"/>')
    o.append(card(30,12,300,72,'何西阿书1章','一镜三名一然而','#1d3d9e',fs=13,lh=16))
    rows=[
        (100,'#e8590c','背景','耶罗波安二世的繁荣\n巴力、牛犊、亚述'),
        (214,'#e0245e','一 · 命令娶','婚姻是镜子\n圣约就是婚约'),
        (328,'#7a3ff2','二 · 三个名字','耶斯列 · 罗路哈玛\n罗阿米：非我民'),
        (442,'#2d5be3','三 · 顺服与然而','先知没有讨价还价\n非我民成为儿子'),
        (556,'#0a9b6b','闭环','创2的婚姻到启19\n罪、救赎、感恩'),
    ]
    prev=84
    for y,c,t,b in rows:
        o.append(f'<path d="M180,{prev} L180,{y}" stroke="{c}" stroke-width="3" opacity=".8"/>')
        o.append(card(30,y,300,100,t,b,c,fs=13,lh=17))
        prev=y+100
    o.append(lines('缩小到手机宽度时，文字仍留在各自色块内。',180,732,16,'middle','svgm','font-size="11.5"'))
    o.append('</svg>')
    return ''.join(o)

def paths():
    W,H=360,520
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="流程图：离弃耶和华的旧路，与然而之后恩典的新路。">']
    o.append('<rect class="sea" width="360" height="520" rx="12"/>')
    o.append(lines('旧路与恩典的新路',180,28,16,'middle','svgt','font-size="15" font-weight="800"'))
    old=['享恩归巴力','离弃耶和华','耶斯列折弓','不蒙怜悯','非我民']
    new=['然而','应许如海沙','新郎舍命','圣灵赐新心','你是我的民']
    for i,t in enumerate(old):
        y=48+i*86
        o.append(card(12,y,160,70,f'旧 {i+1}',t,'#e0245e',fs=13,lh=16))
        if i<len(old)-1:
            o.append(f'<path d="M92,{y+70} L92,{y+86}" stroke="#e0245e" stroke-width="2.4"/>')
    for i,t in enumerate(new):
        y=48+i*86
        o.append(card(188,y,160,70,f'新 {i+1}',t,'#0a9b6b',fs=13,lh=16))
        if i<len(new)-1:
            o.append(f'<path d="M268,{y+70} L268,{y+86}" stroke="#0a9b6b" stroke-width="2.4"/>')
    o.append('</svg>')
    return ''.join(o)

def loop_redemptive():
    W,H=360,820
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="救赎历史闭环：从亚伯拉罕的应许，经西乃婚约与北国背约，到基督、福音与羔羊婚筵。">']
    o.append('<rect class="sea" width="360" height="820" rx="12"/>')
    o.append(lines('救赎历史闭环',180,28,16,'middle','svgt','font-size="15" font-weight="800"'))
    steps=[
        ('亚伯拉罕','后裔如海沙','#0a9b6b'),
        ('西乃','神娶以色列为妻','#0a84c6'),
        ('北国','牛犊、巴力、背约','#e0245e'),
        ('何西阿','用婚姻把罪显出来','#e8590c'),
        ('前722','罗阿米在历史上应验','#7a3ff2'),
        ('基督','一个首领，新郎舍命','#2d5be3'),
        ('福音','非我民成为子民','#0a9b6b'),
        ('婚筵','启19与启21的完成','#d99100'),
    ]
    for i,(a,b,c) in enumerate(steps):
        y=44+i*90
        o.append(card(70,y,220,72,a,b,c,fs=13,lh=18))
        if i<len(steps)-1:
            o.append(f'<path d="M180,{y+72} L180,{y+90}" stroke="{c}" stroke-width="2.4" stroke-dasharray="4 3"><animate attributeName="stroke-dashoffset" from="14" to="0" dur="1s" repeatCount="indefinite"/></path>')
    o.append('<path d="M292,80 C348,360 348,620 292,746" fill="none" stroke="#1d3d9e" stroke-width="2" stroke-dasharray="5 4" opacity=".55"/>')
    o.append(lines('虚线回到同一位神的应许，不是另立一位神。',180,792,16,'middle','svgm','font-size="11.5"'))
    o.append('</svg>')
    return ''.join(o)

def triad():
    W,H=360,460
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="罪、救赎、感恩：歌篾般的不忠，新郎为新妇舍命，并以忠贞回应。">']
    o.append('<rect class="sea" width="360" height="460" rx="12"/>')
    o.append(lines('罪 — 救赎 — 感恩',180,28,16,'middle','svgt','font-size="15" font-weight="800"'))
    o.append(card(24,46,312,100,'① 罪','这地大行淫乱\n三个名字宣判审判\n我常把恩赐归给别神','#e0245e',fs=14,lh=18))
    o.append('<path d="M180,146 L180,166" stroke="#596277" stroke-width="2.4"/>')
    o.append(card(24,166,312,108,'② 救赎','然而，你们是儿子\n基督为不忠的新妇舍命\n不是因为她先变忠贞','#2d5be3',fs=14,lh=18))
    o.append('<path d="M180,274 L180,294" stroke="#596277" stroke-width="2.4"/>')
    o.append(card(24,294,312,108,'③ 感恩','称呼他为丈夫\n唯独敬拜，婚姻贞洁\n在祷告中感谢','#0a9b6b',fs=14,lh=18))
    o.append(lines('这是蒙恩之后的生活，不是赚得爱的方法。',180,430,16,'middle','svgm','font-size="12"'))
    o.append('</svg>')
    return ''.join(o)

REG={'region':region,'jezreel':jezreel,'family':family,'mindmap':mindmap,'paths':paths,'loop-redemptive':loop_redemptive,'triad':triad}
CAP={
 'region':'示意图，不是比例地图。上框是北国：但与伯特利的金牛犊、加利利、耶斯列平原、撒马利亚与基列，并标明亚述自东北而来。中框是犹大与耶路撒冷。下框用箭头标出约前733年与前722/721年两次打击，埃及在图外西南。不同时代的行政疆界没有画出。城点不是考古坐标。',
 'jezreel':'耶斯列谷局部框：他泊山在北、基利波山在南、米吉多在西、耶斯列城在谷中，都是通常的方位，不是测量数据。三张色块对应拿伯、耶户、以及何西阿书1:5的折弓。',
 'family':'家谱式图。何西阿与歌篾之下是三个孩子。每个名字下有两色标签：红色是审判，绿色是后来的反转。',
 'mindmap':'讲章思维导图。色块上下相接，缩小到手机宽度时文字仍留在色块内。',
 'paths':'两条路。左为离弃之约的旧路，右为「然而」之后恩典的新路。',
 'loop-redemptive':'救赎历史闭环。右侧虚线表示终点不是另一位神，而是同一位神的应许在羔羊婚筵里完成。',
 'triad':'海德堡要理问答问2的三件事，用在本讲：罪、救赎、感恩。',
}
def render(name):
    name=name.strip(); svg=REG[name]()
    cls='svg-wrap map' if name in ('region','jezreel') else 'svg-wrap'
    return f'<figure class="{cls}">{svg}<figcaption class="svg-cap">{esc(CAP[name])}</figcaption></figure>'
