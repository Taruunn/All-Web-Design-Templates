from bot import *
from lid import garden_lid
from scenes_d import linen
import random, math
def cl_orchid():
    return (orchid_spray([(0,70),(4,20),(10,-20),(8,-46),(0,-66)],[(1,-10,0.8),(2,12,0.72)],[(3,-15,0.75),(4,-30,0.6)])
            + g(leaf(38,11),2,72,-50) + g(leaf(34,10),3,70,55))
def cl_frang():
    return g(leaf(44,13),0,0,-35)+g(leaf(40,12),0,0,40)+g(frangipani(),-4,-6,15,0.95)+g(frangipani(),20,12,-30,0.7)
def cl_pers():
    return (stem("M-40,-30 C-20,-26 0,-14 14,8",LW*1.3)+g(leaf(36,12),-24,-27,-120)+g(leaf(32,11),-6,-18,150)
            +g(persimmon(r=13),14,18,4)+g(persimmon(r=11),-12,-6,-10))
def cl_palm():
    return g(fan_palm(R=58,spread=150,n=11),0,20,0)+g(frangipani(),18,22,20,0.6)
def cl_bird():
    return stem("M-46,6 C-20,0 10,-2 40,-10",LW*1.2)+g(leaf(28,9),-30,3,-60)+g(leaf(26,8),22,-6,-120)+g(sunbird(),0,0,-4,0.9)
CL=[cl_orchid,cl_frang,cl_pers,cl_palm,cl_orchid,cl_frang,cl_bird,cl_palm]
def garden_repeat(W,H,step=220,scale=1.0,seed=7,opacity=1):
    random.seed(seed); out=[]
    k=0
    for row in range(-1,int(H/(step*0.62))+2):
        for col in range(-1,int(W/step)+2):
            x=col*step+(step/2 if row%2 else 0); y=row*step*0.62
            m=CL[(row*5+col*3)%len(CL)]
            rot=[-14,10,-6,16][(row+col)%4]
            out.append(f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot}) scale({scale})" opacity="{opacity}">{m()}</g>')
    return "".join(out)
def d_flat(W=1612,H=920):
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS,f'<rect width="{W}" height="{H}" fill="{MOON}"/>']
    p.append(garden_repeat(W,H,step=340,scale=1.35))
    p.append(f'<rect width="{W}" height="{H}" filter="url(#noise)" opacity="0.06" style="mix-blend-mode:multiply"/></svg>')
    return "\n".join(p)
def ribbon(d, w=30):
    return (f'<path d="{d}" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="{w}" stroke-linecap="butt" filter="url(#soft2)" transform="translate(5,9)"/>'
            f'<path d="{d}" fill="none" stroke="#B89DA9" stroke-width="{w}" stroke-linecap="butt"/>'
            f'<path d="{d}" fill="none" stroke="#D9C6CE" stroke-width="{w*0.45}" stroke-linecap="butt" opacity=".9"/>'
            f'<path d="{d}" fill="none" stroke="#F1E6EA" stroke-width="{w*0.12}" stroke-linecap="butt" opacity=".8" transform="translate(-2,-3)"/>')
