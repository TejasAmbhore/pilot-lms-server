from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from django.utils import timezone
from .models import Contact_us, Course, Review, Module, Video, Comment, SubComment, Notes,Monitor, Tags, Quiz, Question, Answer, Enrollment
from users.models import Profile, Student, Organization, Teacher
from datetime import datetime, timedelta
from django.contrib.gis.geoip2 import GeoIP2
from django_user_agents.utils import get_user_agent
import requests
import json
from django.urls import reverse
from .utils import searchCourses
from django.shortcuts import redirect
from django.http import JsonResponse

# Create your views here.
