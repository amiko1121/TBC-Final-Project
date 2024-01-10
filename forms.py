from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, IntegerField, SubmitField, PasswordField,RadioField, DateField,SelectField,MultipleFileField,DecimalRangeField,TextAreaField,FloatField
from wtforms.validators import DataRequired , Length, EqualTo


class AddProductForm(FlaskForm):
    name=StringField("მანქანის სახელი", validators=[DataRequired(message="სახელის ველი სავალდებულოა")])
    price=IntegerField("მანქანის ფასი", validators=[DataRequired()])
    img= FileField("მანქანის მთავარი ფოტო", validators=[FileRequired(),FileAllowed(["jpg","png","jpeg"])])
    img2 = FileField("მანქანის ფოტო", validators=[FileRequired(),FileAllowed(["jpg","png","jpeg"])])
    img3 = FileField("მანქანის ფოტო", validators=[FileRequired(),FileAllowed(["jpg","png","jpeg"])])
    img4 = FileField("მანქანის ფოტო", validators=[FileRequired(),FileAllowed(["jpg","png","jpeg"])])
    img5 = FileField("აუქციონის ფოტო", validators=[FileRequired(),FileAllowed(["jpg","png","jpeg"])])
    colour = StringField("მანქანის ფერი", validators=[DataRequired()])
    coment=TextAreaField("მანქანის აღწერა",validators=[ Length(min=0, max=400)])
    engine = FloatField("ძრავის მოცულობა", validators=[DataRequired()])
    category=RadioField("მონიშნეთ კატეგორია", choices=[(1,"სედანი"),(2,"ჯიპი"),(3,"მძიმე ტექნიკა")])
    engine_type = RadioField("საწვავის ტიპი", choices=["დიზელი","ბენზინი","ჰიბრიდი"])
    year =IntegerField("მანქანის წლოვანება", validators=[DataRequired()])
    transmission = RadioField("ტრანსმისია", choices=["მექანიკა", "ავტომატიკა", "ტიპტრონიკი","ვარიატორი"])
    phonenumber1 = IntegerField("საკონტაქტო ნომერი",validators=[DataRequired()])
    interior_colour=StringField("სალონის ფერი", validators=[DataRequired()])
    cilindri=SelectField("ცილინდრების რაოდენობა",choices=["ცილინდრების რაოდენობა","2","3","4","5","6","8","10","12"])
    mileage = IntegerField("გარბენი კილომეტრებში", validators=[DataRequired()])
    submit=SubmitField("დამატება")



class RegisterForm(FlaskForm):
    username=StringField("შეიყვანეთ სახელი",validators=[DataRequired()])
    password=PasswordField("შეიყვანეთ პაროლი", validators=[DataRequired(), Length(min=8, max=64)])
    repeat_password=PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(),EqualTo("password")])
    gender=RadioField("აირჩიეთ სქესი", choices=["ქალი","კაცი"] ,validators=[DataRequired()])
    birthday=DateField("დაბადების თარიღი" ,validators=[DataRequired()])
    country=SelectField("მონიშნეთ ქვეყანა", choices=["United States", "Canada", "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and/or Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Cook Islands", "Costa Rica", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecudaor", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France, Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Republic of", "Korea, Republic of", "Kosovo", "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfork Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia South Sandwich Islands", "South Sudan", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbarn and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States minor outlying islands", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City State", "Venezuela", "Vietnam", "Virigan Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zaire", "Zambia", "Zimbabwe"],validators=[DataRequired()])
    phonenumber=IntegerField("შეიყვანეთ ტელეფონის ნომერი",validators=[DataRequired()])
    submit=SubmitField("რეგისტრაცია")

class LoginForm(FlaskForm):
    username=StringField("შეიყვანეთ სახელი", validators=[DataRequired()])
    password=PasswordField("შეიყვანეთ პაროლი", validators=[DataRequired(), Length(min=8, max=64)])
    submit = SubmitField("ავტორიზაცია")
