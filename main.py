from services import adop
import config
cond=True
while cond:
    user=eval(input("1.Today’s APOD \n2.Today’s APOD with image \n3.APOD by date \n4.APOD by date with image \n0.Exit\n"))
    match user:
        case 1:
            adop.show_details(config.api_url['APOD'])            
        case 2:
            adop.show_details(config.api_url['APOD'],img=True)            
        case 3:
            date_input=input("Date(MM-DD-YYY): ")
            try:
                adop.show_details(config.api_url['APOD'])  
            except Exception as e:
                print('The date should be in the MM-DD-YYYY format.')
        case 4:
            date_input=input("Date(MM-DD-YYY): ")
            try:
                adop.show_details(config.api_url['APOD'],img=True)  
            except Exception as e:
                print('The date should be in the MM-DD-YYYY format.')           
        case 0:
            cond=False
            