def d_hero(W=1640,H=1200):
    S=1000; lid,_=garden_lid(S)
    sc=0.88; cx,cy=700,600; rot=-4
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS,linen(W,H)]
    tis="M1080,150 L1720,90 L1720,1140 L1140,1200 Z"
    p.append(f'<path d="{tis}" fill="#000" opacity="0.10" filter="url(#soft2)" transform="translate(6,10)"/>')
    p.append(f'<clipPath id="tis"><path d="{tis}"/></clipPath><g clip-path="url(#tis)"><rect x="1000" y="60" width="800" height="1200" fill="#F7F4EE"/>'
             f'<g opacity="0.32" transform="rotate(6 1400 650)">{garden_repeat(1900,1500,step=230,scale=1.0,seed=3)}</g>'
             f'<linearGradient id="tl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".35"/><stop offset="1" stop-color="#000" stop-opacity=".04"/></linearGradient>'
             f'<rect x="1000" y="60" width="800" height="1200" fill="url(#tl)"/>'
             f'<path d="M1300,60 C1320,500 1290,800 1330,1260" stroke="#000" stroke-opacity=".05" stroke-width="10" fill="none" filter="url(#soft2)"/>'
             f'<rect x="1000" y="60" width="800" height="1200" filter="url(#noise)" opacity="0.06" style="mix-blend-mode:multiply"/></g>')
    # ribbon tail under lid, curling out at lower left
    # seal
    sx,sy=1450,880
    p.append(f'<circle cx="{sx+6}" cy="{sy+9}" r="56" fill="#000" opacity="0.28" filter="url(#soft2)"/>')
    p.append(f'<radialGradient id="wax" cx=".38" cy=".32" r=".8"><stop offset="0" stop-color="#34405A"/><stop offset=".55" stop-color="#161D2B"/><stop offset="1" stop-color="#0A0E16"/></radialGradient>')
    pts=[]; random.seed(4)
    for i in range(18):
        a=i/18*2*math.pi; rr=54+random.uniform(-4,4); pts.append((sx+rr*math.cos(a), sy+rr*math.sin(a)))
    d="M"+" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)+"Z"
    p.append(f'<path d="{d}" fill="url(#wax)" stroke="#0A0E16" stroke-width="2" stroke-linejoin="round"/>')
    p.append(f'<circle cx="{sx}" cy="{sy}" r="38" fill="#121826" stroke="#2E3850" stroke-width="2.5"/>')
    p.append(brandstar(sx+1.5,sy+2,12,"#05070B")+brandstar(sx,sy,12,"#3A4663"))
    p.append(f'<path d="M{sx-34},{sy-26} A44,44 0 0 1 {sx+8},{sy-44}" fill="none" stroke="#fff" stroke-opacity=".28" stroke-width="4" stroke-linecap="round"/>')
    for (hx,hy,r) in ((1300,1050,24),(1362,1078,24)):
        p.append(f'<circle cx="{hx+3}" cy="{hy+5}" r="{r}" fill="none" stroke="#000" stroke-opacity=".22" stroke-width="10" filter="url(#soft2)"/>')
        p.append(f'<circle cx="{hx}" cy="{hy}" r="{r}" fill="none" stroke="url(#foil)" stroke-width="9"/>')
        p.append(f'<path d="M{hx-r*0.7},{hy-r*0.7} A{r},{r} 0 0 1 {hx+r*0.2},{hy-r*0.98}" fill="none" stroke="#FFF6DD" stroke-width="2.5" stroke-linecap="round" opacity=".8"/>')
    half=S*sc/2
    p.append(f'<g transform="translate({cx},{cy}) rotate({rot})">'
             f'<rect x="{-half+16}" y="{-half+28}" width="{S*sc}" height="{S*sc}" fill="#3A3226" opacity="0.32" filter="url(#soft)"/>'
             f'<rect x="{-half-3}" y="{-half-3}" width="{S*sc+6}" height="{S*sc+6}" fill="#D9D1C3"/>'
             f'<g transform="translate({-half},{-half}) scale({sc})">{lid}'
             f'<rect width="{S}" height="{S}" filter="url(#noise)" opacity="0.07" style="mix-blend-mode:multiply"/>'
             f'<linearGradient id="lidlight" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".18"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".05"/></linearGradient>'
             f'<rect width="{S}" height="{S}" fill="url(#lidlight)"/></g></g>')
    p.append('</svg>')
    return "\n".join(p)
