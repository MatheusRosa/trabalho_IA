#Input functions for degrees of truth
#Matheus da Rosa
#22/09/2011

def output_small(val):
    if val<100:
        ret = 1
    elif val>=100 and val<=120:
        ret = 1-((val-120)/100.0)
    elif val>120:
        ret = 0
    return ret

def output_medium(val):
    if val<100:
        ret = 0
    elif val>=100 and val<=120:
        ret = (val-100)/100.0
    elif val>=120 and val<=140:
        ret = 1-((val-120)/100.0)
    elif val>140:
        ret = 0
    return ret
    
def output_big(val):
    if val<120:
        ret = 0
    elif val>=120 and val<=140:
        ret = (val-120)/100.0
    elif val>=140 and val<=160:
        ret = 1-((val-300)/100.0)
    elif val>160:
        ret = 0
    return ret
    
def output_verybig(val):
    if val<140:
        ret = 0
    elif val>=140 and val<=160:
        ret = ((val-140)/100.0)
    elif val>160:
        ret = 1
    return ret
    
if __name__ == "__main__":
    val = 140
    print 'small = %s' %(output_small(val))
    print 'medium = %s' %(output_medium(val))
    print 'big = %s' %(output_big(val))
    print 'very big = %s' %(output_verybig(val))    
    