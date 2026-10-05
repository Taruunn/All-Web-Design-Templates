from bot import *
from scenes_d import linen
import math
def jaali_paths(x0,y0,W,H,w,h,k=0.6,starhw=10,fx=None,margin=2):
    f = fx or (lambda x,y:(x,y))
    P=[]; S=[]; D=[]
    i0=-margin; i1=int(W/w)+margin+1; j0=-margin; j1=int(H/h)+margin+1
    def pt(x,y):
        X,Y=f(x,y); return f"{X:.1f},{Y:.1f}"
    for j in range(j0,j1):
        for i in range(i0,i1):
            x=x0+i*w; y=y0+j*h
            if (i+j)%2==0:
                for dx in (-1,1):
                    x2=x+dx*w; y2=y+h
                    P.append(f"M{pt(x,y)} C{pt(x,y+k*h)} {pt(x2,y2-k*h)} {pt(x2,y2)}")
                D.append(f(x,y))
            else:
                # star as polygon of transformed control points
                hh=starhw*21/13; hw=starhw; px=hw*0.1; py=hh*0.1
                pts=[(x,y-hh),(x+px,y-py),(x+px,y-py),(x+hw,y),(x+px,y+py),(x+px,y+py),(x,y+hh),(x-px,y+py),(x-px,y+py),(x-hw,y),(x-px,y-py),(x-px,y-py)]
                q=[pt(*p) for p in pts]
                S.append(f"M{q[0]} C{q[1]} {q[2]} {q[3]} C{q[4]} {q[5]} {q[6]} C{q[7]} {q[8]} {q[9]} C{q[10]} {q[11]} {q[0]} Z")
    return " ".join(P), " ".join(S), D
def jaali_layer(x0,y0,W,H,w,h,lw,starhw,ink=GOLD,fx=None,dotr=None,opacity=1):
    P,S,D=jaali_paths(x0,y0,W,H,w,h,starhw=starhw,fx=fx)
    dots="".join(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{dotr or lw*1.5:.2f}" fill="{ink}"/>' for X,Y in D)
    return f'<g opacity="{opacity}"><path d="{P}" fill="none" stroke="{ink}" stroke-width="{lw}" stroke-linecap="round"/><path d="{S}" fill="{ink}"/>{dots}</g>'
def e_flat(W=1612,H=920):
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS,f'<rect width="{W}" height="{H}" fill="{MID}"/>']
    p.append(jaali_layer(0,40,W,H,96,134,4.2,14))
    # subtle cotton-silk texture
    p.append(f'<rect width="{W}" height="{H}" filter="url(#noise)" opacity="0.10" style="mix-blend-mode:screen"/>')
    p.append('</svg>'); return "\n".join(p)
def bilinear(quad, W, H, x0, y0):
    (ax,ay),(bx,by),(cx,cy),(dx,dy)=quad  # TL,TR,BR,BL
    def f(x,y):
        u=(x-x0)/W; v=(y-y0)/H
        tx=ax+(bx-ax)*u; ty=ay+(by-ay)*u
        bxx=dx+(cx-dx)*u; byy=dy+(cy-dy)*u
        return (tx+(bxx-tx)*v, ty+(byy-ty)*v)
    return f
def rattan(d, w=24):
    return (f'<path d="{d}" fill="none" stroke="#000" stroke-opacity=".25" stroke-width="{w}" filter="url(#soft2)" transform="translate(8,12)"/>'
            f'<path d="{d}" fill="none" stroke="#9C7443" stroke-width="{w}" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="#C99E62" stroke-width="{w*0.78}" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="#B48649" stroke-width="{w*0.78}" stroke-dasharray="2 34" stroke-linecap="butt"/>'
            f'<path d="{d}" fill="none" stroke="#E9CF9B" stroke-width="{w*0.22}" stroke-linecap="round" transform="translate(-3,-4)" opacity=".85"/>')
