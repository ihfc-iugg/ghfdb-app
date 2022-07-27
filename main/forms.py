from django import forms
from database.models import Site
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Div, Row, Column, Field, HTML, Fieldset
from crispy_bootstrap5.bootstrap5 import FloatingField


class F(Field):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, template='main/partials/text_only_template.html', **kwargs)


class SiteForm(forms.ModelForm):

    class Meta:
        model = Site
        exclude = ['geom']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields.keys():
            self.fields[fieldname].widget.attrs['readonly'] = True
            self.fields[fieldname].help_text = None

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
                Fieldset(
                    HTML('<h5>Site Information</h5>'),
                    F('id'),
                    F('name'),
                    Row(Column(F('lat'),F('lng'))),
                    F('elevation'),
                ),
                Fieldset(
                    HTML('<h5>Site Information</h5>'),
                    F('q'),
                    F('q_unc'),
                    F('method'),
                    F('env'),
                    F('expl'),
                    F('wat_temp'),
                    F('q_comment'),
                ),
        )

# class SiteForm(forms.ModelForm):

#     class Meta:
#         model = Site
#         # fields = '__all__'
#         exclude = ['geom']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for fieldname in self.fields.keys():
#             self.fields[fieldname].widget.attrs['readonly'] = True
#             self.fields[fieldname].help_text = None

#         self.helper = FormHelper(self)
#         self.helper.layout = Layout(
#                 Fieldset(
#                     HTML('<h5>Site Information</h5>'),
#                     Field('name', template='main/partials/text_only_template.html'),
#                     Row(Column('lat'),Column('lng')),
#                 ),
#         )

class DownloadWithChoicesForm(forms.Form):
    download_type = forms.ChoiceField(
        label="Download Type",
        required=True,
        choices=[('basic','Basic'),
                ('standard','Standard'),
                ('detailed','Detailed')],
                )

    data_select = forms.MultipleChoiceField(
        label='Include',
        required=True,
        choices=[
            ('intervals','Heat Flow/Gradient'),
            ('temperature','Temperature'),
            ('conductivity','Thermal Conductivity'),
            ('heatproduction','Heat Production'),
        ],
        initial=['intervals','temperature','conductivity','heatproduction'],
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        fields = ['download_type','data_select']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'GET'
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
                Field('download_type'),
                Field('data_select'),
            ButtonHolder(
                Submit('submit', 'Download', css_class='button')
            )
        )

class DownloadBasicForm(forms.Form):
    download_type = forms.ChoiceField(
        label="Download Type",
        required=False,
        choices=[   ('standard','Standard'),
                    ('detailed','Detailed')])

    class Meta:
        fields = ['download_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
                Field('download_type', css_class='mb-2'),
                ButtonHolder(
                Submit('submit', 'Download', css_class='button mt-2')
            ))


