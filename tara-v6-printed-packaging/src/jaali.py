import sys
MID="#10151F"; GOLD="#C2A36B"
def star(cx,cy,hw,hh):
    # brand star: half width hw, half height hh, pinch 0.1
    px=hw*0.1; py=hh*0.1
    return (f"M{cx:.2f},{cy-hh:.2f} C{cx+px:.2f},{cy-py:.2f} {cx+px:.2f},{cy-py:.2f} {cx+hw:.2f},{cy:.2f} "
            f"C{cx+px:.2f},{cy+py:.2f} {cx+px:.2f},{cy+py:.2f} {cx:.2f},{cy+hh:.2f} "
            f"C{cx-px:.2f},{cy+py:.2f} {cx-px:.2f},{cy+py:.2f} {cx-hw:.2f},{cy:.2f} "
            f"C{cx-px:.2f},{cy-py:.2f} {cx-px:.2f},{cy-py:.2f} {cx:.2f},{cy-hh:.2f} Z")
def build(W,H,w,h,k=0.62,lw=3.0,starhw=16,ox=0,oy=0,ground=MID,ink=GOLD,dots=True):
    # nodes at (i*w, j*h) where i+j even ; S-curves between diagonal neighbours with vertical tangents
    paths=[]; stars=[]; dd=[]
    i0=int(-2); i1=int(W/w)+3; j0=-2; j1=int(H/h)+3
    for j in range(j0,j1):
        for i in range(i0,i1):
            if (i+j)%2: continue
            x=i*w+ox; y=j*h+oy
            for dx in (-1,1):
                x2=x+dx*w; y2=y+h
                paths.append(f"M{x:.2f},{y:.2f} C{x:.2f},{y+k*h:.2f} {x2:.2f},{y2-k*h:.2f} {x2:.2f},{y2:.2f}")
            if dots: dd.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{lw*1.5:.2f}" fill="{ink}"/>')
    # cell centres: nodes with (i+j) odd
    for j in range(j0,j1):
        for i in range(i0,i1):
            if (i+j)%2==0: continue
            x=i*w+ox; y=j*h+oy
            stars.append(star(x,y,starhw,starhw*21/13))
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" fill="{ground}"/>',
         f'<path d="{" ".join(paths)}" fill="none" stroke="{ink}" stroke-width="{lw}" stroke-linecap="round"/>',
         f'<path d="{" ".join(stars)}" fill="{ink}"/>', *dd, '</svg>']
    return "\n".join(svg)
if __name__=="__main__":
    open("jaali-flat.svg","w").write(build(1600,900,100,140,k=0.6,lw=3.2,starhw=13,ox=0,oy=30))
    open("jaali-tile.svg","w").write(build(600,600,60,84,k=0.6,lw=2,starhw=8,ox=0,oy=0))
