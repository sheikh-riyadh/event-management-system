from django import forms
from events.models import Event, Category, Participant


class StyleFormMixin:
    common_style = "border border-2 p-5 outline:none rounded"

    def apply_style_widget(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': f'{self.common_style} w-full',
                    'placeholder':f'please enter {field_name}'

                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f'{self.common_style} w-full',
                    'rows':4,
                    'placeholder':f'please enter {field_name}'
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': self.common_style,
                    'placeholder':f'please enter {field_name}'
                })
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({
                    'class': f'{self.common_style}',
                    'placeholder':f'please enter {field_name}'
                })
            elif isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs.update({
                    'class': self.common_style,
                    'placeholder':f'please enter {field_name}'
                })



class EventModelForm(StyleFormMixin ,forms.ModelForm):
    class Meta:
        model = Event

        exclude =['category']
        widgets={
            'date':forms.SelectDateWidget,
            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
    


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style_widget()


class EventCategoryModelForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style_widget()
    



class ParticipantModelForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

        widgets={
            'event': forms.SelectMultiple
        }
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style_widget()
        
