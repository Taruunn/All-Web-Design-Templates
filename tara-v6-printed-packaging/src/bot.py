# Botanical motif library for the tara Garden print
import math, random
MID="#10151F"; MOON="#F4F1EA"; ORCH="#C9B1BB"; ORCH2="#A98C99"; PALM="#A7B19F"; PALM2="#8A977F"; GOLD="#C2A36B"
LW=1.15
def g(content, x=0, y=0, rot=0, s=1, flip=False):
    sx = -s if flip else s
    return f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f}) scale({sx:.3f},{s:.3f})">{content}</g>'
def leaf(L=60, W=18, fill=PALM, rib=True, lw=LW):
    # base at 0,0 pointing along +y negative (up)
    d=f"M0,0 C{W*0.9:.1f},{-L*0.25:.1f} {W*0.7:.1f},{-L*0.75:.1f} 0,{-L:.1f} C{-W*0.7:.1f},{-L*0.75:.1f} {-W*0.9:.1f},{-L*0.25:.1f} 0,0Z"
    s=f'<path d="{d}" fill="{fill}" stroke="{MID}" stroke-width="{lw}" stroke-linejoin="round"/>'
    if rib: s+=f'<path d="M0,{-L*0.05:.1f} Q{W*0.12:.1f},{-L*0.5:.1f} 0,{-L*0.9:.1f}" fill="none" stroke="{MID}" stroke-width="{lw*0.6:.2f}" stroke-linecap="round"/>'
    return s
def petal(L, W, fill, lw=LW, skew=0):
    d=f"M0,0 C{W+skew:.1f},{-L*0.2:.1f} {W*0.9+skew:.1f},{-L*0.85:.1f} {skew*0.5:.1f},{-L:.1f} C{-W*0.9+skew:.1f},{-L*0.85:.1f} {-W+skew:.1f},{-L*0.2:.1f} 0,0Z"
    return f'<path d="{d}" fill="{fill}" stroke="{MID}" stroke-width="{lw}" stroke-linejoin="round"/>'
def orchid(lw=LW):
    # Vanda Miss Joaquim, facing viewer, ~40 radius
    s=""
    for a,L,W in ((-128,30,9),(128,30,9)):   # lateral sepals (behind)
        s+=g(petal(L,W,ORCH,lw),0,0,a)
    s+=g(petal(32,11,ORCH,lw),0,0,0)          # dorsal sepal
    for a in (-66,66):                        # broad lateral petals
        s+=g(petal(34,15,ORCH,lw),0,0,a)
    # lip (labellum): broad fan, deeper tone, with fine veins
    lip=f'<path d="M0,2 C-14,8 -22,27 -12,35 C-5,40 5,40 12,35 C22,27 14,8 0,2Z" fill="{ORCH2}" stroke="{MID}" stroke-width="{lw}" stroke-linejoin="round"/>'
    for vx in (-9,-3,3,9):
        lip+=f'<path d="M0,8 Q{vx*0.6:.1f},20 {vx*0.9:.1f},31" fill="none" stroke="{MID}" stroke-width="{lw*0.5:.2f}" stroke-linecap="round"/>'
    s+=lip
    s+=f'<ellipse cx="0" cy="2" rx="5" ry="6" fill="{MOON}" stroke="{MID}" stroke-width="{lw}"/>'
    return s
def bud(lw=LW):
    return f'<path d="M0,0 C7,-6 7,-18 0,-24 C-7,-18 -7,-6 0,0Z" fill="{ORCH}" stroke="{MID}" stroke-width="{lw}"/>'
def frangipani(lw=LW):
    s=""
    pd="M0,0 C9,-5 21,-20 16,-36 C11,-48 -6,-46 -9,-32 C-11,-22 -5,-8 0,0Z"
    for i in range(5):
        s+=f'<path d="{pd}" transform="rotate({i*72})" fill="#FBF9F4" stroke="{MID}" stroke-width="{lw}" stroke-linejoin="round"/>'
    for i in range(5):
        s+=f'<path d="M0,0 Q3,-6 2,-12" transform="rotate({i*72+14})" fill="none" stroke="{MID}" stroke-width="{lw*0.55:.2f}" stroke-linecap="round"/>'
    s+=f'<circle cx="0" cy="0" r="3.2" fill="{ORCH}" stroke="{MID}" stroke-width="{lw*0.8:.2f}"/>'
    return s
