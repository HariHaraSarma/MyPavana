from django import forms

from .models import Person, DealersInfo, ComplteStockDetails

class PostForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('user', 'pwd','first_name', 'last_name','age', 'email_id','dob','phone','address',)

class DealerForm(forms.ModelForm):

    class Meta:
        model = DealersInfo
        fields = ('person_info', 'company_name','dl1', 'dl2','tin',)
        
class StockForm(forms.ModelForm):

    class Meta:
        model = ComplteStockDetails
        fields = ('batch_num', 'item_name','company', 'price_per_unit','manf_date','exp_date', 'quantity', 'dealer', 'comments',)
        