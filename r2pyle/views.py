from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    context ={
        'questions': questions
    }
    # return HttpResponse('<h1>Rhyl Home</h1>')  # simple response
    return render(request, 'r2pyle/home.html', context)      # render method

def about(request):
    # return HttpResponse('<h1>Rhyl About</h1>')  # simple response
    return render(request, 'r2pyle/about.html')      # render method


questions = [
    {
        'qcontent': 'AI does not personally benefit me.',
    },
    {
        'qcontent': 'AI saves me time.',
    },
    {
        'qcontent': 'AI is likely to make decisions about people without their knowledge.',
    },
    {
        'qcontent': 'AI reduces mistakes made by humans.',
    },
    {
        'qcontent': 'I do not want organisations using AI to access my personal data.',
    },
    {
        'qcontent': 'AI improves the service I receive as a customer.',
    },
    {
        'qcontent': 'AI is likely to undermine human autonomy.',
    },
    {
        'qcontent': 'AI makes people more productive.',
    },
    {
        'qcontent': 'AI technologies are making human lives worse.',
    },
    {
        'qcontent': 'AI technologies are making human lives better.',
    }
]
