# -*- coding:utf-8 -*-
from django.http.response import HttpResponse
from cminit import *
from django.shortcuts import render,render_to_response
from django.template.response import TemplateResponse
from .models import *
# Create your views here.
def kuayu(response):
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def test(requset):
	response = "ok"
	result = {"result": "ok"}
	response = HttpResponse(json.dumps(result, ensure_ascii=False)) 
	return kuayu(response)

def record(requset):
	nowTime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_")
	cord = requset.GET.get('cord','')
	cord = nowTime + " : " + cord
	txt = os.path.join(TEMP_DIR, nowTime + ".txt")
	# file = open(txt, 'wb')
	# file.write(cord)
	# file.close()
	result = {"result": cord}
	response = HttpResponse(json.dumps(result, ensure_ascii=False)) 
	return kuayu(response)

def hello(requset):
	# response = HttpResponse("hello") 
	tmptab = Class.objects.filter(name = "main")
	now = datetime.now()
	helloTab = {"current_date": now, "imgPath": tmptab[0].photo.name}
	print helloTab
	response = render_to_response("hello.html", helloTab)
	return response
    
def countUmeng(requset):
	print "---countUmeng---"
	name = requset.GET.get('name', '')
	desc = requset.GET.get('desc', '')
	print name
	print desc
	finds = Umeng.objects.filter(name = name)
	if len(finds) == 0:
		record = Umeng(name = name, log = desc, countTime = 1)
		record.save()
	else:
		find = finds[0]
		find.name = name
		find.desc = "why"
		find.countTime = find.countTime + 1
		find.save()
	# print "--finds--"
	# print finds
	return HttpResponse("ok")
	# cultday = abs(int(cultday)) + 1
	# log = AndLog.objects.filter(only_id=tmp_onlyid)