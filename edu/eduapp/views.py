from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
import json

# Create your views here.

def CourseView(request,cid):
    course = get_object_or_404(Course,cid =cname)
    # course = Course.objects.get(name = cname)
    # c = Course.objects.get(pk =0)
    # print c
    dic = {}
    dic['course_id'] = course.cid
    dic['course_name'] = course.name
    dic['lecture_count'] = course.nooflectures
    dic['description'] = course.description
    print dic
    return HttpResponse(json.dumps(dic), content_type='application/json')

def LectureView(request,cid,lid):
    dic = {}
    course = get_object_or_404(Course,cid =cid)
    lectures = Lecture.objects.filter(course = course)
    lec = get_object_or_404(lectures,lecid =lid)
    hrs = (lec.duration) / 60
    mins = (lec.duration)%60
    dic['lecture_id'] =  lec.lecid
    dic['lecture_name'] = lec.name
    dic['lecture_url'] = lec.videoid
    dic['courseid'] = cid
    dic['lecture_length'] = str(hrs) + ":" + str(mins)

    return HttpResponse(json.dumps(dic), content_type='application/json')
