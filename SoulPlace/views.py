from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.messages.api import success
from SoulPlace.models import Feedback
from django.contrib.messages.api import success

# Create your views here.

def register(request):
    if request.method == 'POST':
        log = request.POST.get('log')

        if log=="no":
            username = request.POST.get('userId')
            email = request.POST.get('emailId')
            password = request.POST.get('password')

            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=email,email=email,password=password,first_name = username)
                user.save()
                user = auth.authenticate(username=email,email=email, password=password)
                auth.login(request,user)
                return redirect("trail")
        else:
            email = request.POST.get('emailId')
            password = request.POST.get('password')
            user = auth.authenticate(username=email,email=email, password=password)
            print(user)
            if user is not None:
                auth.login(request,user)
                return redirect("trail")
            else:
                messages.info(request,"Invalid credentials")
                return redirect("register")
    else:
        return render (request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('trail')        
    

original_questions = {
    # Format is 'question':[options]
    '1. Do you ever blame yourself for anything that happens in your life?':
    [
        "I don't feel I am any worse than anybody else",
        'I am critical of myself for my weaknesses or mistakes.',
        'I blame myself all the time for my faults.',
        'I blame myself for everything bad that happens.'
    ],
    '2. Have you ever thought of hurting yourself?':
    [
        "I don't have any thoughts of killing myself.",
        'I have thoughts of killing myself, but I would not carry them out.',
        'I would like to kill myself.',
        'I would kill myself if I had the chance.'
    ],
    '3. Do you cry more often?':
    [
        "I don't cry any more than usual.",
        'I cry more now than I used to.',
        'I cry all the time now.',
        "I used to be able to cry, but now I can't cry even though I want to."
    ],
    '4. Do you ever feel irritated?':
    [
        'I am no more irritated by things than I ever was.',
        'I am slightly more irritated now than usual.',
        'I am quite annoyed or irritated a good deal of the time.',
        'I feel irritated all the time.'
    ],
    "5. Do you ever feel you're losing interest in people?":
    [
        'I have not lost interest in other people.',
        'I am less interested in other people than I used to be.',
        'I have lost most of my interest in other people.',
        'I have lost all of my interest in other people.'
    ],
    '6. Can you make decisions on your own?':
    [
        'I make decisions about as well as I ever could.',
        'I put off making decisions more than I used to',
        'I have greater difficulty in making decisions more than I used to.',
        "I can't make decisions at all anymore."
    ],
    '7. What are your views on your appearance?':
    [
        "I don't feel that I look any worse than I used to.",
        'I am worried that I am looking old or unattractive.',
        'I feel there are permanent changes in my appearance that make me look unattractive .',
        'I believe that I look ugly.'
    ],
    '8. Do you face any difficulties working by yourself?':
    [
        'I can work about as well as before.', 'It takes an extra effort to get started at doing something.', 'I have to push myself very hard to do anything.', "I can't do any work at all."
    ],
    '9. How is your sleep schedule?':
    [
        'I can sleep as well as usual.',
        "I don't sleep as well as I used to.",
        'I wake up 1-2 hours earlier than usual and find it hard to get back to sleep.',
        'I wake up several hours earlier than I used to and cannot get back to sleep.'
    ],
    '10. Do you get tired easily?':
    [
        "I don't get more tired than usual.",
        'I get tired more easily than I used to.',
        'I get tired from doing almost anything.',
        'I am too tired to do anything.'
    ],
    '11. How would you describe your appetite?':
    [
        'My appetite is no worse than usual.',
        'My appetite is not as good as it used to be.',
        'My appetite is much worse now.',
        'I have no appetite at all anymore'
    ],
    '12. Have you lost weight recently?':
    [
        "I haven't lost much weight, if any, lately.",
        'I have lost more than five pounds.',
        'I have lost more than ten pounds.',
        'I have lost more than fifteen pounds.'
    ],
    '13. Are you worried about your health/ physical appearance?':
    [
        'I am no more worried about my health than usual.',
        'I am worried about physical problems like aches, pains, upset stomach, or constipation.',
        "I am very worried about physical problems and it's hard to think of much else.",
        'I am so worried about my physical problems that I cannot think of anything else.'
    ],
    '14. How do you feel about your interests/hobbies?':
    [
        'I have not noticed any recent change in my interests.',
        'I am less interested in my hobbies than I used to be.',
        'I have almost no interest in my hobbies.',
        'I have lost interest in my hobbies completely.'
    ],
    '15. Do you ever feel sad?':
    [
        'I do not feel sad.',
        'I feel sad.',
        "I am sad all the time and I can't snap out of it.",
        "I am so sad and unhappy that I can't stand it."
    ],

    '16. What are your views on the future?':
    [
        'I am not particularly discouraged about the future.',
        ' I feel discouraged about the future.',
        ' I feel I have nothing to look forward to.',
        ' I feel the future is hopeless and that things cannot improve.'],

    '17. Do you ever feel like a failure?':
    [
        'I do not feel like a failure.',
        'I feel I have failed more than the average person.',
        'As I look back on my life, all I can see is a lot of failures.',
        'I feel I am a complete failure as a person.'
    ],

    '18. Do you feel satisfied with life?':
    [
        'I get as much satisfaction out of things as I used to.',
        "I don't enjoy things the way I used to.",
        "I don't get real satisfaction out of anything anymore.",
        'I am dissatisfied or bored with everything.'
    ],

    '19. Do you ever feel guilty?':
    [
        "I don't feel particularly guilty.",
        'I feel guilty a good part of the time.',
        'I feel quite guilty most of the time.',
        'I feel guilty all of the time.'
    ],

    '20. Do you ever feel punished?':
    [
        "don't feel I am being punished.",
        'I feel I may be punished.',
        'I expect to be punished.',
        'I feel I am being punished.'
    ],

    '21. Do you ever feel disappointed in yourself?':
    [
        "I don't feel disappointed in myself.",
        'I am disappointed in myself.',
        'I am disgusted with myself.',
        'I hate myself.'
    ]
}

def test(request):
    questions = list(original_questions.keys())
    context = {"q": questions,"o": original_questions}
    return render(request, 'test.html',context)

def result(request):
    if request.method == "POST":
        score = 0
        mess=""

        for i in original_questions.keys():

            answered = request.POST.get(i)
            print(answered)

            if original_questions[i][0] == answered:
                score += 0
            elif original_questions[i][1] == answered:
                score += 1
            elif original_questions[i][2] == answered:
                score += 2
            elif original_questions[i][3] == answered:
                score += 3
            else :
                score = -1
                break

        if score==-1:
            mess="Please answer all the questions"
        elif score >= 0 and score <= 10:
            mess="These ups and downs are considered normal"
        elif score>=11 and score<=16:
            mess="Mild mood disturbance"
        elif score>=17 and score<=20:
            mess="Borderline clinical depression"
        elif score>=21 and score<=30:
            mess="Moderate depression"
        elif score>=31 and score<=40:
            mess="Severe depression"
        elif score>40:
            mess="Extreme depression"

        messages.add_message(request,20,mess)

        return render(request,'result.html', {'score':score})
    else:
        return redirect("test")










def trail(request):
    return render(request,'trail.html')
def review(request):
    return render(request,'review.html')
def feed(request):
    return render(request,'feed.html')
def base(request):
    return render(request,'base.html')
def exercise(request):
    return render(request,'exercise.html')
def feed2(request):
    return render(request,'feed2.html')
def ex1(request):
    return render(request,'ex1.html')
def ex2(request):
    return render(request,'ex2.html')

def ex3(request):
    return render(request,'ex3.html')

def ex4(request):
    return render(request,'ex4.html')

def ex5(request):
    return render(request,'ex5.html')

def ex6(request):
    return render(request,'ex6.html')

def ex7(request):
    return render(request,'ex7.html')

def ex8(request):
    return render(request,'ex8.html')

def ex9(request):
    return render(request,'ex9.html')

def ex10(request):
    return render(request,'ex10.html')
def feed(request):
    return render(request,'feed.html')
def feedback(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        number = request.POST['number']
        suggestion_p = request.POST['suggestion_p']

        new_Feedback = Feedback(fullname=fullname,email=email,number=number,suggestion_p=suggestion_p)

        new_Feedback.save()
        success = True
        return redirect('trail')
    else:
        return render (request,"feedback.html")


