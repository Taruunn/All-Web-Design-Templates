from bot import *
def garden_lid(S=1000, logo=True):
    # artwork for a square lid, S units. Arch window centred.
    ax0,ax1=S*0.30,S*0.70; atop=S*0.17; abot=S*0.86
    r=(ax1-ax0)/2
    arch=f"M{ax0},{abot} L{ax0},{atop+r} A{r},{r} 0 0 1 {ax1},{atop+r} L{ax1},{abot} Z"
    p=[]
    # --- bottom-left: big fan palm off the corner
    p.append(g(fan_palm(R=230,spread=170,n=15),S*0.07,S*1.02,28))
    p.append(g(fan_palm(R=150,spread=150,n=11),S*-0.02,S*0.70,62))
    # orchid spray climbing the left side of the arch
    p.append(orchid_spray([(S*0.17,S*1.0),(S*0.20,S*0.86),(S*0.23,S*0.72),(S*0.235,S*0.60),(S*0.22,S*0.50),(S*0.20,S*0.42),(S*0.17,S*0.36)],
                          [(2,-8,1.25),(3,10,1.15),(4,-12,1.0)],[(5,-20,1.1),(6,-35,0.9)]))
    p.append(leafy_branch(S*0.18,S*0.98,S*0.04,S*0.86,S*0.10,S*0.97,n=3,L=46,W=14))
    # frangipani pair at bottom
    p.append(g(frangipani(),S*0.30,S*0.94,8,1.55))
    p.append(g(frangipani(),S*0.40,S*0.985,-20,1.25))
    p.append(g(leaf(70,18),S*0.345,S*0.975,-50))
    p.append(g(leaf(64,16),S*0.47,S*1.0,40))
    # --- bottom-right: persimmon branch with two gold fruits, frangipani
    p.append(stem(f"M{S*1.02},{S*0.62} C{S*0.92},{S*0.66} {S*0.86},{S*0.74} {S*0.80},{S*0.86}",LW*1.6))
    p.append(stem(f"M{S*0.90},{S*0.67} C{S*0.88},{S*0.70} {S*0.875},{S*0.72} {S*0.873},{S*0.745}",LW*1.2))
    p.append(g(leaf(62,20),S*0.95,S*0.645,-120)); p.append(g(leaf(56,18),S*0.88,S*0.71,160))
    p.append(g(leaf(58,19),S*0.84,S*0.79,-100)); p.append(g(leaf(52,17),S*0.82,S*0.82,150))
    p.append(g(persimmon(r=25),S*0.873,S*0.785,6))
    p.append(g(persimmon(r=21),S*0.795,S*0.895,-8))
    p.append(g(fan_palm(R=200,spread=160,n=13),S*0.97,S*1.04,-30))
    p.append(g(frangipani(),S*0.70,S*0.96,30,1.45))
    p.append(g(leaf(66,17),S*0.64,S*0.99,-40)); p.append(g(leaf(60,16),S*0.75,S*1.0,55))
    # right side: small orchid spray rising
    p.append(orchid_spray([(S*0.93,S*0.62),(S*0.90,S*0.52),(S*0.86,S*0.44),(S*0.83,S*0.38),(S*0.82,S*0.32)],
                          [(1,20,1.0),(2,8,0.95)],[(3,-10,1.0),(4,-25,0.85)]))
    # --- top-right: sunbird on a slim branch from the corner
    p.append(stem(f"M{S*1.02},{S*0.10} C{S*0.94},{S*0.13} {S*0.86},{S*0.17} {S*0.78},{S*0.20}",LW*1.3))
    p.append(g(leaf(44,13),S*0.93,S*0.125,-60)); p.append(g(leaf(40,12),S*0.86,S*0.165,-130)); p.append(g(leaf(36,11),S*0.80,S*0.19,-50))
    p.append(g(sunbird(),S*0.885,S*0.148,-12,1.7,flip=True))
    # --- top-left: a quiet sprig from the corner
    p.append(leafy_branch(S*-0.02,S*0.04,S*0.16,S*0.20,S*0.06,S*0.16,n=4,L=40,W=12,side=-1))
    p.append(g(bud(),S*0.16,S*0.20,130,1.0))
    art="".join(p)
    out=[f'<clipPath id="lidclip"><rect width="{S}" height="{S}"/></clipPath>',
         f'<g clip-path="url(#lidclip)">',
         f'<rect width="{S}" height="{S}" fill="{MOON}"/>',
         # keep the window clear
         f'<mask id="win"><rect width="{S}" height="{S}" fill="#fff"/><path d="{arch}" fill="#000" stroke="#000" stroke-width="{S*0.03}"/></mask>',
         f'<g mask="url(#win)">{art}</g>',
         f'<path d="{arch}" fill="none" stroke="url(#foilH)" stroke-width="{S*0.0045}"/>',
         f'<path d="M{ax0+S*0.014},{abot-S*0.014} L{ax0+S*0.014},{atop+r} A{r-S*0.014},{r-S*0.014} 0 0 1 {ax1-S*0.014},{atop+r} L{ax1-S*0.014},{abot-S*0.014} Z" fill="none" stroke="url(#foilH)" stroke-width="{S*0.0016}"/>']
    if logo:
        out.append(wordmark(S*0.5,S*0.55,S*0.25,MID,"url(#foil)"))
        out.append(brandstar(S*0.5,S*0.28,S*0.010,"url(#foil)"))
    out.append('</g>')
    return "".join(out), arch
if __name__=="__main__":
    S=1000
    body,_=garden_lid(S)
    open('lid.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">{DEFS}{body}</svg>')
