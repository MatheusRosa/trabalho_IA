import fuzzy_input
import fuzzy_output

def discover_centroid(degree):
  ret = [0]*180
  num = 0
  den = 0
  #small curve
  for i in range(0,120,10):
    if (fuzzy_output.output_small(i) < degree[0]):
      ret[i] = fuzzy_output.output_small(i)
    else:
      ret[i] = degree[0]
  #medium curve
  for i in range(120,140,10):
    if (fuzzy_output.output_medium(i) < degree[1]):
      ret[i] = fuzzy_output.output_medium(i)
    else:
      ret[i] = degree[1]
  #big curve
  for i in range(140,160,10):
    if (fuzzy_output.output_big(i) < degree[2]):
      ret[i] = fuzzy_output.output_big(i)
    else:
      ret[i] = degree[2]
  #very big curve
  for i in range(160,180,10):
    if (fuzzy_output.output_verybig(i) < degree[3]):
      ret[i] = fuzzy_output.output_verybig(i)
    else:
      ret[i] = degree[3]
     
   #calculate centroid
  for i in range(0,180,10):
    num += ret[i]*i
    den += ret[i]
  return (num/den)
  
   
if __name__ == "__main__":
  while 1:
    val = input("Put the weight of cargo:")
    vinput = [0,0,0,0]
    vinput[0] = fuzzy_input.input_small(val)
    vinput[1] = fuzzy_input.input_medium(val)
    vinput[2] = fuzzy_input.input_big(val)
    vinput[3] = fuzzy_input.input_verybig(val)
  
    i = discover_centroid(vinput)
    print "Centroide %s" %(i)