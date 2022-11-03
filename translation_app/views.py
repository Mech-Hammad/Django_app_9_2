from django.shortcuts import render
from .translate import translate


# Create your views here.
def translator_view(request):
    if request.method == 'POST':
        user_inp_text = request.POST['my_textarea']
        output = translate(user_inp_text)
        return render(request, 'translation_app/translator.html', {'output_text': output, 'original_text': user_inp_text})
    
    else:
        return render(request, 'translation_app/translator.html')