def tassel(x,y,cord_from):
    cx0,cy0=cord_from
    s=f'<path d="M{cx0},{cy0} C{cx0+30},{cy0+20} {x-6},{y-60} {x},{y-14}" fill="none" stroke="#0B0F17" stroke-width="4.5" stroke-linecap="round"/>'
    # fringe
    strands=""
    for i in range(23):
        t=i/22; sx=x-20+40*t; ex=x-30+60*t
        col=["#B89DA9","#C9B1BB","#A88A98","#D6C3CB"][i%4]
        strands+=f'<path d="M{sx:.1f},{y+30} C{sx:.1f},{y+70} {ex:.1f},{y+100} {ex:.1f},{y+142}" fill="none" stroke="{col}" stroke-width="3.2" stroke-linecap="round"/>'
    s+=f'<ellipse cx="{x+8}" cy="{y+150}" rx="34" ry="8" fill="#000" opacity=".18" filter="url(#soft2)"/>'+strands
    s+=f'<linearGradient id="tsh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".18"/><stop offset=".4" stop-color="#fff" stop-opacity=".22"/><stop offset="1" stop-color="#000" stop-opacity=".22"/></linearGradient>'
    s+=f'<path d="M{x-21},{y+30} L{x+21},{y+30} L{x+31},{y+142} L{x-31},{y+142} Z" fill="url(#tsh)"/>'
    # cap + band
    s+=f'<path d="M{x-14},{y+4} C{x-14},{y-16} {x+14},{y-16} {x+14},{y+4} L{x+22},{y+30} L{x-22},{y+30} Z" fill="url(#foil)" stroke="#8E7444" stroke-width="1.2"/>'
    s+=f'<rect x="{x-23}" y="{y+26}" width="46" height="7" rx="3" fill="url(#foilH)" stroke="#8E7444" stroke-width="1"/>'
    # star charm on a short chain
    s+=f'<path d="M{x+12},{y-8} L{x+30},{y+40}" stroke="url(#foilH)" stroke-width="2" stroke-dasharray="3 2"/>'
    s+=f'<circle cx="{x+30}" cy="{y+42}" r="3" fill="none" stroke="#B8955A" stroke-width="1.5"/>'
    s+=brandstar(x+30,y+66,13,"url(#foil)")
    return s
