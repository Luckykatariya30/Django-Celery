from django.shortcuts import render , redirect
from django_celery.celery import add
from myapp.tasks import sub
from celery.result import AsyncResult


# Enqueue Task using delay()
def home(request):
    # DELAY()..........!
    
    # print("Results: add of x + y ")
    # result1 = add.delay(10, 20)
    # print('Results: ',result1)
    
    # print("Results: sub. of x + y ")
    # result2  = sub.delay(20,10)
    # print('Results: ',result2)
    
    # APPLY_ASYNC()..............!
    
    print('Result: add of two values ')
    result1 = add.apply_async(args=[20,10])
    print('Results: ', result1)
    
    print('Result: sub. of two values ')
    result2 = sub.apply_async(args=[32,10])
    print('Results: ', result2)
    
    return render(request ,'myapp/home.html')

# Display addition value after task execution.
def home(request):
    result = add.delay(20,12)
    return render(request ,'myapp/home.html',{'result':result})

# SHOW RESULTS ......!

def check_result(request , task_id=None):
    if task_id != None:
        result = AsyncResult(task_id)
        print('Ready: ', result.ready())
        print('Successful: ', result.successful())
        print('Failed: ', result.failed())
        return render(request,'myapp/result.html',{'result':result})
    else:
        return HttpResponce('Request id = None give me any id. ')
def about(request):
    return redirect('/')


def contact(request):
    return render(request ,'myapp/contact.html')
