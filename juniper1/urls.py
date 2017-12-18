from django.conf.urls import url
from . import views
from perlscripts import views as s
from javacode import views as j
from scriptsOptimization import views as so
from errorlogs import views as e
from usecase1 import views as usecase1
from django.contrib.auth.views import login
from AdaptivePlanning import views as a
from testcoverage import views as tc
from defectduplication import views as dd

urlpatterns=[
    url(r'^$', views.index, name='index1'),
    url(r'^about$', views.about, name='about'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^demo$', views.demo, name='demo'),
    url(r'^aspire$', views.aspire, name='aspire'),
    url(r'^perlscripts/$', s.index, name='index'),
    url(r'^javacode/$', j.index, name='index'),
    url(r'^scriptsOptimization/$', so.index, name='index'),
    url(r'^scriptsOptimization/result$', so.result, name='result'),
    url(r'^errorlogs/$', e.index, name='index'),
    url(r'^perlscripts/result/$', s.perl, name='perl'),
    url(r'^javacode/result/$', j.java, name='java'),
    url(r'^errorlogs/result/$', e.error_logs, name='Error_logs'),
    url(r'^usecase1/$', usecase1.metrics, name='usecase1'),
    url(r'^login/$', login, {'template_name':'registration/login.html'}),
    url(r'^AdaptivePlanning/$', a.adp, name='AdaptivePlanning'),
    url(r'^AdaptivePlanning/detail/$', a.check ,name='Adaptive'),
    url(r'^AdaptivePlanning/clicked/(?P<adaptive_id>[0-9]+)$', a.clicked, name='clicked'),
    url(r'^AdaptivePlanning/result/$', a.result, name='result'),
    url(r'^AdaptivePlanning/result/predict/$', a.predict, name='predict'),
    url(r'^about/releasenotes$', views.release, name='release'),
    url(r'^testcoverage/$', tc.index, name='index'),
    url(r'^testcoverage/result$', tc.index, name='scripts'),

    url(r'^help$', views.help, name='help'),
    url(r'^save/$', views.save, name='save'),
    url(r'^defectduplication/fileupload/$', dd.simple_upload, name='upload'),
    url(r'^defectduplication/$', dd.index, name='index'),
    url(r'^defectduplication/result$', dd.result, name='scripts'),

    url(r'^intoduction_to_juniper_usecases$', views.intoduction_to_juniper_usecases, name='intoduction_to_juniper_usecases'),
    url(r'^aspire_tool_kit$', views.aspire_tool_kit, name='aspire_tool_kit'),
    url(r'^installation_guide$', views.installation_guide, name='installation_guide'),
    url(r'^aspire_user_manual$', views.aspire_user_manual, name='aspire_user_manual'),
    url(r'^copyright$', views.copyright, name='copyright'),

    url(r'^releasenotes$', views.releasenotes, name='releasenotes'),
    url(r'^team$', views.team, name='team'),
    url(r'^defectfinal$', views.defectfinal, name='defectfinal'),
    url(r'^defect$', views.defect, name='defect'),

    ]