def fan_palm(R=120, spread=200, n=15, lw=LW, fill=PALM):
    s=""
    a0=-90-spread/2
    for i in range(n):
        a=a0+spread*i/(n-1)
        L=R*(0.86+0.14*math.sin(math.pi*i/(n-1)))
        W=R*0.085
        seg=(f'<path d="M0,0 C{W:.1f},{-L*0.3:.1f} {W*1.1:.1f},{-L*0.8:.1f} {W*0.35:.1f},{-L:.1f} L0,{-L*0.93:.1f} L{-W*0.35:.1f},{-L:.1f} '
             f'C{-W*1.1:.1f},{-L*0.8:.1f} {-W:.1f},{-L*0.3:.1f} 0,0Z" fill="{fill}" stroke="{MID}" stroke-width="{lw}" stroke-linejoin="round"/>'
             f'<path d="M0,{-R*0.12:.1f} L0,{-L*0.9:.1f}" stroke="{MID}" stroke-width="{lw*0.5:.2f}"/>')
        s+=f'<g transform="rotate({a+90:.1f})">{seg}</g>'
    s+=f'<circle cx="0" cy="0" r="{R*0.07:.1f}" fill="{PALM2}" stroke="{MID}" stroke-width="{lw}"/>'
    return s
def persimmon(r=13, lw=LW, foil="url(#foil)"):
    s=f'<path d="M{-r:.1f},0 C{-r:.1f},{-r*0.8:.1f} {r:.1f},{-r*0.8:.1f} {r:.1f},0 C{r:.1f},{r*1.05:.1f} {-r:.1f},{r*1.05:.1f} {-r:.1f},0Z" fill="{foil}" stroke="{MID}" stroke-width="{lw}"/>'
    for a in (-60,-20,20,60):
        s+=g(f'<path d="M0,0 C3,-2 3.5,-5.5 0,-7.5 C-3.5,-5.5 -3,-2 0,0Z" fill="{PALM}" stroke="{MID}" stroke-width="{lw*0.8:.2f}"/>',0,-r*0.55,a)
    s+=f'<path d="M0,{-r*0.6:.1f} L1,{-r*1.05:.1f}" stroke="{MID}" stroke-width="{lw*1.2:.2f}" stroke-linecap="round"/>'
    return s
def sunbird(lw=LW):
    # faces right, perched; origin at feet
    s=""
    s+=f'<path d="M-20,-15 C-30,-12 -40,-6 -50,2 C-42,-2 -36,-4 -30,-6 C-36,-6 -42,-6 -48,-4 C-38,-12 -30,-17 -22,-20Z" fill="{PALM2}" stroke="{MID}" stroke-width="{lw}" stroke-linejoin="round"/>'  # tail
    s+=f'<path d="M-22,-16 C-18,-32 2,-38 14,-32 C22,-28 22,-16 14,-10 C4,-4 -12,-6 -22,-16Z" fill="#FBF9F4" stroke="{MID}" stroke-width="{lw}" stroke-linejoin="round"/>'  # body (pale belly)
    s+=f'<path d="M-22,-16 C-16,-30 2,-38 14,-32 C8,-30 -4,-24 -22,-16Z" fill="{PALM}" stroke="{MID}" stroke-width="{lw}" stroke-linejoin="round"/>'  # back
    s+=f'<path d="M-8,-24 C0,-31 10,-29 12,-23 C4,-19 -4,-19 -8,-24Z" fill="{PALM2}" stroke="{MID}" stroke-width="{lw*0.9:.2f}"/>'  # wing
    s+=f'<circle cx="17" cy="-33" r="7" fill="{PALM}" stroke="{MID}" stroke-width="{lw}"/>'  # head
    s+=f'<path d="M14,-27 C17,-24 20,-24 22,-27 C20,-30 16,-30 14,-27Z" fill="{MID}"/>'  # dark throat
    s+=f'<path d="M23,-34 C32,-35 40,-30 44,-22" fill="none" stroke="{MID}" stroke-width="{lw*1.1:.2f}" stroke-linecap="round"/>'  # beak
    s+=f'<circle cx="19" cy="-35" r="1.3" fill="{MID}"/>'
    s+=f'<path d="M-2,-8 L-4,0 M6,-9 L6,0" stroke="{MID}" stroke-width="{lw}" stroke-linecap="round"/>'  # legs
    return s
def stem(d, lw=LW*1.1):
    return f'<path d="{d}" fill="none" stroke="{MID}" stroke-width="{lw}" stroke-linecap="round"/>'
