from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from Library_App.models import ComplaintBox,Books_Avail,st_admin_data,User



class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
	class Meta:
		model=User
		fields=['username']
		widgets={"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"UserName",
			}),

		}
class Usperm(forms.ModelForm):
	class Meta:
		model = User
		fields=["username","role"]
		widgets={
		 "username":forms.TextInput(attrs={"class":"form-control","readOnly":True,}),
		 "role":forms.Select(attrs={"class":"form-control"}),
		}
class ComplaintForm(forms.ModelForm):
	class Meta:
		model=ComplaintBox
		fields="__all__"
# class ImForm(forms.ModelForm):
# 	class Meta:
# 		model=ImProfile
# 		fields=['age','gender',"impf"]
# 		widgets={
# 		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"update age",}),
# 		"gender":forms.Select(attrs={"class":"form-control","placeholder":"Select your gender",}),
# 		}

class UtupForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','email']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control"}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"updateemail",}),
		}

class ChPwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(
		attrs={'class':"form-control", 'placeholder':"enter old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(
		attrs={'class':"form-control", 'placeholder':"enter new password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(
		attrs={'class':"form-control", 'placeholder':"Confirm new password"}))
	class Meta:
		model=User
		fields='__all__'

class Books_AvailForm(forms.ModelForm):
	class Meta:
		model=st_admin_data
		fields=['Book_name','Book_author']
		widgets={"Book_name":forms.TextInput(attrs={"class":"form-control "
			,"placeholder":"Enter Book name","name":"Book_name","required":True}),
		"Book_author":forms.TextInput(attrs={"class":"form-control "
			,"placeholder":"Enter Book Author","required":True}),
		"Rg_No":forms.TextInput(attrs={"class":"form-control "
			,"placeholder":"Enter Registration Number","required":True}),
		"Branch":forms.TextInput(attrs={"class":"form-control "
			,"placeholder":"Enter u r Branch ","required":True}),
		"Name":forms.TextInput(attrs={"class":"form-control "
			,"placeholder":"Enter u r Name","required":True})}
class Books_AvailForm_admin(forms.ModelForm):
	class Meta:
		model=Books_Avail
		fields=['Book_name','Book_author','Book_count']
		widgets={"Book_name":forms.TextInput(attrs={"class":"form-control "
			,"placeholder":"Enter Book name","name":"Book_name","required":True}),
		"Book_author":forms.TextInput(attrs={"class":"form-control "
			,"placeholder":"Enter Book Author","name":"Book_author","required":True}),
		"Book_count":forms.NumberInput(attrs={"class":"form-control "
			,"placeholder":"No. of Books","name":"Book_count","required":True})}
class Expire_date(forms.ModelForm):
	class Meta:
		model=st_admin_data
		fields=['Issue_date','Expire_date']
		widgets={"Issue_date":forms.DateInput(attrs={"class":"form-control "
			,"placeholder":"Enter Issue_date","name":"issue","required":True}),
		"Expire_date":forms.DateInput(attrs={"class":"form-control "
			,"placeholder":"Enter Return date","name":"Expire","required":True})}

	
		

# class student_detailsForm(forms.ModelForm):
# 	class Meta:
# 		model=st_admin_data
# 		fields=['Rg_No','Branch','Name',]
# 		widgets={"Rg_No":forms.TextInput(attrs={"class":"form-control "
# 			,"placeholder":"Enter Registration Number","required":True}),
# 		"Branch":forms.TextInput(attrs={"class":"form-control "
# 			,"placeholder":"Enter u r Branch ","required":True}),
# 		"Name":forms.TextInput(attrs={"class":"form-control "
# 			,"placeholder":"Enter u r Name","required":True})}

		

