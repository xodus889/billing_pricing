from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from common.util.handlingData import HandlingPricig


def index(request):

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'project_list': ["AmazonEC2", "AmazonS3", "AmazonRDS", "AmazonRoute53",
                        "AWSLambda", "AmazonApiGateway", "AmazonCloudFront",
                         "AmazonCloudSearch", "AmazonCloudWatch", "AmazonDynamoDB"],
    }
    return HttpResponse(template.render(context, request))

def run(request, product):
    msg = 'My Message'
    createDate = '20181112'
    return render(request, 'index.html', {'message': msg})

def detail(request, product):
    return HttpResponse("You're looking at question %s." % product)

def results(request, product):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % product)

def vote(request, product):

    HandlingPricig.handlingData(product)
    response = "%s is completed"
    return HttpResponse(response % product)

