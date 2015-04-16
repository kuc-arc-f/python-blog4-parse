# -*- coding: utf-8 -*- 
import com_appConst

#com_func
class funcClass:

    def __init__(self):
        print ""
        
    def getZero_byNum(self, sNum ,nNum):
        ret="0000000000000000000"
        buf=ret+sNum
        #print len(buf)
        nLen = len(buf)
        nPos1= nLen-nNum
        ret= buf[nPos1:nLen]
        return ret
        
    def getResponse(self, dicGet , dicMst):
    	ret ="000000000000000000000000"
    	ret2=""
    	
    	k_flg_1=self.Is_validValve( int(dicGet["snum_1"]) ,dicMst["moi_num"])
    	k_flg_2=self.Is_validValve( int(dicGet["snum_2"]) ,dicMst["moi_num"])
    	k_flg_3=self.Is_validValve( int(dicGet["snum_3"]) ,dicMst["moi_num"])
    	k_flg_4=self.Is_validValve( int(dicGet["snum_4"]) ,dicMst["moi_num"])
        sMoi= self.getZero_byNum(str(dicMst["moi_num"]) ,4)
        sKai= self.getZero_byNum(str(dicMst["kai_num_1"]) ,3)
        ret2=ret2+sMoi
        if dicMst["vnum_1"]==1L:
        	ret2=ret2+str(k_flg_1)
        else:
        	ret2=ret2+"0"
        if dicMst["vnum_2"]==1L:
        	ret2=ret2+str(k_flg_2)
        else:
        	ret2=ret2+"0"
        if dicMst["vnum_3"]==1L:
        	ret2=ret2+str(k_flg_3)
        else:
        	ret2=ret2+"0"
        if dicMst["vnum_4"]==1L:
        	ret2=ret2+str(k_flg_4)
        else:
        	ret2=ret2+"0"
        ret2=ret2 + sKai + "000000000"
        #print ret2
        return ret2
        
    # @return TRUE: opne-Valve
    def Is_validValve(self, iSen , iMoi):
    	clsConst = com_appConst.appConstClass()
    	ret=clsConst.mNG_CODE
    	if(iMoi > iSen ):
    		ret=clsConst.mOK_CODE
    	return ret
    	
    def conv_senValue(self, dSrc , dMst):
    	ret={}
    	
    	ret=dSrc
    	if dMst["vnum_1"]==0:
    		dSrc["snum_1"]=0
    	if dMst["vnum_2"]==0:
    		dSrc["snum_2"]=0
    	if dMst["vnum_3"]==0:
    		dSrc["snum_3"]=0
    	if dMst["vnum_4"]==0:
    		dSrc["snum_4"]=0
    	
    	return ret
    	