def orchid_spray(pts, heads, buds, lw=LW, flip=False):
    # pts: list of points for a smooth stem; heads/buds: (t-index, angle, scale)
    x0,y0=pts[0]
    d=f"M{x0},{y0} "+" ".join(f"Q{pts[i][0]},{pts[i][1]} {(pts[i][0]+pts[i+1][0])/2:.1f},{(pts[i][1]+pts[i+1][1])/2:.1f}" for i in range(1,len(pts)-1))+f" T{pts[-1][0]},{pts[-1][1]}"
    s=stem(d,lw*1.1)
    for (i,a,sc) in buds:
        x,y=pts[i]; s+=g(bud(lw/sc),x,y,a,sc)
    for (i,a,sc) in heads:
        x,y=pts[i]; s+=g(orchid(lw/sc),x,y,a,sc)
    return s
def leafy_branch(x0,y0,x1,y1,cx,cy,n=4,L=34,W=11,lw=LW,side=1):
    s=stem(f"M{x0},{y0} Q{cx},{cy} {x1},{y1}",lw*1.2)
    for k in range(n):
        t=(k+1)/(n+1)
        bx=(1-t)**2*x0+2*(1-t)*t*cx+t*t*x1; by=(1-t)**2*y0+2*(1-t)*t*cy+t*t*y1
        dx=2*(1-t)*(cx-x0)+2*t*(x1-cx); dy=2*(1-t)*(cy-y0)+2*t*(y1-cy)
        ang=math.degrees(math.atan2(dy,dx))
        sd = side if k%2==0 else -side
        s+=g(leaf(L*(0.8+0.3*((k*7)%3)/2),W),bx,by,ang+90+sd*55)
    return s
DEFS='''<defs>
<linearGradient id="foil" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#A9894F"/><stop offset=".38" stop-color="#E6D3A2"/><stop offset=".62" stop-color="#B8955A"/><stop offset="1" stop-color="#D9BE85"/></linearGradient>
<linearGradient id="foilH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B08F55"/><stop offset=".3" stop-color="#E6D3A2"/><stop offset=".55" stop-color="#B38F55"/><stop offset=".8" stop-color="#DCC28A"/><stop offset="1" stop-color="#A9894F"/></linearGradient>
<filter id="noise" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" result="n"/><feColorMatrix type="saturate" values="0"/></filter>
<filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="18"/></filter>
<filter id="soft2" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5"/></filter>
</defs>'''
LETTERS="M94.12 170.0H84.16000000000001V87.2H63.40000000000001V86.0H115.0V87.2H94.12ZM160.04 170.0H158.6L194.48 86.0L195.8 85.4L226.04 170.0H215.84L206.48 143.6H171.44ZM190.76 98.96000000000001 171.92 142.4H206.12ZM282.84 86.96000000000001Q296.76 86.0 307.44 86.0Q337.08 86.0 337.08 105.8Q337.08 114.2 333.0 120.80000000000001Q328.92 127.4 318.96 129.56L342.96 170.0H331.8L308.28 130.28H292.8V170.0H282.84ZM307.44 87.2Q300.48 87.2 292.8 88.04V129.07999999999998H310.56Q327.48 128.36 327.48 106.03999999999999Q327.48 96.92 322.44 92.06Q317.4 87.2 307.44 87.2ZM397.6 170.0H396.16L432.04 86.0L433.36 85.4L463.6 170.0H453.4L444.04 143.6H409.0ZM428.32 98.96000000000001 409.48 142.4H443.68Z"
STARP="M429.88,34.40 C431.18,53.30 431.18,53.30 442.88,55.40 C431.18,57.50 431.18,57.50 429.88,76.40 C428.58,57.50 428.58,57.50 416.88,55.40 C428.58,53.30 428.58,53.30 429.88,34.40 Z"
def wordmark(cx, cy, width, letters=MID, star=GOLD):
    # logo letters span x 63..464 (401 wide), y 34..170 ; centre on letters
    s=width/401.0
    return f'<g transform="translate({cx-263.5*s:.2f},{cy-128*s:.2f}) scale({s:.4f})"><path d="{LETTERS}" fill="{letters}"/><path d="{STARP}" fill="{star}"/></g>'
def brandstar(cx,cy,hw,fill=GOLD):
    hh=hw*21/13; px=hw*0.1; py=hh*0.1
    return (f'<path d="M{cx},{cy-hh} C{cx+px},{cy-py} {cx+px},{cy-py} {cx+hw},{cy} C{cx+px},{cy+py} {cx+px},{cy+py} {cx},{cy+hh} '
            f'C{cx-px},{cy+py} {cx-px},{cy+py} {cx-hw},{cy} C{cx-px},{cy-py} {cx-px},{cy-py} {cx},{cy-hh} Z" fill="{fill}"/>')
