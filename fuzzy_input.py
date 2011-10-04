#Output functions for degrees of truth
#Matheus da Rosa
#22/09/2011

def input_small(val):
    if val<100:
        ret = 1
    elif val>=100 and val<=200:
        ret = 1-((val-100)/100.0)
    elif val>200:
        ret = 0
    return ret

def input_medium(val):
    if val<100:
        ret = 0
    elif val>=100 and val<=200:
        ret = (val-100)/100.0
    elif val>=200 and val<=300:
        ret = 1-((val-200)/100.0)
    elif val>300:
        ret = 0
    return ret
    
def input_big(val):
    if val<200:
        ret = 0
    elif val>=200 and val<=300:
        ret = (val-200)/100.0
    elif val>=300 and val<=400:
        ret = 1-((val-300)/100.0)
    elif val>400:
        ret = 0
    return ret
    
def input_verybig(val):
    if val<300:
        ret = 0
    elif val>=300 and val<=400:
        ret = ((val-300)/100.0)
    elif val>400:
        ret = 1
    return ret

if __name__ == "__main__":
    val = 270
    print 'small = %s' %(input_small(val))
    print 'medium = %s' %(input_medium(val))
    print 'big = %s' %(input_big(val))
    print 'very big = %s' %(input_verybig(val))