# -*- coding: utf-8 -*- 
import requests
import json
import urllib
import com_appConst
import com_func

#com_putParse
class putParseClass:

	def __init__(self):
		print ""

	def send_parse(self, dict, sTime):
		clsConst  = com_appConst.appConstClass()
		headers = {
		  "X-Parse-Application-Id": clsConst.mParse_APP_ID ,
		  "X-Parse-REST-API-Key": clsConst.mParse_REST_ID ,
		  "Content-Type": "application/json"
		}
		dtParam ={'mc_id': int(dict["mc_id"]) }
		dtParam["snum1"] = int(dict["snum_1"])
		dtParam["snum2"] = int(dict["snum_2"])
		dtParam["snum3"] = int(dict["snum_3"])
		dtParam["snum4"] = int(dict["snum_4"])
		dtParam["dtnum"] = int(sTime)
		
		try:
			r = requests.post('https://api.parse.com/1/classes/SenObject1', headers=headers , data=json.dumps(dtParam), timeout=30)
			print r.status_code
			print r.json()
		except:
			print "failue, send_parse"
			raise
		finally:
			print "End ,send_parse"

	def send_valve(self, dict, sTime, dMst):
		clsConst  = com_appConst.appConstClass()
		clsCom  = com_func.funcClass()
		headers = {
		  "X-Parse-Application-Id": clsConst.mParse_APP_ID ,
		  "X-Parse-REST-API-Key": clsConst.mParse_REST_ID ,
		  "Content-Type": "application/json"
		}
		k_flg_1=0
		k_flg_2=0
		k_flg_3=0
		k_flg_4=0
		if dMst["vnum_1"]==1L:
			k_flg_1= clsCom.Is_validValve( int(dict["snum_1"]) ,dMst["moi_num"] )
		if dMst["vnum_2"]==1L:
			k_flg_2= clsCom.Is_validValve( int(dict["snum_2"]) ,dMst["moi_num"])
		if dMst["vnum_3"]==1L:
			k_flg_3= clsCom.Is_validValve( int(dict["snum_3"]) ,dMst["moi_num"])
		if dMst["vnum_4"]==1L:
			k_flg_4= clsCom.Is_validValve( int(dict["snum_4"]) ,dMst["moi_num"])
		
		dtParam ={'mc_id': int(dict["mc_id"]) }
		dtParam["vnum1"] = k_flg_1
		dtParam["vnum2"] = k_flg_2
		dtParam["vnum3"] = k_flg_3
		dtParam["vnum4"] = k_flg_4
		dtParam["dtnum"] = int(sTime)
		try:
			r = requests.post('https://api.parse.com/1/classes/Vitem1', headers=headers , data=json.dumps(dtParam), timeout=30)
			print r.status_code
			print r.json()
		except:
			print "failue, send_parse"
			raise
		finally:
			print "End ,send_parse"

	def get_master(self, sId ):
		ret={}
		clsConst  = com_appConst.appConstClass()
		headers = {
		  "X-Parse-Application-Id": clsConst.mParse_APP_ID ,
		  "X-Parse-REST-API-Key": clsConst.mParse_REST_ID ,
		  "Content-Type": "application/json"
		}
		dtParam = {'mc_id': int(sId) };
		params = urllib.urlencode({"where":json.dumps(dtParam)})
		try:
			r = requests.get('https://api.parse.com/1/classes/MsObject?' +params, headers=headers ,  timeout=30)
			print r.status_code
			dRest = r.json()
			nCt= len(dRest["results"])
			print nCt
			if(nCt > 0):
				print dRest["results"][0]
			ret=dRest["results"][0]
		except:
			print "failue, send_parse"
			raise
		finally:
			print "End ,send_parse"
		return ret