def box_oblique(x, y, w, lidh, baseh, depth, lidart_id, shift=None):
    shift = depth*0.55 if shift is None else shift
    s=""
    s+=f'<ellipse cx="{x+w/2+40}" cy="{y+lidh+baseh+6}" rx="{w*0.64}" ry="18" fill="#3A3226" opacity=".26" filter="url(#soft)"/>'
    # right side faces (receding)
    s+=f'<path d="M{x+w-6},{y+lidh} L{x+w-6+shift},{y+lidh-depth} L{x+w-6+shift},{y+lidh+baseh-depth} L{x+w-6},{y+lidh+baseh} Z" fill="#070A10"/>'
    s+=f'<path d="M{x+w},{y} L{x+w+shift},{y-depth} L{x+w+shift},{y+lidh-depth} L{x+w},{y+lidh} Z" fill="#D6CEBF"/>'
    # base front
    s+=f'<rect x="{x+6}" y="{y+lidh-4}" width="{w-12}" height="{baseh+4}" fill="#10151F"/>'
    s+=f'<linearGradient id="baseL" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".07"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient>'
    s+=f'<rect x="{x+6}" y="{y+lidh-4}" width="{w-12}" height="{baseh+4}" fill="url(#baseL)"/>'
    s+=wordmark(x+w/2, y+lidh+baseh*0.52, w*0.28, "url(#foil)", "url(#foil)")
    # lid band front
    s+=f'<rect x="{x}" y="{y}" width="{w}" height="{lidh}" fill="#EEE8DE"/>'
    s+=f'<rect x="{x}" y="{y}" width="{w}" height="{lidh}" fill="url(#baseL)"/>'
    s+=f'<line x1="{x}" y1="{y+lidh}" x2="{x+w}" y2="{y+lidh}" stroke="#000" stroke-opacity=".25" stroke-width="2"/>'
    # top face: lid artwork mapped to a parallelogram receding up and right
    sx=w/1000.0; sy=depth/1000.0; sh=-shift/1000.0
    s+=f'<clipPath id="topc"><path d="M{x},{y} L{x+w},{y} L{x+w+shift},{y-depth} L{x+shift},{y-depth} Z"/></clipPath>'
    s+=f'<g clip-path="url(#topc)"><g transform="matrix({sx:.4f},0,{sh:.5f},{sy:.4f},{x+shift},{y-depth})"><use href="#{lidart_id}"/></g>'
    s+=f'<path d="M{x},{y} L{x+w},{y} L{x+w+shift},{y-depth} L{x+shift},{y-depth} Z" fill="#fff" opacity=".12"/></g>'
    s+=f'<path d="M{x},{y} L{x+w},{y}" stroke="#fff" stroke-opacity=".7" stroke-width="1.5"/>'
    return s
