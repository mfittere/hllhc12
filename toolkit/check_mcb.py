#!/usr/bin/python

import sys
import gzip
import numpy as np

scale = 23348.89927; #Brho 7 TeV
#dictionary with maximum corrector strength
corrmax= {'acbx%s%s'%(pp,ii): 2.5 for ii in ['1','2'] for pp in ['h','v']}
corrmax.update({'acbx%s3'%(pp): 4.5 for pp in ['h','v']})
corrmax.update({'acbrd%s4'%(pp): 4.5 for pp in ['h','v']})
corrmax.update({'acby%ss4'%(pp): 4.5 for pp in ['h','v']})
corrmax.update({'acby%ss5'%(pp): 2.7 for pp in ['h','v']})
corrmax.update({'acbc%s%s'%(pp,ii): 2.8 for ii in ['6','7'] for pp in ['h','v']})

#dictionary with strength required for IT error correction
iterror= {'acbx%s1'%(pp): 0.92 for pp in ['h','v']}
iterror.update({'acbx%s2'%(pp): 1.40 for pp in ['h','v']})
iterror.update({'acbx%s3'%(pp): 0.78 for pp in ['h','v']})
iterror.update({'acbrd%s4'%(pp): 0.04 for pp in ['h','v']})
iterror.update({'acby%ss4'%(pp): 0.0 for pp in ['h','v']})
iterror.update({'acby%ss5'%(pp): 0.0 for pp in ['h','v']})
iterror.update({'acbc%s%s'%(pp,ii): 0.0 for ii in ['6','7'] for pp in ['h','v']})

def mk_dic(fn): 
  """create dictionary from mad output file"""
  corrs={}
  if fn.endswith('.gz'):
    fh=gzip.open(fn)
  else:
    fh=file(fn)
  for l in fh:
    [name,acb]=l.replace(' ','').replace(';','').split('=')
    corrs[name]=float(acb)
  return corrs

def print_acb(corrs,name,scale = 23348.89927):
  out=[name]
  tot=0
  for pp in ['x','s','o','ccp','ccm','ccs']:
    out.append(scale*corrs[name+pp])
  #iterror
  out.append(iterror[name.split('.')[0]])
  #calculate total strength
  tot = scale*max(abs(corrs[name+'x']),abs(corrs[name+'s']))
  for pp in ['o','ccp','ccm','ccs']:
    tot=tot+scale*abs(corrs[name+pp])
  tot = tot+iterror[name.split('.')[0]]#add strength necessary for IT error correction
  out.append(tot)
  #maximum and margin
  cmax=corrmax[name.split('.')[0]]
  out.append(cmax)
  out.append(abs(cmax-tot)*100/cmax)
  print ('%-15s'+'%7.2f'*10) % tuple(out)
  return out

def check_orbit(fn):
  print "Checking %s" % fn
  print "for 'tot' use maximum value over 'x' and 's'"
  corrs=mk_dic(fn)
  print('%50s') % ('corrector strength [Tm]')
  print('%-18s'+' %-6s'*10) % ('name','x','s','o','ccp','ccm','ccs','iterr','tot','max','margin [%]')
  outall=[]#list to save the maximum values in for the summary table
  for cc,ii in zip(['acbx','acbx','acbx','acbrd','acby','acby','acbc','acbc'],['1','2','3','4','s4','s5','6','7']): 
    outallmax=[]
    outmargin=[]
    for pp in 'h','v':
      for ss in 'l','r':
        if cc == 'acbx':
          name='%s%s%s.%s5'%(cc,pp,ii,ss)
          out=print_acb(corrs,name)
          outallmax.append(out[1:-1])#maximum strength
          outmargin.append([out[-1]])
        else:
          for bb in 'b1','b2':
            name='%s%s%s.%s5%s'%(cc,pp,ii,ss,bb)
            if name+'x' in corrs.keys():
              out=print_acb(corrs,name)
              outallmax.append(out[1:-1])#maximum strength
              outmargin.append([out[-1]])
    sout=(('-- '+name.split('.')[0]).ljust(15)+'%7.2f'*10) % tuple(max(outallmax)+min(outmargin))
    outall.append([sout])
    print sout
  print 'Summary table'
  print('%50s') % ('corrector strength [Tm]')
  print('%-18s'+' %-6s'*10) % ('name','x','s','o','ccp','ccm','ccs','iterr','tot','max','margin [%]')
  for ll in outall:
    print '%s'%(ll[0])

check_orbit(sys.argv[1])
