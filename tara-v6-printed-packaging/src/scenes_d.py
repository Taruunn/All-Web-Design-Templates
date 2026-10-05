from bot import *
from lid import garden_lid
import random
def linen(W,H,base="#E8E1D5",light="#F3EEE6"):
    return (f'<radialGradient id="bgl" cx=".3" cy=".2" r="1"><stop offset="0" stop-color="{light}"/><stop offset="1" stop-color="{base}"/></radialGradient>'
            f'<rect width="{W}" height="{H}" fill="url(#bgl)"/>'
            f'<rect width="{W}" height="{H}" filter="url(#noise)" opacity="0.09" style="mix-blend-mode:multiply"/>')
def sprig_set(seed=1):
    random.seed(seed)
    return [lambda: g(orchid(),0,0,random.uniform(-25,25),0.9),
            lambda: g(frangipani(),0,0,random.uniform(0,72),0.9),
            lambda: g(persimmon(r=11),0,0,random.uniform(-15,15),1),
            lambda: g(leaf(40,12),0,0,random.uniform(0,360)),
            lambda: g(fan_palm(R=46,spread=150,n=9),0,0,random.uniform(-30,30))]
def toss(W,H,step=150,seed=3,scale=1.0,skip=()):
    random.seed(seed); out=[]
    motifs=sprig_set(seed)
    j=0
    for row in range(int(H/step)+2):
        for col in range(int(W/step)+2):
            x=col*step+(step/2 if row%2 else 0)+random.uniform(-18,18); y=row*step+random.uniform(-18,18)
            m=motifs[(row*3+col*2+j)%len(motifs)]; j+=1
            out.append(f'<g transform="translate({x:.1f},{y:.1f}) scale({scale})">{m()}</g>')
    return "".join(out)
def d_hero(W=1640,H=1200):
    S=1000; lid,_=garden_lid(S)
    sc=0.80; cx,cy=700,600; rot=-5
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS,linen(W,H)]
    # tissue sheet on the right, printed with tossed sprigs at low strength
    p.append('<clipPath id="tis"><path d="M1060,180 L1700,120 L1700,1120 L1120,1180 Z"/></clipPath>')
    p.append('<path d="M1060,180 L1700,120 L1700,1120 L1120,1180 Z" fill="#000" opacity="0.10" filter="url(#soft2)" transform="translate(6,10)"/>')
    p.append(f'<g clip-path="url(#tis)"><rect x="1000" y="100" width="760" height="1100" fill="#F7F4EE"/>'
             f'<g opacity="0.42" transform="rotate(8 1380 650)">{toss(1900,1400,170,seed=5,scale=0.9)}</g>'
             f'<linearGradient id="fold" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".48" stop-color="#fff" stop-opacity=".0"/><stop offset=".5" stop-color="#000" stop-opacity=".06"/><stop offset=".56" stop-color="#fff" stop-opacity=".25"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
             f'<rect x="1000" y="100" width="760" height="1100" fill="url(#fold)"/>'
             f'<rect x="1000" y="100" width="760" height="1100" filter="url(#noise)" opacity="0.06" style="mix-blend-mode:multiply"/></g>')
    # wax seal on the tissue
    sx,sy=1400,860
    p.append(f'<circle cx="{sx+6}" cy="{sy+9}" r="62" fill="#000" opacity="0.25" filter="url(#soft2)"/>')
    p.append(f'<radialGradient id="wax" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#2A3346"/><stop offset=".7" stop-color="#151B28"/><stop offset="1" stop-color="#0B0F17"/></radialGradient>')
    p.append(f'<path d="M{sx-60},{sy} C{sx-62},{sy-34} {sx-30},{sy-64} {sx+4},{sy-61} C{sx+40},{sy-62} {sx+64},{sy-30} {sx+60},{sy+4} C{sx+63},{sy+36} {sx+32},{sy+62} {sx-2},{sy+60} C{sx-38},{sy+63} {sx-63},{sy+34} {sx-60},{sy}Z" fill="url(#wax)"/>')
    p.append(f'<circle cx="{sx}" cy="{sy}" r="42" fill="none" stroke="#2C364B" stroke-width="3"/><circle cx="{sx}" cy="{sy}" r="41" fill="none" stroke="#06080D" stroke-width="1.2" opacity=".7"/>')
    p.append(brandstar(sx+1,sy+1,14,"#06080D")+brandstar(sx,sy,14,"#323D55"))
    # huggies
    for (hx,hy,r) in ((1255,1030,26),(1318,1062,26)):
        p.append(f'<circle cx="{hx+3}" cy="{hy+5}" r="{r}" fill="none" stroke="#000" stroke-opacity=".22" stroke-width="10" filter="url(#soft2)"/>')
        p.append(f'<circle cx="{hx}" cy="{hy}" r="{r}" fill="none" stroke="url(#foil)" stroke-width="9"/>')
        p.append(f'<path d="M{hx-r*0.7},{hy-r*0.7} A{r},{r} 0 0 1 {hx+r*0.2},{hy-r*0.98}" fill="none" stroke="#FFF6DD" stroke-width="2.5" stroke-linecap="round" opacity=".8"/>')
    # lid shadow + lid
    half=S*sc/2
    p.append(f'<g transform="translate({cx},{cy}) rotate({rot})">'
             f'<rect x="{-half+14}" y="{-half+26}" width="{S*sc}" height="{S*sc}" fill="#3A3226" opacity="0.30" filter="url(#soft)"/>'
             f'<rect x="{-half-3}" y="{-half-3}" width="{S*sc+6}" height="{S*sc+6}" fill="#DCD4C6"/>'
             f'<g transform="translate({-half},{-half}) scale({sc})">{lid}'
             f'<rect width="{S}" height="{S}" filter="url(#noise)" opacity="0.07" style="mix-blend-mode:multiply"/>'
             f'<linearGradient id="lidlight" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".18"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".05"/></linearGradient>'
             f'<rect width="{S}" height="{S}" fill="url(#lidlight)"/></g></g>')
    p.append('</svg>')
    return "\n".join(p)