def d_bag(W=1612,H=920):
    S=1000; lid,_=garden_lid(S)
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS]
    p.append(f'<defs><g id="lidart">{lid}</g></defs>')
    p.append(f'<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F1ECE4"/><stop offset="1" stop-color="#E9E3D9"/></linearGradient><rect width="{W}" height="{H*0.80}" fill="url(#wall)"/>')
    p.append(f'<rect y="{H*0.80}" width="{W}" height="{H*0.20}" fill="#DED6C8"/><rect width="{W}" height="{H}" filter="url(#noise)" opacity="0.08" style="mix-blend-mode:multiply"/>')
    p.append('<g transform="translate(-125,0)">')
    bx0,bx1,by0,by1=440,840,210,860; gus=60
    bw=bx1-bx0; bh=by1-by0
    p.append(f'<ellipse cx="{(bx0+bx1)/2+60}" cy="{by1+8}" rx="300" ry="26" fill="#3A3226" opacity=".28" filter="url(#soft)"/>')
    p.append(f'<path d="M{bx1},{by0} L{bx1+gus},{by0+18} L{bx1+gus},{by1-10} L{bx1},{by1} Z" fill="#E2DACC"/>')
    p.append(f'<path d="M{bx1+gus*0.5},{by0+9} L{bx1+gus*0.5},{by1-5}" stroke="#CFC6B6" stroke-width="2"/>')
    p.append(f'<clipPath id="bf"><rect x="{bx0}" y="{by0}" width="{bw}" height="{bh}"/></clipPath><g clip-path="url(#bf)"><rect x="{bx0}" y="{by0}" width="{bw}" height="{bh}" fill="{MOON}"/>')
    base=by1; art=[]
    art.append(g(fan_palm(R=160,spread=170,n=13),bx0+40,base+30,25))
    art.append(orchid_spray([(bx0+96,base+20),(bx0+102,base-60),(bx0+114,base-136),(bx0+110,base-200),(bx0+98,base-250)],[(1,-8,1.0),(2,8,0.95),(3,-10,0.85)],[(4,-25,0.85)]))
    art.append(g(frangipani(),bx0+180,base-22,10,1.15)); art.append(g(leaf(54,15),bx0+222,base-8,40)); art.append(g(frangipani(),bx0+262,base+6,-20,1.0))
    art.append(stem(f"M{bx1+10},{base-210} C{bx1-40},{base-180} {bx1-70},{base-125} {bx1-98},{base-60}",LW*1.4))
    art.append(g(leaf(48,16),bx1-40,base-186,-120)); art.append(g(leaf(46,15),bx1-80,base-124,-100))
    art.append(g(persimmon(r=19),bx1-62,base-148,6)); art.append(g(persimmon(r=16),bx1-100,base-52,-8))
    art.append(g(fan_palm(R=140,spread=160,n=11),bx1-10,base+30,-28))
    art.append(g(frangipani(),bx0+bw*0.6,base-6,25,1.05))
    p.append("".join(art))
    p.append(f'<rect x="{bx0}" y="{by0}" width="{bw}" height="{bh}" filter="url(#noise)" opacity="0.07" style="mix-blend-mode:multiply"/>')
    p.append(f'<linearGradient id="bagl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".25"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".06"/></linearGradient><rect x="{bx0}" y="{by0}" width="{bw}" height="{bh}" fill="url(#bagl)"/>')
    p.append(f'<rect x="{bx0}" y="{by0}" width="{bw}" height="46" fill="#000" opacity=".035"/><line x1="{bx0}" y1="{by0+46}" x2="{bx1}" y2="{by0+46}" stroke="#D8D0C2" stroke-width="1.5"/></g>')
    ax0,ax1,at,ab=bx0+bw*0.35,bx0+bw*0.65,by0+110,by0+320; r=(ax1-ax0)/2
    p.append(f'<path d="M{ax0},{ab} L{ax0},{at+r} A{r},{r} 0 0 1 {ax1},{at+r} L{ax1},{ab} Z" fill="none" stroke="url(#foilH)" stroke-width="2.4"/>')
    p.append(wordmark((bx0+bx1)/2,by0+236,bw*0.21,MID,"url(#foil)")+brandstar((bx0+bx1)/2,at+44,5.5,"url(#foil)"))
    hd=f"M{bx0+bw*0.30},{by0+28} C{bx0+bw*0.28},{by0-160} {bx0+bw*0.72},{by0-160} {bx0+bw*0.70},{by0+28}"
    p.append(f'<path d="{hd}" fill="none" stroke="#0B0F17" stroke-width="10" stroke-linecap="round"/><path d="{hd}" fill="none" stroke="#3A4560" stroke-width="2.5" stroke-dasharray="6 7" opacity=".7"/>')
    for hx in (bx0+bw*0.30, bx0+bw*0.70):
        p.append(f'<circle cx="{hx}" cy="{by0+30}" r="7.5" fill="url(#foil)" stroke="#8E7444" stroke-width="1"/>')
    # box beside the bag
    p.append(box_oblique(990, 700, 400, 50, 112, 92, "lidart"))
    p.append('</g></svg>')
    return "\n".join(p)
if __name__=="__main__":
    open('d-hero.svg','w').write(d_hero()); open('d-bag.svg','w').write(d_bag()); open('d-flat.svg','w').write(d_flat())