def e_hero(W=1640,H=1200):
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS]
    p.append(f'<linearGradient id="wl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F4EFE7"/><stop offset="1" stop-color="#E7E0D4"/></linearGradient><rect width="{W}" height="{H}" fill="url(#wl)"/>')
    p.append(f'<linearGradient id="fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E2D9C9"/><stop offset="1" stop-color="#D6CCBA"/></linearGradient><rect y="860" width="{W}" height="{H-860}" fill="url(#fl)"/>')
    p.append(f'<rect y="858" width="{W}" height="3" fill="#fff" opacity=".5"/><rect width="{W}" height="{H}" filter="url(#noise)" opacity="0.09" style="mix-blend-mode:multiply"/>')
    p.append('<g transform="translate(820,1000) scale(1.16) translate(-820,-1000)">')
    X0,X1,YT,YB=470,1170,600,1000; seam=YT+120; dep=130; ins=52
    Wc=X1-X0
    # floor shadow
    p.append(f'<ellipse cx="{(X0+X1)/2+40}" cy="{YB+10}" rx="{Wc*0.62}" ry="40" fill="#2E2619" opacity=".35" filter="url(#soft)"/>')
    # top face trapezoid
    quad=[(X0+ins,YT-dep),(X1-ins,YT-dep),(X1,YT),(X0,YT)]
    tq=" ".join(f"{a:.1f},{b:.1f}" for a,b in quad)
    p.append(f'<clipPath id="topf"><polygon points="{tq}"/></clipPath><g clip-path="url(#topf)"><polygon points="{tq}" fill="#161C29"/>')
    fx=bilinear(quad, Wc, 440, X0, 0)
    p.append(jaali_layer(X0,0,Wc,440,54,76,2.2,7.5,fx=fx,dotr=2.6))
    p.append(f'<polygon points="{tq}" fill="#fff" opacity=".07"/></g>')
    # front face
    p.append(f'<clipPath id="frf"><rect x="{X0}" y="{YT}" width="{Wc}" height="{YB-YT}" rx="10"/></clipPath><g clip-path="url(#frf)"><rect x="{X0}" y="{YT}" width="{Wc}" height="{YB-YT}" fill="{MID}"/>')
    p.append(jaali_layer(X0-27,YT-20,Wc+60,YB-YT+60,54,76,2.6,8.2,dotr=3))
    p.append(f'<linearGradient id="frl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".07"/><stop offset=".5" stop-color="#000" stop-opacity=".05"/><stop offset="1" stop-color="#000" stop-opacity=".38"/></linearGradient><rect x="{X0}" y="{YT}" width="{Wc}" height="{YB-YT}" fill="url(#frl)"/>')
    p.append(f'<linearGradient id="frh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".25"/><stop offset=".35" stop-color="#fff" stop-opacity=".06"/><stop offset=".7" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".3"/></linearGradient><rect x="{X0}" y="{YT}" width="{Wc}" height="{YB-YT}" fill="url(#frh)"/>')
    p.append(f'<rect x="{X0}" y="{YT}" width="{Wc}" height="{YB-YT}" filter="url(#noise)" opacity="0.10" style="mix-blend-mode:screen"/></g>')
    # piping
    for (a,b,c,d) in ((X0,YT,X1,YT),(X0+4,seam,X1-4,seam),(X0+8,YB-2,X1-8,YB-2)):
        p.append(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#0A0D14" stroke-width="7" stroke-linecap="round"/><line x1="{a}" y1="{b-1}" x2="{c}" y2="{d-1}" stroke="url(#foilH)" stroke-width="3" stroke-linecap="round"/>')
    p.append(f'<polyline points="{X0+ins},{YT-dep} {X1-ins},{YT-dep}" fill="none" stroke="url(#foilH)" stroke-width="2.4"/>')
    p.append(f'<line x1="{X0}" y1="{YT}" x2="{X0+ins}" y2="{YT-dep}" stroke="url(#foilH)" stroke-width="2.4"/><line x1="{X1}" y1="{YT}" x2="{X1-ins}" y2="{YT-dep}" stroke="url(#foilH)" stroke-width="2.4"/>')
    # woven label
    lx,ly,lw_,lh=(X0+X1)/2,YT+60,190,58
    p.append(f'<rect x="{lx-lw_/2+3}" y="{ly-lh/2+5}" width="{lw_}" height="{lh}" fill="#000" opacity=".35" filter="url(#soft2)"/>')
    p.append(f'<rect x="{lx-lw_/2}" y="{ly-lh/2}" width="{lw_}" height="{lh}" fill="#F1ECE2"/>')
    p.append(f'<rect x="{lx-lw_/2+6}" y="{ly-lh/2+6}" width="{lw_-12}" height="{lh-12}" fill="none" stroke="#B8AE9C" stroke-width="1.2" stroke-dasharray="5 4"/>')
    p.append(wordmark(lx,ly+3,lw_*0.56,MID,"url(#foil)"))
    p.append(f'<rect x="{lx-lw_/2}" y="{ly-lh/2}" width="{lw_}" height="{lh}" filter="url(#noise)" opacity=".12" style="mix-blend-mode:multiply"/>')
    # handle mounts + rattan
    hy=YT-dep*0.5; hx0,hx1=(X0+X1)/2-130,(X0+X1)/2+130
    p.append(rattan(f"M{hx0},{hy} C{hx0-10},{hy-300} {hx1+10},{hy-300} {hx1},{hy}"))
    for hx in (hx0,hx1):
        p.append(f'<path d="M{hx-22},{hy+12} L{hx+22},{hy+12} L{hx+18},{hy-4} L{hx-18},{hy-4} Z" fill="url(#foil)" stroke="#7E6639" stroke-width="1.2"/>')
        p.append(f'<rect x="{hx-14}" y="{hy-30}" width="28" height="30" rx="5" fill="url(#foilH)" stroke="#7E6639" stroke-width="1.2"/>')
        p.append(f'<circle cx="{hx}" cy="{hy-16}" r="4" fill="#8E7444"/>')
    # tassel from right mount
    p.append(f'<g transform="translate({X1-80},{YT+60}) scale(1.35) translate({-(X1-80)},{-(YT+60)})">'+tassel(X1-80, YT+60, (hx1+6,hy-14))+'</g>')
    p.append('</g></svg>'); return "\n".join(p)
def bead(x,y,r): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="url(#bead)" stroke="#7A5E2C" stroke-width=".8"/>'
def pearl(x,y,r): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="url(#pearl)" stroke="#A79D8E" stroke-width=".6"/>'
def necklace(x0,y0,x1,sag):
    cx=(x0+x1)/2; cy=y0+sag*2
    def B(t): return ((1-t)**2*x0+2*(1-t)*t*cx+t*t*x1, (1-t)**2*y0+2*(1-t)*t*cy+t*t*y0)
    def N(t):
        dx=2*(1-t)*(cx-x0)+2*t*(x1-cx); dy=2*(1-t)*(cy-y0)+2*t*(y0-cy); L=math.hypot(dx,dy); return (-dy/L, dx/L)
    s=f'<path d="M{x0},{y0} Q{cx},{cy} {x1},{y0}" fill="none" stroke="url(#foilH)" stroke-width="4"/>'
    n=30
    units=""
    for i in range(n+1):
        t=i/n; x,y=B(t); nx,ny=N(t)
        if ny<0: nx,ny=-nx,-ny
        if 0.12<t<0.88 and abs(t-0.5)>0.06:
            ang=math.degrees(math.atan2(ny,nx))-90
            units+=(f'<g transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f})">'
                    f'<path d="M0,3 C13,9 13,32 0,44 C-13,32 -13,9 0,3Z" fill="url(#foil)" stroke="#7A5E2C" stroke-width="1"/>'
                    f'<path d="M0,10 C6,14 6,28 0,35 C-6,28 -6,14 0,10Z" fill="none" stroke="#8E7444" stroke-width=".9"/>'
                    f'<circle cx="0" cy="22" r="3.6" fill="#F6EFE0" stroke="#7A5E2C" stroke-width=".6"/>'
                    f'<path d="M0,44 L0,49" stroke="#B8955A" stroke-width="1.5"/>'
                    f'<circle cx="0" cy="55" r="6.5" fill="url(#pearl)" stroke="#A79D8E" stroke-width=".6"/></g>')
        units+=bead(x,y,7.5) if i%2==0 else pearl(x,y,5.5)
    s+=units
    mx,my=B(0.5)
    med=f'<g transform="translate({mx:.1f},{my+44:.1f}) scale(1.3)"><circle r="40" fill="url(#bead)" stroke="#7A5E2C" stroke-width="1.2"/>'
    for i in range(16):
        a=i/16*2*math.pi; med+=pearl(34*math.cos(a),34*math.sin(a),4.2)
    for i in range(8):
        med+=f'<path d="M0,0 C7,-6 7,-18 0,-24 C-7,-18 -7,-6 0,0Z" transform="rotate({i*45})" fill="url(#foil)" stroke="#7A5E2C" stroke-width=".8"/>'
    med+=f'<circle r="6" fill="#F6EFE0" stroke="#7A5E2C" stroke-width=".8"/>'
    for dx in (-16,0,16):
        med+=f'<path d="M{dx},{38 if dx else 40} L{dx},{50 if dx else 56}" stroke="url(#foilH)" stroke-width="2"/>'+pearl(dx,(56 if dx else 63),6.5 if dx==0 else 5.5)
    med+='</g>'
    s+=f'<path d="M{mx},{my} L{mx},{my+4}" stroke="url(#foilH)" stroke-width="3"/>'+med
    return s
def jhumka(x,y,s=1.0):
    o=f'<g transform="translate({x},{y}) scale({s})">'
    o+=f'<ellipse cx="6" cy="96" rx="40" ry="8" fill="#000" opacity=".15" filter="url(#soft2)"/>'
    o+=f'<circle cx="0" cy="0" r="15" fill="url(#bead)" stroke="#7A5E2C" stroke-width="1"/>'
    for i in range(8): o+=pearl(11*math.cos(i*math.pi/4),11*math.sin(i*math.pi/4),2.6)
    o+=f'<circle r="4" fill="#F6EFE0"/><path d="M0,15 L0,26" stroke="url(#foilH)" stroke-width="2.5"/>'
    o+=f'<path d="M-8,26 C-8,21 8,21 8,26 C26,30 34,54 34,74 C20,78 -20,78 -34,74 C-34,54 -26,30 -8,26Z" fill="url(#foil)" stroke="#7A5E2C" stroke-width="1.1"/>'
    for yy in (40,52,64): o+=f'<path d="M{-14-(yy-40)*0.6:.1f},{yy} Q0,{yy+5} {14+(yy-40)*0.6:.1f},{yy}" fill="none" stroke="#8E7444" stroke-width="1"/>'
    for i in range(9): o+=pearl(-28+7*i,82,4)
    o+='</g>'; return o
def e_open(W=1612,H=920):
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS]
    p.append('<defs><radialGradient id="bead" cx=".35" cy=".32" r=".75"><stop offset="0" stop-color="#F6E7BC"/><stop offset=".5" stop-color="#CBA765"/><stop offset="1" stop-color="#8A6A33"/></radialGradient>'
             '<radialGradient id="pearl" cx=".35" cy=".32" r=".75"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".6" stop-color="#EEE8DD"/><stop offset="1" stop-color="#BFB5A5"/></radialGradient>'
             '<radialGradient id="vel" cx=".5" cy=".45" r=".7"><stop offset="0" stop-color="#F3EEE6"/><stop offset="1" stop-color="#DCD3C4"/></radialGradient></defs>')
    p.append(linen(W,H))
    X0,X1=330,1290; LT,LB=40,400; BT,BB=420,890; rim=30
    p.append(f'<rect x="{X0+14}" y="{LT+24}" width="{X1-X0}" height="{BB-LT}" fill="#2E2619" opacity=".32" filter="url(#soft)"/>')
    for (yt,yb) in ((LT,LB),(BT,BB)):
        p.append(f'<clipPath id="r{yt}"><rect x="{X0}" y="{yt}" width="{X1-X0}" height="{yb-yt}" rx="12"/></clipPath><g clip-path="url(#r{yt})"><rect x="{X0}" y="{yt}" width="{X1-X0}" height="{yb-yt}" fill="{MID}"/>'
                 + jaali_layer(X0,yt,X1-X0,yb-yt,30,42,1.4,4.2,dotr=1.8) + '</g>')
        p.append(f'<rect x="{X0+rim}" y="{yt+rim}" width="{X1-X0-2*rim}" height="{yb-yt-2*rim}" rx="6" fill="url(#vel)"/>')
        p.append(f'<rect x="{X0+rim}" y="{yt+rim}" width="{X1-X0-2*rim}" height="{yb-yt-2*rim}" rx="6" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="5" filter="url(#soft2)"/>')
        p.append(f'<rect x="{X0+rim}" y="{yt+rim}" width="{X1-X0-2*rim}" height="{yb-yt-2*rim}" filter="url(#noise)" opacity=".10" style="mix-blend-mode:multiply"/>')
        p.append(f'<rect x="{X0+4}" y="{yt+4}" width="{X1-X0-8}" height="{yb-yt-8}" rx="10" fill="none" stroke="url(#foilH)" stroke-width="2"/>')
    # lid interior: foil wordmark + star
    p.append(wordmark((X0+X1)/2,(LT+LB)/2+14,270,"url(#foil)","url(#foil)"))
    # necklace cushion
    cx0,cx1,cy0,cy1=X0+230,X1-230,BT+70,BB-70
    p.append(f'<rect x="{cx0+6}" y="{cy0+10}" width="{cx1-cx0}" height="{cy1-cy0}" rx="40" fill="#000" opacity=".22" filter="url(#soft2)"/>')
    p.append(f'<radialGradient id="cush" cx=".5" cy=".35" r=".8"><stop offset="0" stop-color="#F6F2EB"/><stop offset="1" stop-color="#D8CEBE"/></radialGradient><rect x="{cx0}" y="{cy0}" width="{cx1-cx0}" height="{cy1-cy0}" rx="40" fill="url(#cush)"/>')
    p.append(necklace(cx0+34,cy0+34,cx1-34,118))
    # jhumka cushions
    for jx in (X0+120, X1-120):
        p.append(f'<ellipse cx="{jx+4}" cy="{(BT+BB)/2+8}" rx="70" ry="110" fill="#000" opacity=".18" filter="url(#soft2)"/><ellipse cx="{jx}" cy="{(BT+BB)/2}" rx="68" ry="108" fill="url(#cush)"/>')
        p.append(jhumka(jx,(BT+BB)/2-55,1.05))
    # hinge line
    p.append(f'<rect x="{X0+40}" y="{LB}" width="{X1-X0-80}" height="{BT-LB}" fill="#0A0D14"/>')
    # tassel lying on linen at right
    p.append(f'<g transform="rotate(-24 1450 640)">{tassel(1450,600,(1452,470))}</g>')
    p.append('</svg>'); return "\n".join(p)
if __name__=="__main__":
    open('e-flat.svg','w').write(e_flat()); open('e-hero.svg','w').write(e_hero()); open('e-open.svg','w').write(e_open())