def d_bag(W=1612,H=920):
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS]
    p.append(f'<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F1ECE4"/><stop offset="1" stop-color="#E9E3D9"/></linearGradient><rect width="{W}" height="{H*0.80}" fill="url(#wall)"/>')
    p.append(f'<rect y="{H*0.80}" width="{W}" height="{H*0.20}" fill="#DED6C8"/><rect width="{W}" height="{H}" filter="url(#noise)" opacity="0.08" style="mix-blend-mode:multiply"/>')
    # bag geometry
    bx0,bx1,by0,by1=620,1000,250,850; gus=58
    p.append(f'<ellipse cx="{(bx0+bx1)/2+60}" cy="{by1+8}" rx="300" ry="26" fill="#3A3226" opacity=".28" filter="url(#soft)"/>')
    # gusset (right side)
    p.append(f'<path d="M{bx1},{by0} L{bx1+gus},{by0+18} L{bx1+gus},{by1-10} L{bx1},{by1} Z" fill="#E2DACC"/>')
    p.append(f'<path d="M{bx1+gus*0.5},{by0+9} L{bx1+gus*0.5},{by1-5}" stroke="#CFC6B6" stroke-width="2"/>')
    # front face
    bw=bx1-bx0; bh=by1-by0
    p.append(f'<clipPath id="bf"><rect x="{bx0}" y="{by0}" width="{bw}" height="{bh}"/></clipPath>')
    p.append(f'<g clip-path="url(#bf)"><rect x="{bx0}" y="{by0}" width="{bw}" height="{bh}" fill="{MOON}"/>')
    # garden rising from the bottom (scaled lid-style clusters)
    S=bw; base=by1
    art=[]
    art.append(g(fan_palm(R=150,spread=170,n=13),bx0+40,base+30,25))
    art.append(orchid_spray([(bx0+90,base+20),(bx0+96,base-60),(bx0+108,base-130),(bx0+104,base-190),(bx0+92,base-236)],[(1,-8,0.95),(2,8,0.9),(3,-10,0.8)],[(4,-25,0.8)]))
    art.append(g(frangipani(),bx0+170,base-20,10,1.1))
    art.append(g(leaf(52,14),bx0+210,base-8,40))
    art.append(g(frangipani(),bx0+250,base+6,-20,0.95))
    art.append(stem(f"M{bx1+10},{base-200} C{bx1-40},{base-170} {bx1-70},{base-120} {bx1-95},{base-60}",LW*1.4))
    art.append(g(leaf(46,15),bx1-40,base-176,-120)); art.append(g(leaf(44,14),bx1-78,base-120,-100))
    art.append(g(persimmon(r=18),bx1-60,base-140,6)); art.append(g(persimmon(r=15),bx1-96,base-50,-8))
    art.append(g(fan_palm(R=130,spread=160,n=11),bx1-10,base+30,-28))
    art.append(g(frangipani(),bx0+bw*0.58,base-6,25,1.0))
    p.append("".join(art))
    p.append(f'<rect x="{bx0}" y="{by0}" width="{bw}" height="{bh}" filter="url(#noise)" opacity="0.07" style="mix-blend-mode:multiply"/>')
    p.append(f'<linearGradient id="bagl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".25"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".06"/></linearGradient><rect x="{bx0}" y="{by0}" width="{bw}" height="{bh}" fill="url(#bagl)"/>')
    # top fold band
    p.append(f'<rect x="{bx0}" y="{by0}" width="{bw}" height="44" fill="#000" opacity=".035"/><line x1="{bx0}" y1="{by0+44}" x2="{bx1}" y2="{by0+44}" stroke="#D8D0C2" stroke-width="1.5"/>')
    p.append('</g>')
    # arch window with logo
    ax0,ax1,at,ab=bx0+bw*0.36,bx0+bw*0.64,by0+110,by0+300; r=(ax1-ax0)/2
    p.append(f'<path d="M{ax0},{ab} L{ax0},{at+r} A{r},{r} 0 0 1 {ax1},{at+r} L{ax1},{ab} Z" fill="none" stroke="url(#foilH)" stroke-width="2.2"/>')
    p.append(wordmark((bx0+bx1)/2,by0+222,bw*0.19,MID,"url(#foil)"))
    p.append(brandstar((bx0+bx1)/2,at+42,5,"url(#foil)"))
    # rope handles (midnight cord)
    for hx in (bx0+bw*0.33, bx0+bw*0.67):
        pass
    p.append(f'<path d="M{bx0+bw*0.30},{by0+26} C{bx0+bw*0.28},{by0-150} {bx0+bw*0.72},{by0-150} {bx0+bw*0.70},{by0+26}" fill="none" stroke="#0B0F17" stroke-width="9" stroke-linecap="round"/>')
    p.append(f'<path d="M{bx0+bw*0.30},{by0+26} C{bx0+bw*0.28},{by0-150} {bx0+bw*0.72},{by0-150} {bx0+bw*0.70},{by0+26}" fill="none" stroke="#3A4560" stroke-width="2.5" stroke-dasharray="6 7" stroke-linecap="round" opacity=".7"/>')
    for hx in (bx0+bw*0.30, bx0+bw*0.70):
        p.append(f'<circle cx="{hx}" cy="{by0+28}" r="7" fill="url(#foil)" stroke="#8E7444" stroke-width="1"/>')
    p.append('</svg>')
    return "\n".join(p)
def d_flat(W=1612,H=920):
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS,f'<rect width="{W}" height="{H}" fill="{MOON}"/>']
    p.append(f'<g transform="translate(-40,-40)">{toss(W+100,H+100,230,seed=11,scale=1.55)}</g>')
    p.append(f'<rect width="{W}" height="{H}" filter="url(#noise)" opacity="0.06" style="mix-blend-mode:multiply"/>')
    p.append('</svg>')
    return "\n".join(p)
if __name__=="__main__":
    open('d-hero.svg','w').write(d_hero()); open('d-bag.svg','w').write(d_bag()); open('d-flat.svg','w').write(d_flat())
