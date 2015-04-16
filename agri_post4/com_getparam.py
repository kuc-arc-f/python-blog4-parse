# -*- coding: utf-8 -*- 

mHEAD="put_dat="

class getparamClass:

    def __init__(self):
        print ""

    def testmethod(self,str):
        print "call testmethod"
        print str

    def Is_fromMC(self,str):
    	ret=False
    	buf=str[0:8]
    	if buf==mHEAD:
    		ret=True
    	return ret

    def getDict(self,str):
    	ret = {"mc_id":"", "snum_1":"", "snum_2":"", "snum_3":"", "snum_4":"" }
        ret["mc_id"]   =str[8:12]
        ret["snum_1"]  =str[12:16]
        ret["snum_2"]  =str[16:20]
        ret["snum_3"]  =str[20:24]
        ret["snum_4"]  =str[24:28]
        return ret

